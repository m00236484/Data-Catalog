import sys, os

from core.businessLayer.dataSetBL import DataSetBl
from core.apis.fdaMngr import FdaAdapter
from core.dataLayer.dataportal import DataPortal

if __name__ == '__main__':
    #fdAd = FdaAdapter()
    #fdAd.processResponse(fdAd.getDsRequest())
    dp = DataPortal()
    dp.createDataPortal()
