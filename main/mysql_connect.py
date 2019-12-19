connect = str('mysql+pymysql://root:@localhost/qarterdb?host=localhost?port=3306')
# Необходимо создать установщик с вводом параметров подключения
# username = str('root')
# password = str(' ')
# host = str('localhost')
# dbname = str('qarterdb')
# connect = str('mysql+pymysql://'+username+':'+password+
# '@'+host+'/'+dbname)

from sqlalchemy import *
from sqlalchemy.orm import(scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType 

engine = create_engine(connect, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def table_exists(name):
    ret = engine.dialect.has_table(engine, name)
#    print('Table "{}" exists: {}'.format(name,ret))
    return ret

def db_is_empty():
    table_names = inspect(engine).get_table_names()
    is_empty = table_names == []
#    print('db is empty:{}'.format(is_empty))
    return is_empty

# Автозаполнитель БД, переместить в установщик, когда будет готов
if (db_is_empty()):
    engine.execute('create table users ('
                   'id_user integer(11) not null,'
                   'login varchar(30),'
                   'password varchar(20),'
                   'primary key (id));')     


#result = engine.execute('select * from users')
#for _r in result:
#    print(_r)

base = declarative_base()
base.query = db_session.query_property()

class Users(base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)

class UsersSchema(SQLAlchemyObjectType):
    class Meta:
        model = Users
        interfaces = (relay.Node, )

class UsersConnection(relay.Connection):
    class Meta:
        node = UsersSchema

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UsersConnection)

schema = graphene.Schema(query=Query)

