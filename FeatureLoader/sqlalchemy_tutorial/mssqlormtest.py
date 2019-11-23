


#from sqlalchemy import create_engine
#df
##https://stackoverflow.com/questions/15750711/connecting-to-sql-server-2012-using-sqlalchemy-and-pyodbc/36747352
## create sqlalchemy engine
#engine= create_engine("mssql+pyodbc://sa:1@localhost:1433/WaferBot?driver=SQL+Server+Native+Client+11.0")
#df.to_sql('test_table',con = engine, if_exists = 'append', chunksize = 1000)
#df[1:]
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.sql import *
import pyodbc

engine = create_engine("mssql+pyodbc://sa:1@localhost:1433/BikeStores?driver=SQL+Server+Native+Client+11.0")
Base = declarative_base()



class Categories(Base):
    __tablename__='categories'
    __table_args__ = {"schema": "production"}
    category_id = Column(Integer,primary_key=True)
    category_name = Column(String)

class Products(Base):
    __tablename__='products'
    __table_args__ = {"schema": "production"}
    product_id = Column(Integer,primary_key=True)
    product_name = Column(String)
    brand_id = Column(Integer,ForeignKey('brands.brand_id'))
    category_id = Column(Integer,ForeignKey('categories.category_id'))
    model_year = Column(SmallInteger)
    list_price = Column(DECIMAL)
    category = relationship('Categories',backref=backref('products',order_by=category_id))
    brand = relationship('Brands',backref=backref('products',order_by=brand_id))


class Brands(Base):
    __tablename__ = 'brands'
    __table_args__ = {"schema": "production"}
    brand_id = Column(Integer,primary_key = True)
    brand_name = Column(String)


Categories.__table__.create(bind=engine,checkfirst=True)
Brands.__table__.create(bind=engine,checkfirst=True)
Products.__table__.create(bind=engine,checkfirst=True)

Base.metadata.create_all(engine)

connection = engine.connect()
query = select([Categories.category_id])
result = connection.execute(query)
list(result)
Session = sessionmaker(bind=engine)
session = Session()

new_category = Categories(category_name='testste')
session.add(new_category)
session.commit()