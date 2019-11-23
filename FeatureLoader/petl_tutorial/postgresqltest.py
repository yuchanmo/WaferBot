#https://petl.readthedocs.io/en/stable/io.html

import petl as etl
import psycopg2
import pandas as pd
import numpy as np
from datetime import datetime
dn = 'defect'
du ='postgres'
dp = 1
dh = 'localhost'
dbp = 5432

cs = "dbname=%s user=%s password=%s host=%s port=%s" % (dn,du,dp,dh,dbp)
connection = psycopg2.connect(cs)


#
a = np.random.rand(100000,200).tolist()
b = np.random.rand(100000,10).tolist()
etl.fromcolumns()



#pandas -> table -> db
import pandas as pd
df = pd.DataFrame(columns=['id','features','model_id','regdate'])
for i in range(1,10000):
    df.loc[i] = [i,np.random.rand(10).tolist(),'test1',datetime.now()]


pddf = etl.fromdataframe(df)
etl.todb(pddf,connection,'defect_features','public')

#select query
mkcursor = lambda: connection.cursor(name='arbitrary')
table = etl.fromdb(mkcursor,'select * from public.defect_features')
table

#primitive -> db
import numpy as np
from datetime import datetime
datatable = [['id','features','model_id','regdate']]
for i in range(1,10):
    datatable.append([i,np.random.rand(10).tolist(),'test1',datetime.now()])
etl.todb(datatable,connection,'defect_features','public')
