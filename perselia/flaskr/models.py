from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine, TIMESTAMP
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.functions import generate_token, encrypt


Base = declarative_base()

engine = create_engine('sqlite:///database.sqlite', connect_args={'check_same_thread':False})
Session = sessionmaker()
Session.configure(bind=engine)

sess = Session()

class Data():
    created = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    token = Column(String)

class User(Base, Data):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    avatar_url = Column(String)
    password = Column(String)
    master = Column(Integer)
    customfields = relationship("CustomField", cascade="all,delete", backref="User")

class CustomField(Base, Data):
    __tablename__ = 'customfields'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    key = Column(String)
    value = Column(String)

class Token(Base, Data):
    __tablename__ = 'tokens'
    value = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))

class Option(Base, Data):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    value = Column(String)

class Post(Base, Data):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)


def create_admin():
    user = User\
    (
        firstname='Richard',
        lastname='Stallman',
        email='admin@admin.com',
        avatar_url='https://stallman.org/Portrait_-_Denmark_DTU_2007-3-31.jpg',
        password=encrypt('admin'),
        master=1,
        token=generate_token()
    )

    old_user = sess.query(User).filter(User.email==user.email).first()

    if old_user is not None:
        return False

    sess.add(user)
    sess.commit()

    return True

def initialize_database():
    Base.metadata.create_all(engine)

