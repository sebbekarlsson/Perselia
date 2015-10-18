from flask import session
from models import sess, User, CustomField
import json
from api.errors import throw_error
from api.functions import encrypt, decrypt


class Users(object):

    ''' api/users.register (REGISTERS USERS) '''
    def register(self, data, token):
        ids = []
        for user in data['users']:

            existing_user = sess.query(User).filter(User.email==user['email']).first()
            if existing_user is not None:
                return throw_error(202, 'User already exists')

            u = User(\
                firstname=user['firstname'],\
                lastname=user['lastname'],\
                email=user['email'],\
                avatar_url=user['avatar_url'],\
                password=encrypt(user['password']),\
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

        return {'status' : 201, 'ids' : ids, "errors" : None}

    ''' api/users.delete (DELETS USERS) '''
    def delete(self, data, token):
        user = sess.query(User).filter(User.id==data['id']).first()
        if user is not None:
            if user.token != token:
                return throw_error(400, 'Bad token')

            sess.delete(user)
            sess.commit()

            return throw_error(200, 'null')
        else:
            return throw_error(400, 'No such user')

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
                    "password": user.password.decode(encoding='UTF-8'),
                    "master" : user.master,
                    "id": user.id,
                    "created": user.created,
                    
                    "custom_fields":\
                    [{"key": field.key, "value": field.value} for field in customfields]

                }
            )

        return {'status' : 200, 'users' : returns}

    def get(self, data, token):
        email = data['email']

        user = sess.query(User).filter(User.email==email).first()

        if user is None:
            print('no such user')
            return throw_error(400, 'No such user')

        returns = []

        customfields = sess.query(CustomField).filter(CustomField.user_id==user.id).all()
        returns.append(\
            {\
                "firstname": user.firstname,
                "lastname": user.lastname,
                "email": user.email,
                "avatar_url": user.avatar_url,
                "password": user.password.decode(encoding='UTF-8'),
                "master" : user.master,
                "id": user.id,
                "created": user.created,
                
                "custom_fields":\
                [{"key": field.key, "value": field.value} for field in customfields]

            }
        )

        return {'status' : 200, 'users' : returns, "errors" : None}

    def login(self, data, token):

        try:
            user = self.get(data, token)['users'][0]
        except KeyError:
            return throw_error(400, 'No such user')

        ok = data['password'] == decrypt(user['password'])

        if ok is True:
            session['user_id'] = user['id']
            return {'status' : 200, "errors" : None}
        else:
            try:
                del session['user_id']
            except KeyError:
                pass

            return throw_error(202, 'Wrong password')
