# Необходимо создать установщик с вводом параметров подключения
# username = str('root')
# password = str(' ')
# host = str('localhost')
# dbname = str('qarterdb')
# connect = str('mysql+pymysql://'+username+':'+password+
# '@'+host+'/'+dbname)

from sqlalchemy.orm import(scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType 
from sqlalchemy import *
import graphene

class mysql_connect():
    connect = ''
    db = ''

    engine = create_engine(connect, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    base = declarative_base()
    base.query = db_session.query_property()
