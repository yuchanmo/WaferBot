import pyodbc as mssql
import numpy as np
import pandas as pd
import psycopg2 as pg

import petl as etl

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};Server=localhost;Database=master;'
con = mssql.connect(connection_string)