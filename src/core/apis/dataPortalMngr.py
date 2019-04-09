import urllib
import json
import requests
import wget
import boto3
import os
import sys
from core.businessLayer.dataSetBL import DataSetBl

class DataPortalMng():
    def __init__(self):
        self.id = None

    def getDsRequest(self):
        url = "https://api.fda.gov/download.json"
        response = urllib.urlopen(url)
        return response

    def apiRequest(self, url):
        # url = "https://api.fda.gov/download.json"
        response = urllib.urlopen(url)
        return response

    def validateDataPortal(self , url):
        response = urllib.urlopen(url)
        return response


    def discoverDataPortal(self):
        url = "http://datacatalogs.org/api/data.json"
        response =  self.getDsRequest(url)
        self.processResponse(response)
        #print response

    def processResponse(self, response):
        data = json.loads(response.read())
        if len(data) < 1 : return
        for dp in data.keys():
            print dp


if __name__ == '__main__':
    fdAd =  DataPortalMng():
    fdAd.discoverDataPortal()
