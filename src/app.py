import sys, os

from businessLayer.dataSetBL import DataSetBl
from services.fdaMngr import FdaAdapter


if __name__ == '__main__':
    fdAd = FdaAdapter()
    fdAd.processResponse(fdAd.getDsRequest())
