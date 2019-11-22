import pyodbc as mssql
import numpy as np
import pandas as pd
import psycopg2 as pg
import json
import petl as etl
server = 'localhost' 
database = 'WaferBot' 
username = 'asd' 
password = '1' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

df = pd.DataFrame(columns=['list','dict'])

for i in range(5):
    a = np.array([k for k in range(i+10)]).tobytes()
    b = json.dumps({'ab':[1,2,3],'cd':[4,5,6]})
    df.loc[i] = (a,b)


    df