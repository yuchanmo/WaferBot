
class ConnectionStringBuilder():
    def __init__(self,host,database,username,password,port,dbtype='gpdb'):
        self.host = host
        self.database = database
        self.username = username
        self.password = password        
        self.dbtype = dbtype
        if port == None:
            if dbtype =='gpdb':
                self.port = 5432
            elif dbtype =='mssql':
                self.port = 1433
            else:
                self.port = 9999

    def get_connectionstring(self):
        if self.dbtype == 'gpdb':
            return "dbname={} user={} password={} host={} port={}".format(self.database,self.username,self.password,self.host,self.port)
        elif self.dbtype =='mssql':
            return 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.host+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password





#MSSQL CONFIG
server = 'localhost' 
database = 'BikeStores' 
username = 'sa' 
password = '1' 

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


