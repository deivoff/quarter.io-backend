connect = str('mysql+pymysql://root:@localhost/qarterdb?host=localhost?port=3306')

import sqlalchemy as sa
from sqlalchemy import create_engine
 
engine = create_engine(connect)

def table_exists(name):
    ret = engine.dialect.has_table(engine, name)
#    print('Table "{}" exists: {}'.format(name,ret))
    return ret

def db_is_empty():
    table_names = sa.inspect(engine).get_table_names()
    is_empty = table_names == []
#    print('db is empty:{}'.format(is_empty))
    return is_empty

if (db_is_empty()):
    engine.execute('create table users ('
                   'id integer(11) not null,'
                   'login varchar(30),'
                   'password varchar(20),'
                   'primary key (id));')     


result = engine.execute('select * from users')
for _r in result:
    print(_r)

