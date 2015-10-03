from models import sess, User, CustomField
import json


class Users(object):
    def register(self, data, token):
        ids = []
        for user in data['users']:
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

    def delete(self, data, token):
        user = sess.query(User).filter(User.id==data['id']).first()
        if user is not None and user.token == token:
            sess.delete(user)
            sess.commit()
            return {"ok":"true"}
        else:
            return {"ok":"false"}