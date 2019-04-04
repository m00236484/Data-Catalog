import urllib
import json
import requests
import wget
import boto3
import os
import sys
from businessLayer.dataSetBL import DataSetBl

class FdaAdapter():
    def __init__(self):
        self.id = None

    def getDsRequest(self):
        url = "https://api.fda.gov/download.json"
        response = urllib.urlopen(url)
        return response


    def processResponse(self, response):
        data = json.loads(response.read())
        results = data['results']
        # Get the service client
        s3 = boto3.client('s3')
        sDir = ''
        #ds_src_id ,ds_type ,name ,   url  ,adpter_type_id  , store  , refesh_frq   ,insert_date ,  last_update

        ds_src_id = 1
        ds_type = 1
        name = ""

        # dataset name should be generated from code below

        dsUrl = "'some Url'" #where dataset live ,
        adpter_type_id = 1 #,
        store = ""
        refesh_frq = 1

        for category  in data['results'].keys():
            # by category name get source
            dataSets = data['results'][category]
            for ds in dataSets.keys():
                dataset = dataSets[ds]

                # Dataset insert ot update last update
                dss = DataSetBl()
                name = "fda/"  + str(category) + "/" + str(ds)
                store = "fda/"  + str(category) + "/" + str(ds)
                print "\n Dataset name :" + name + ", Datasource:" + category +"\n  Downloading from:\n" + url
                dss.setDataSet(ds_src_id ,ds_type ,str(name) ,dsUrl,adpter_type_id ,store  ,refesh_frq)
                for i in  dataset['partitions']:
                    url =  i['file']
                    #print "Download File :" + url
                    #r = requests.get(url, "~/tmp")
                    filename = wget.download(url)
                    sDir= str("fda/"+ str(category) + "/" +str(ds) +"/"+str(filename))
                    #print sDir
                    s3.upload_file(filename, "datainsight-dc", sDir)
                    os.remove(filename)
                    #print(r.text)
if __name__ == '__main__':
    fdAd = FdaAdapter()
    fdAd.processResponse(fdAd.getDsRequest())

