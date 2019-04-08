import wget

dwnToS3 = 'arn:aws:s3:::ds-temp-dir'
url = 'https://download.open.fda.gov/device/enforcement/device-enforcement-0001-of-0001.json.zip'
wget.download(url, -ouput='arn:aws:s3:::ds-temp-dir')



