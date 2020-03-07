from mysql_connect import *
from graphs import *


def table_exists(name):
    ret = engine.dialect.has_table(engine, name)
#    print('Table "{}" exists: {}'.format(name,ret))
    return ret

def db_is_empty():
    table_names = inspect(engine).get_table_names()
    is_empty = table_names == []
#    print('db is empty:{}'.format(is_empty))
    return is_empty

def create_table_users():
    engine.execute('create table users ('
                    'id_user integer(11) not null auto_increment,'
                    'login varchar(20),'
                    'password varchar(20),'
                    'user_profile integer(11) not null,'
                    'primary key (id_user));')

def create_table_user_profiles():
    engine.execute('create table user_profiles ('
                    'id_profile integer(11) not null auto_increment,'
                    'e_mail varchar(50),'
                    'first_name varchar(30),'
                    'surname varchar(30),'
                    'address varchar(100),'
                    'telephone varchar(30),'
                    'image varchar(30),'
                    '_createdAt datetime,'
                    '_updateAt datetime,'
                    'primary key (id_profile));')

def create_table_sensors():
    engine.execute('create table sensors ('
                    'id_sensor integer(11),'
                    'mac varchar(30),'
                    'dtype integer(11),'
                    'mongo_key varchar(30);')

if __name__ == "__main__":
    # Автозаполнитель БД, переместить в установщик, когда будет готов
    if (db_is_empty()):
        engine.execute()     

    