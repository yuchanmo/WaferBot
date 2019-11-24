from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,DateTime, ForeignKey, create_engine) 
metadata = MetaData()
cookies = Table('cookies', metadata,    
                Column('cookie_id', Integer(), primary_key=True),    
                Column('cookie_name', String(50), index=True),    
                Column('cookie_recipe_url', String(255)),    
                Column('cookie_sku', String(55)),    
                Column('quantity', Integer()),    
                Column('unit_cost', Numeric(12, 2)) )
users = Table('users', metadata,    
              Column('user_id', Integer(), primary_key=True),    
              Column('customer_number', Integer(), autoincrement=True),    
              Column('username', String(15), nullable=False, unique=True),    
              Column('email_address', String(255), nullable=False),    
              Column('phone', String(20), nullable=False),    
              Column('password', String(25), nullable=False),    
              Column('created_on', DateTime(), default=datetime.now),    
              Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now) )
orders = Table('orders', metadata,    
               Column('order_id', Integer(), primary_key=True),    
               Column('user_id', ForeignKey('users.user_id')) )
line_items = Table('line_items', metadata,    
                   Column('line_items_id', Integer(), primary_key=True),    
                   Column('order_id', ForeignKey('orders.order_id')),    
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),    
                   Column('quantity', Integer()),    
                   Column('extended_cost', Numeric(12, 2)) )
engine = create_engine('sqlite:///:memory:') 
metadata.create_all(engine)

ins = cookies.insert().values(    
    cookie_name="chocolate chip",    
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",    
    cookie_sku="CC01",    
    quantity="12",    
    unit_cost="0.50" ) 
print(str(ins)) 

ins.compile().params

connection = engine.connect()
res = connection.execute(ins)

ins = cookies.insert()

res.inserted_primary_key 

l = [
    {'cookie_name': 'chocolate chip', 'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html', 'cookie_sku': 'CC01', 'quantity': '12', 'unit_cost': '0.50'},
    {'cookie_name': 'cho chip', 'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html', 'cookie_sku': 'CC01', 'quantity': '12', 'unit_cost': '0.50'},
    {'cookie_name': 'late chip', 'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html', 'cookie_sku': 'CC01', 'quantity': '12', 'unit_cost': '0.50'},

    ]

rrr = connection.execute(ins,l)
rrr.inserted_primary_key


from sqlalchemy.sql import select
s = select([cookies])
rc = connection.execute(s)
results = rc.fetchall()

path = '../WaferMapBotModel/requirements.txt'
f = open(path,'r')
f.readlines()