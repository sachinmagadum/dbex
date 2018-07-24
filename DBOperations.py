from ReadWriteFile import FileOperations
from ReadWriteExcel import ExcelOperations
import pymysql
import time

class DbOperations:

    # Create Connection with database
    def getConnection(self):
        conn = pymysql.connect(port=3306, host='localhost', user='root', passwd='admin123', db='pythondb')
        print('\n Inside getconnection ',conn)
        return conn

    # Create Table if allready created first delete then create
    def createDataBaseTable(self):
        connection = self.getConnection()
        cur = connection.cursor()
        cur.execute('create table user_credentails (id INT AUTO_INCREMENT PRIMARY KEY,username varchar(100),password varchar(100),expectedmsg varchar(100))')
        connection.commit()  # Data save on to database
        print('\n\nUser_Credentials Table created successfully...with ID/UserName/Password/ExpMsg')
        time.sleep(2)

    # Insert data onto database
    def insertIntoDatabase(self,list):
        self.createDataBaseTable() # first time required to call this
        connection = self.getConnection()
        cur = connection.cursor()
        cnt = 0
        print('No of Cells --',list.__len__()) # Number of total cells
        noOfRecords = list.__len__()/3;  # Number of rows
        for sno in range(1,int(noOfRecords+1)):
            print(cnt)
            sql_query = 'insert into user_credentails values('+str(sno)+',\''+list[cnt]+'\''+',\''+list[cnt+1]+'\','+'\''+list[cnt+2]+'\')'
            print('\n'+sql_query)
            cnt+=3
            cur.execute(sql_query)
            connection.commit()
            time.sleep(2)
        print('\n\n All Records inserted into DB')

    # Query for delete table from database
    def dropTable(self):
        connection = self.getConnection()
        cur = connection.cursor()
        cur.execute('drop table user_credentails')
        connection.commit()
        print('\n Table deleted Successfully....!')

    # Read data from database
    def getAllRecordsFromDbIntoList(self):
        listOfRecordsFrmDb = []
        connection = self.getConnection()
        cur = connection.cursor()
        cur.execute('select * from user_credentails')
        rows=cur.fetchall()
        for items in rows:  #-- Item is tuble and rows are tuble of tuple
            print(items)
            listOfRecordsFrmDb.append(items) #-- Convert tuble into list
        print(listOfRecordsFrmDb)
        return listOfRecordsFrmDb




if __name__ == '__main__':
    f = FileOperations()
    ex = ExcelOperations()
    db = DbOperations()
    f.readfromfile()  # --Read Data from text File
    ex.writeexcel()   # --Write Data to Excel File
    list1 = ex.readexcel(1) # --Read Data from Excel
    # -- Data Base Operations --
    db.dropTable() # -- Delete Table
    db.insertIntoDatabase(list1) # -- Create Conn -- Create Table -- Insert into table
    dbToFileList = db.getAllRecordsFromDbIntoList()  #-- Read all Data from table (Database)
    f.writeDataIntoFile(dbToFileList)  # -- Write data into again Text File
    # dbOb.dropTable()