

# Put there schemas of db tables on GQL type

class Users(base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True, autoincrement = True)
    login = Column(String)
    password = Column(String)
    user_profile = Column(Integer)

class UsersType(SQLAlchemyObjectType):
    class Meta:
        model = Users
        interfaces = (relay.Node, )

class UsersConnection(relay.Connection):
    class Meta:
        node = UsersType

class UserProfiles(base):
    __tablename__ = 'user_profiles'
    id_profile = Column(Integer, primary_key=True, autoincrement = True)
    e_mail = Column(String)
    first_name = Column(String)
    surname = Column(String)
    address = Column(String)
    _createdAt = Column(DateTime)
    _updatedAt = Column(DateTime)

class UserProfilesType(SQLAlchemyObjectType):
    class Meta:
        model = UserProfiles
        interfaces = (relay.Node, )

class UserProfilesConnection(relay.Connection):
    class Meta:
        node = UserProfilesType

class Sensors(base):
    __tablename__= 'sensors'
    id_sensor = Column(Integer, primary_key=True, autoincrement = True)
    mac = Column(String)
    dtype = Column(Integer)

class SensorsType(SQLAlchemyObjectType):
    class Meta:
        model = Sensors
        interfaces = (relay.Node, )

class SensorsConnection(relay.Connection):
    class Meta:
        node = SensorsType

