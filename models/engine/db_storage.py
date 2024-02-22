#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                               expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        from models import base_model
        objs = {}
        if cls:
            query = self.__session.query(cls).all()
        else:
            classes = [base_model.Base.__subclasses__()]
            query = []
            for c in classes:
                query += self.__session.query(c).all()
        for obj in query:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objs[key] = obj
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                               expire_on_commit=False))
        self.__session = Session()
