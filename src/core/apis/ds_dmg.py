import os
import wget
import boto3
from botocore.exceptions import ClientError
import logging


class DsDMG:

    def __init__(self):
        self.fileName = None
        self.destType = None #Local, S3, etc
        self.dest = None
 

    def dwmgr(self):
        if self.checkDest():
        if self.destType.upper()== 'LOCAL':
           self.fromWeb(self.fileName,self.dest)


    def checkDest(self):
        if self.destType.upper()== 'LOCAL':
            return os.path.exist(self.dest)
        elif self.destType == 'S3':
            s3 = boto3.Client('s3')
            try:
                response = s3.head_bucket(Bucket=self.dest) 
            except ClientError as e:
                logging.debug(e)
                return False
	    return True
 
  	
    def fromWeb(self,url, opt):
        trr:
            wget.download(url, out = opt)
        except:
            logging.debug('Unable to Download')
 


 
