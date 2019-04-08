
from core.dbConnection import DbManager

class DataSet:
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
        self.dbconn = DbManager()

    def generateID(self):
         return self.idd

    def checkDataSet(self, id=None , name = None):
        datasets = {}
        if id:
            sql = "select * from dataset where id = " + id
        elif not id  and name :
            sql = "select * from dataset where name = '" + name + "'"
        else:
            return 0

        datasets = self.dbconn.sqlExec(sql)
        return  len(datasets)

    def createDataSet(self, ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq ):
        '''
        #sql = "insert into dataset( ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq  ,insert_date , last_update ) values ("+ str(ds_src_id) +"," + str(ds_type) +"," \
        #"" + str(name)  +"," + str(url) +"," +  str(adpter_type_id) + ", " + str(store)  + ", "+ str(refesh_frq) + ",CURRENT_TIMESTAMP,CURRENT_TIMESTAMP  ) ;"

        :param ds_src_id:
        :param ds_type:
        :param name:
        :param url:
        :param adpter_type_id:
        :param store:
        :param refesh_frq:
        :return:
        '''


        sql = "insert into dataset_old( ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq  ,insert_date , last_update ) values (%s,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)"

        data = (ds_src_id, ds_type , name, url,adpter_type_id, store, refesh_frq   )

        datasets = self.dbconn.insExec(sql , data)



    def updateDataSet(self , ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq):
        sql = "update dataset  set last_update = CURRENT_TIMESTAMP ;"
        datasets = self.dbconn.sqlExec(sql)

    def isDataSet(self, ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq ):
        if self.checkDataSet() < 1 and (name != None and name != ''):
            self.createDataSet(ds_src_id ,ds_type ,name ,url,adpter_type_id ,store  ,refesh_frq )
        else:
            self.updateDataSet(ds_src_id, ds_type, name, url, adpter_type_id, store, refesh_frq)



    def getAll(self):
        datasets = {}

        datasets = self.dbconn.sqlExec("select * from dataset")
        return datasets


    #get data sets by src id
    #def getDataSet(self,ds_src_id, id , dsName):


    def setDataSet(self,ds_src_id , ds_type , dsName, dsUrl, dsDesc,adpter_type_id,store,licese, owner,resource, format, locationType, location):
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


class DataSetTag:
    def __init__(self):
        self.id = None
        self.tag = None
        self.tageUpdated = None

    def setDsTag(self, id, tag,upDate):
        self.id = id
        self.tag = tag
        self.tageUpdated = upDate

class DsResources:
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