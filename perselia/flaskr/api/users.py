from models import sess, User, CustomField
import json
from api.functions import ok, errors


class Users(object):

    ''' api/users.register (REGISTERS USERS) '''
    def register(self, data, token):
        ids = []
        for user in data['users']:

            existing_user = sess.query(User).filter(User.email==user['email']).first()
            if existing_user is not None:
                return errors(['user_already_exists.json'])

            u = User(\
                firstname=user['firstname'],\
                lastname=user['lastname'],\
                email=user['email'],\
                avatar_url=user['avatar_url'],\
                password=user['password'],\
                master=user['master'],\
                token=token
            )

            # adding user to database
            sess.add(u)

            # flushing the session
            sess.flush()

            # refreshing the user object to obtain the new id
            sess.refresh(u)

            # collecting the id of the user
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
        if user is not None:
            if user.token != token:
                return errors(['bad_token.json'])

            sess.delete(user)
            sess.commit()

            return errors(None)
        else:
            return errors(['no_such_user.json'])

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