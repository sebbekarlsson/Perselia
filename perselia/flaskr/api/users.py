from models import sess, User, CustomField
import json


class Users(object):
    def register(self, data):
        ids = []
        for user in data['users']:
            u = User(\
                firstname=user['firstname'],\
                lastname=user['lastname'],\
                email=user['email'],\
                avatar_url=user['avatar_url'],\
                password=user['password']\
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