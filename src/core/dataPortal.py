from dbConnection import DbManager
class DataPortal:
    def __init__(self):
        self.id = None
        self.id_name = None
        self.name = None
        self.title = None
        self.url = None
        self.author = None
        self.publisher = None
        self.issued = None
        self.publisher_classification = None
        self.description = None
        self.tags = []
        self.license_id = None
        self.license_url = None
        self.place = None
        self.location = None
        self.country = None
        self.language = None
        self.status = None
        self.metadatacreated = None
        self.generator = None
        self.api_endpoint = None
        self.api_type = None
        self.full_metadata_download = None
        self.description_html = None
        self.groups = []
        self.dc_status = None
        self.user_created = None
        self.Insert_Date = None
        self.user_updated = None
        self.Updated_Date = None

    def setDataPortal(self):
        self.id = id
        self.id_name = id_name
        self.name = name
        self.title = title
        self.url = url
        self.author = author
        self.publisher = publisher
        self.issued = issued
        self.publisher_classification = publisher_classification
        self.description = description
        self.tags = tags
        self.license_id = license_id
        self.license_url = license_url
        self.place = place
        self.location = location
        self.country = country
        self.language = language
        self.status = status
        self.metadatacreated = metadatacreated
        self.generator = generator
        self.api_endpoint = api_endpoint
        self.api_type = api_type
        self.full_metadata_download = full_metadata_download
        self.description_html = description_html
        self.groups = groups
        self.dc_status = dc_status
        self.user_created = user_created
        self.Insert_Date = Insert_Date
        self.user_updated = user_updated
        self.Updated_Date = Updated_Date

    def createDataPortal(self, id_name, name, title, url, author, publisher, issued,
                         publisher_classification, description, tags, license_id, license_url,
                         place, location, country, language, status, metadatacreated,
                         generator, api_endpoint, api_type, full_metadata_download,
                         description_html, groups, dc_status, user_created, Insert_Date,
                         user_updated, Updated_Date):
        dbconn = DbManager()


        sql = "Insert Into DataPortal (id_name  ,name ,title ,url ,author ,publisher ," \
              "issued ,publisher_classification ,description ,tags  ,license_id ,license_url   ,place ,location," \
              "country ,language,status ,metadatacreated ,generator ,api_endpoint ,api_type ,full_metadata_download," \
              "description_html ,groups ,dc_status ,user_created ,user_updated ,Insert_Date  ,Updated_Date) VALUES " \
              "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)"

        '''
        sql = "Insert Into DataPortal (id_name  ,name ,title ,url ,author ,publisher ," \
              "issued ,publisher_classification ,description ,tags  ,license_id ,license_url   ,place ,location," \
              "country ,language,status ,metadatacreated ,generator ,api_endpoint ,api_type ,full_metadata_download," \
              "description_html ,groups ,dc_status ,user_created ,Insert_Date ,user_updated ,Updated_Date) VALUES " \
              "(%(id_name)s,%(name)s,%(title)s,%(url)s,%(author)s,%(publisher)s,%(issued)s,%(publisher_classification)s,%(description)s,[],%(license_id)s, %(license_url)s, %(place)s, %(location)s, %(country)s, [], %(status)s, %(metadatacreated)s, %(generator)s, %(api_endpoint)s, %(api_type)s, %(full_metadata_download)s, %(description_html)s, [], %(dc_status)s, %(user_created)s, CURRENT_TIMESTAMP, %(user_updated)s, CURRENT_TIMESTAMP)"
        
        '''

        data = (id_name, name, title, url, author, publisher, issued,publisher_classification, description, tags,
                license_id, license_url,place, location, country, language, status, metadatacreated,generator,
                api_endpoint, api_type, full_metadata_download,description_html, groups, dc_status, user_created,
                user_updated)


        #print data
        dbconn.insExec(sql,data)




    def getDataPortalId(self, name):
        return self.id
