import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL

import settings

# from finalproject import UPLOADS_FOLDER
UPLOAD_FOLDER = "/static/images"
 
Base = declarative_base()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
# db = SQLAlchemy(app)


def create_db(app):
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    print ("in create_db: Database URL {}".format(URL(**settings.DATABASE)))
    engine = create_engine(URL(**settings.DATABASE))
    #create database session
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @staticmethod
    def make_unique_nickname(nickname, session):
        if session.query(User).filter_by(name=nickname).first() is None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if session.query(User).filter_by(name=new_nickname).first() is None:
                break
            version += 1
        return new_nickname

    @staticmethod
    def create(login_session, session):
        newUser = User(name = login_session['username'], email = login_session['email'], picture = login_session['picture'])
        session.add(newUser)
        session.commit()
        user = session.query(User).filter_by(email = login_session['email']).first()
        return user.id

    @staticmethod
    def find_id_by_email(email, session):
        try:
            user = session.query(User).filter_by(email = email).first()
            return user.id
        except:
            return None

    def __init__(self, name, email, picture):
        self.name = name
        self.email = email
        self.picture = picture

    def __repr__(self):
        return '<User %r>' % self.name



class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'user_id'   : self.user_id
       }
 
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return '<Category %r>' % self.name

class MenuItem(Base):
    __tablename__ = 'menu_item'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    imagefile = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price
       }

    def imageURL(self):
      return UPLOAD_FOLDER + "/" + self.imagefile

    def categoryName(self):
        if self.category:
            return self.category.name
        else:
            return "None"

    def __init__(self, name, description, price, category, imagefile, user_id):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.imagefile = imagefile
        self.user_id = user_id

    # def __init__(self, name, description, price, course, category_id, imagefile, user_id):
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.course = course
    #     self.category_id = category_id
    #     self.imagefile = imagefile
    #     self.user_id = user_id

    def __repr__(self):
        return '<MenuItem %r>' % self.name
        

if __name__ == '__main__':
    app = create_app()
    Session = create_db(app)
    # db.create_all()
    # db.session.commit()
    print("created tables")

