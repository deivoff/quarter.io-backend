from .mysql_connect import base
from mongoengine import Document
from mongoengine.fields import FloatField, StringField, ListField, URLField, ObjectIdField
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship

class Users(base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True, autoincrement = True)
    login = Column(String)
    password = Column(String)
    userprofiles_id = Column(Integer, ForeignKey('UserProfiles.id_profile'))
    _permitions = Column(Integer)
    userprofiles = relationship(
        UserProfiles,
        backref=backref('users', 
            uselist=True,
            cascade='delete,all'))

class UserProfiles(base):
    __tablename__ = 'user_profiles'
    id_profile = Column(Integer, primary_key=True, autoincrement = True)
    e_mail = Column(String)
    first_name = Column(String)
    surname = Column(String)
    address = Column(String)
    telephone = Column(String)
    image = Column(String)
    _createdAt = Column(DateTime, default=func.now())
    _updatedAt = Column(DateTime, default=func.now())


class SensorBase(base):
    __tablename__= 'SensorConnection'
    id_sensor = Column(Integer, primary_key=True, autoincrement = True)
    mac = Column(String)
    dtype = Column(Integer)
    mongo_key = Column(String)

class Sensor(Document):
    meta = {"collection": "sensor"}
    ID = ObjectIdField()
    mac = StringField()
    data = ListField()