from  DataLayer import DataSet

class DataSetBl:
    def __init__(self, id = None):
        self.id = id


    def getDataSet(self):
        datasets = {}
        ds = DataSet()
        datasets = ds.getAll()
        print datasets


if __name__ == '__main__':
    dbconn = DataSetBl()
    dbconn.getDataSet()

