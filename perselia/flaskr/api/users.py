from flask import session
from models import sess, User, CustomField
import json
from api.errors import throw_error
from api.functions import encrypt, decrypt, download_file, generate_name


class Users(object):

    ''' api/users.register (REGISTERS USERS) '''
    def register(self, data, token):
        ids = []

        if 'users' not in data:
            return throw_error(422, 'JSON missing users array')

        for user in data['users']:

            existing_user = sess.query(User).filter(User.email==user['email']).first()
            if existing_user is not None:
                return throw_error(202, 'User already exists')

            try:
                u = User(\
                    firstname=user['firstname'],\
                    lastname=user['lastname'],\
                    email=user['email'],\
                    avatar_url=user['avatar_url'],\
                    password=encrypt(user['password']),\
                    master=user['master'],\
                    token=token
                )
            except KeyError:
                return throw_error(422, 'Invalid data')

            # Validating the password, is it equal to the confirmation password?
            if u.password != encrypt(user['password_confirm']):
                return throw_error(202, 'Passwords does not match!')

            # Validating each field of the user
            for attr, value in u.__dict__.items():
                if value is '' or value is ' ' or value is None:
                    return throw_error(422, 'Value of {attribute} is empty.'.format(attribute=attr))

            # Validating the avatar_url, trying to download the file
            try:
                try:
                    dir = 'flaskr/static/upload/image/avatar/{filename}.jpg'.format(filename=generate_name())
                    download_file(u.avatar_url, dir)
                except ValueError:
                    return throw_error(422, 'avatar_url is invalid')
            except FileNotFoundError:
                return throw_error(500, 'Could not find directory where avatar should be saved:\n{dir}'.format(dir=dir))

            # adding user to database
            sess.add(u)

            # flushing the session
            sess.flush()

            # refreshing the user object to obtain the new id
            sess.refresh(u)

            # collecting the id of the user
            ids.append(u.id)

            # Adding custom_fields if there are any
            if 'custom_fields' in user:
                for field in user['custom_fields']:
                    customfield = CustomField(
                        key=field['key'],
                        value=field['value'], user_id=u.id\
                    )
                    sess.add(customfield)

            # Finally, we are saving the user
            sess.commit()

        return {'status' : 201, 'ids' : ids, "errors" : None}

    ''' api/users.delete (DELETES USERS) '''
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

    ''' api/users.get (FETCH USER BY EMAIL) '''
    def get(self, data, token):
        if data is None:
            return throw_error(400, 'Data is null')

        email = data['email']

        user = sess.query(User).filter(User.email==email).first()

        if user is None:
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

    ''' api/users.login (LOGINS USER) '''
    def login(self, data, token):
        user_data = self.get(data, token)
        if 'users' in user_data:
            users = user_data['users']
            if len(users) > 0:
                user = users[0]
            else:
                return throw_error(404, 'No matching users found')
        else:
            return throw_error(404, 'No matching users found')

        # Making sure we recieve a valid password
        if 'password' in data:
            request_pass = data['password']
        else:
            throw_error(422, 'No password provided')

        if 'password' in user:
            real_pass = decrypt(user['password'])
        else:
            throw_error(500, 'Could not find a password for this user')

        # Validation for the password
        ok = (request_pass == real_pass)

        # We are signing in the user if the validation of the password is valid
        if ok is True:
            session['user_id'] = user['id']
            return {'status': 200, 'user_id': session['user_id'] ,"errors": None}
        else:
            try:
                del session['user_id']
            except KeyError:
                pass

            return throw_error(202, 'Wrong password')
