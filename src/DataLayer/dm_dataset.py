import psycopg2
from psycopg2.extras import RealDictCursor
from dbConnection import DbManager

class DataSet(self):
    def __init__(self):
        self.id = None
        self.ds_src_id = None
        self.ds_type = None
        self.name= None
        self.desc = None
        self.url = None
        self.adpter_type_id = None
        self.store = None
        self.refresh_frq = None
        self.license = None
        #self.owner = None
        #self.resource = {}
        self.format = None
        #self.locationTypoe = None
        #self.location = {}
        self.insert_date = None
        self.last_update = None

    def generateID(self):
         return self.idd


    def getAll(self):
        datasets = {}
        dbconn = DbManager()
        datasets = dbconn.sqlExec("select * from dataset")
        return datasets


    #get data sets by src id
    def getDataSet(self,ds_src_id, id , dsName):


    def setDataSet(self,ds_src_id , ds_type ,ds_type ,   dsName, dsUrl, dsDesc,adpter_type_id,store,licese, owner,resource, format, locationType, location):
        self.ds_src_id = ds_src_id
        self.ds_type = ds_type
        self.name = dsName
        self.desc= dsDesc
        self.url = dsUrl
        self.adpter_type_id =adpter_type_id
        self.store = store
        self.license = licese
        self.owner = owner
        self.resource = resource
        self.format = format
        self.locationTypoe = locationType
        self.location = location


class DataSetTag(self):
    def __init__(self):
        self.id = None
        self.tag = None
        self.tageUpdated = None

    def setDsTag(self, id, tag,upDate):
        self.id = id
        self.tag = tag
        self.tageUpdated = upDate

class DsResources(self):
    def __init__(self):
        self.id = None
        self.ds_id = None
        self.ds_type = None
        self.url = None
        self.insert_date=None
        self.last_update= None

    def setDsResources(self,ds_id,ds_type,url,insert_date,update_date):
        self.ds_id = ds_id
        self.ds_type = ds_type
        self.url = url
        self.insert_date=insert_date
        self.last_update=update_date