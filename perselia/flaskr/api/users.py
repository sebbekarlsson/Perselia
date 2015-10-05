from models import sess, User, CustomField
import json
from api.functions import ok


class Users(object):

    ''' api/users.register (REGISTERS USERS) '''
    def register(self, data, token):
        ids = []
        for user in data['users']:

            existing_user = sess.query(User).filter(User.email==user['email']).first()
            if existing_user is not None:
                return ok(False)

            u = User(\
                firstname=user['firstname'],\
                lastname=user['lastname'],\
                email=user['email'],\
                avatar_url=user['avatar_url'],\
                password=user['password'],\
                master=user['master'],\
                token=token
            )
            sess.add(u)
            sess.flush()

            sess.refresh(u)

            ids.append(u.id)

            for field in user['custom_fields']:
                customfield = CustomField(\
                    key=field['key'],\
                    value=field['value'], user_id=u.id\
                    )
                sess.add(customfield)
                sess.commit()

        return {'ids' : ids}

    ''' api/users.delete (DELETS USERS) '''
    def delete(self, data, token):
        user = sess.query(User).filter(User.id==data['id']).first()
        if user is not None and user.token == token:
            sess.delete(user)
            sess.commit()

            return ok(True)
        else:
            return ok(False)

    ''' api/users.list (LISTS USERS) '''
    def list(self, data, token):
        offset = data['offset']
        limit = data['max']

        users = sess.query(User).filter(User.token==token).offset(offset).limit(limit)

        returns = []

        for user in users:
            customfields = sess.query(CustomField).filter(CustomField.user_id==user.id).all()
            returns.append(\
                {\
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                    "email": user.email,
                    "avatar_url": user.avatar_url,
                    "password": user.password,
                    "master" : user.master,
                    "id": user.id,
                    "created": user.created,
                    
                    "custom_fields":\
                    [{"key": field.key, "value": field.value} for field in customfields]

                }
            )

        return {"users":returns}