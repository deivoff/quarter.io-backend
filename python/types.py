from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType 
from graphene_mongo import MongoengineObjectType
from .models import *

# Put there schemas of db tables on GQL type

class UsersType(SQLAlchemyObjectType):
    class Meta:
        model = Users
        interfaces = (relay.Node, )

class UserProfilesType(SQLAlchemyObjectType):
    class Meta:
        model = UserProfiles
        interfaces = (relay.Node, )

class SensorBaseType(SQLAlchemyObjectType):
    class Meta:
        model = SensorBase
        interfaces = (relay.Node, )

class SensorType(MongoengineObjectType):
    class Meta:
        model = Sensor
        interfaces = (relay.Node, )

