
from core.dataLayer.dataSetDM import DataSet


class DataSetBl:
    def __init__(self, id = None):
        self.id = id



    def setDataSet(self ,  ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq):
        ds = DataSet()
        ds.isDataSet(ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq)

    def getDataSet(self):
        datasets = {}
        ds = DataSet()
        datasets = ds.getAll()
        print datasets




if __name__ == '__main__':
    db = DataSetBl()
    db.getDataSet()


