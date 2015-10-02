from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker()
Session.configure(bind=engine)

sess = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    avatar_url = Column(String)
    password = Column(String)
    admin = Column(Integer, default=0)

class Option(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    value = Column(String)

def initialize_database():
    Base.metadata.create_all(engine)