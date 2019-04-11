from os import path
import sys
sys.path.append(path.abspath('/home/ubuntu/Data-Catalog/Data-Catalog/src/'))

from core.apis.fdaMngr import FdaAdapter
from core.dataLayer.dataPortal import DataPortal
from airflow import DAG
from airflow.operators import BashOperator,PythonOperator
from datetime import datetime, timedelta


seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                      datetime.min.time())

def dataPortal(ds, **kwargs):
    #fdAd = FdaAdapter()
    #fdAd.processResponse(fdAd.getDsRequest())
    print "Test Workflow"
    dp = DataPortal()
    dp.createDataPortal()


run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=dataPortal,
    dag=dag,
)