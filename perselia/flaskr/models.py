from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine, TIMESTAMP
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker()
Session.configure(bind=engine)

sess = Session()

class Data():
    created = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

class User(Base, Data):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    avatar_url = Column(String)
    password = Column(String)
    master = Column(Integer)

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
    

def initialize_database():
    Base.metadata.create_all(engine)