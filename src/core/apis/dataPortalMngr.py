import urllib2
import json
import datetime
from core.dataLayer.dataPortal import DataPortal
#from core.businessLayer.dataSetBL import DataSetBl

class DataPortalMng():
    def __init__(self):
        self.id = None

    def getDsRequest(self):
        url = "https://api.fda.gov/download.json"
        response = urllib2.urlopen(url)
        return response

    def apiRequest(self, url):
        # url = "https://api.fda.gov/download.json"
        response = urllib2.urlopen(url)
        return response

    def validateDataPortal(self , url):
        try:
            response = urllib2.urlopen(url ,timeout = 10)
            code = response.getcode()
        except urllib2.HTTPError, e:
            code =  e.code
        except urllib2.URLError, e:
            code = 999
        except:
            code = 1000
        return code


    def discoverDataPortal(self):
        url = "http://datacatalogs.org/api/data.json"
        response =  self.apiRequest(url)
        self.processResponse(response)
        #print response

    def processResponse(self, response):
        data = json.loads(response.read())
        if len(data) < 1 : return
        for dp in data.keys():
            id = data[dp]['id']
            id_name = dp
            name = data[dp]['name']
            title = data[dp]['title']
            url = data[dp]['url']
            author = data[dp]['author']
            publisher = data[dp]['publisher']
            issued = data[dp]['issued']
            publisher_classification = data[dp]['publisher_classification']
            description = data[dp]['description']
            tags = data[dp]['tags']
            license_id = data[dp]['license_id']
            license_url = data[dp]['license_url']
            place = data[dp]['place']
            location = data[dp]['location']
            country = data[dp]['country']
            language = data[dp]['language']
            status = data[dp]['status']
            metadatacreated = data[dp]['metadatacreated']
            generator = data[dp]['generator']
            api_endpoint = data[dp]['api_endpoint']
            api_type = data[dp]['api_type']
            full_metadata_download = data[dp]['full_metadata_download']
            description_html = data[dp]['description_html']
            groups = data[dp]['groups']
            dc_status = self.validateDataPortal(url)
            user_created = 1
            ts = datetime.datetime.now()
            Insert_Date =ts
            user_updated = 1
            Updated_Date = ts

            portal = DataPortal()
            portal.createDataPortal(id_name, name     , title , url , author , publisher , issued ,
                publisher_classification , description , tags  , license_id , license_url   ,
                place , location , country , language  , status , metadatacreated ,
                generator , api_endpoint , api_type , full_metadata_download ,
                description_html , groups , dc_status , user_created , 	 Insert_Date ,
                user_updated ,  Updated_Date)


if __name__ == '__main__':
    fdAd =  DataPortalMng()
    fdAd.discoverDataPortal()
