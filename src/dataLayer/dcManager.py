from dbConnection import DbManager

class DcManager:
    def __init__(self):
        self.version = 1
        self.dbConn = DbManager()

    def getSource(self, parm):
        result = {}
        sql = """ select * from adapter_type """
        result = self.dbConn.insExec(sql)


    def createSource(self):
        result = {}

        sql = """ select * from adapter_type """
        sql = """ Insert into adapter_type (id  ,type , name  ) VALUES(4, 'api','gc')"""
        result  = self.dbConn.insExec(sql)
        print result


if __name__ == '__main__':
    dbconn = DcManager()
    dbconn.createSource()
