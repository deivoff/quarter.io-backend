from graphene_sqlalchemy import SQLAlchemyConnectionField
from .types import *

class UsersConnection(relay.Connection):
    class Meta:
        node = UsersType

class UserProfilesConnection(relay.Connection):
    class Meta:
        node = UserProfilesType

class SensorBaseConnection(relay.Connection):
    class Meta:
        node = SensorBaseType