#this class represent the dataset dataobject


class DataSetTag(self):
    def __init__(self):
        self.id = None
        self.tag = None
        self.tageUpdated = None



    def setDsTag(self, id, tag,upDate):
        self.id = id
        self.tag = tag
        self.tageUpdated = upDate

class DataSet(self):
    def __init__(self):
        self.id = None
        self.name= None
        self.url = None
        self.desc = None
        self.license = None
        self.owner = None
        self.resource = None
        self.format = None
        self.locationTypoe = None
        self.location = {}

    def generateID(self):
         return self.idd

    def setDataSet(self,dsName, dsUrl, dsDesc,licese, owner,resource, format, locationType, location):
         self.name = dsName
         self.desc= dsDesc
         self.url = dsUrl
         self.license = licese
         self.owner = owner
         self.resource = resource
         self.format = format
         self.locationTypoe = locationType
         self.location = location


