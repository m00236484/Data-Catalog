import urllib
import json

class FdaAdapter():
    def __init__(self):
        self.id = None

    def getDsRequest(self):
        url = "https://api.fda.gov/download.json"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data


if __name__ == '__main__':
    fdAd = FdaAdapter()
    fdAd.getDsRequest()
