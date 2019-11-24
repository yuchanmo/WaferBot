import pyodbc 
import numpy as np
import pandas as pd
import psycopg2 as pg
import json
import petl as etl
server = 'localhost' 
database = 'BikeStores' 
username = 'sa' 
password = '1' 
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
mkcursor = lambda: connection.cursor()
table = etl.fromdb(mkcursor,'select * from production.brands')
table
cursor = cnxn.cursor()

categories = [['yuchan','raum','hyejin']]

table = etl.fromcolumns(categories)
table = etl.rename(table,'f0','category_name')
res = etl.appenddb(table,connection,'categories','production')
res

#df = pd.DataFrame(columns=['id','list','dict'])

#for i in range(5):
#    id = i
#    a = np.array([k for k in range(i+10)]).tobytes()
#    b = json.dumps({'ab':[1,2,3],'cd':[4,5,6]})
#    df.loc[i] = (i,a,b)


#from sqlalchemy import create_engine
#df
##https://stackoverflow.com/questions/15750711/connecting-to-sql-server-2012-using-sqlalchemy-and-pyodbc/36747352
## create sqlalchemy engine
#engine= create_engine("mssql+pyodbc://sa:1@localhost:1433/WaferBot?driver=SQL+Server+Native+Client+11.0")
#df.to_sql('test_table',con = engine, if_exists = 'append', chunksize = 1000)
#df[1:]

