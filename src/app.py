import sys, os

from core.businessLayer.dataSetBL import DataSetBl
from core.services.fdaMngr import FdaAdapter


if __name__ == '__main__':
    fdAd = FdaAdapter()
    fdAd.processResponse(fdAd.getDsRequest())
