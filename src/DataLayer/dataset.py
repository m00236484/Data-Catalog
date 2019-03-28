#this class represent the dataset dataobject


class DataSetTag(self):
    def __init__(self):
        self.dsId = None
        self.dsTag = None
        self.dsTageUpdated = None
    def setDsTag(self, id, tag,upDate):
        self.dsId = id
        self.dsTag = tag
        self.dsTageUpdated = upDate

class DataSet(self):
    def __init__(self):
        self.dsId = None
        self.dsName= None
        self.dsUrl = None
        self.dsDesc = None
        self.license = None
        self.owner = None
        self.resource = None
        self.format = None
        self.locationTypoe = None
        self.location = {}

    def generateID(self):
         return self.dsId

    def setDataSet(self,dsName, dsUrl, dsDesc,licese, owner,resource, format, locationType, location):
         self.dsName = dsName
         self.dsDesc= dsDesc
         self.dsUrl = dsUrl
         self.license = licese
         self.owner = owner
         self.resource = resource
         self.format = format
         self.locationTypoe = locationType
         self.location = location


