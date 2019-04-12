from os import path
import sys

from core.fdaMngr import FdaAdapter
from core.dataPortal import DataPortal
from airflow import DAG
from airflow.operators import BashOperator,PythonOperator
from datetime import datetime, timedelta


seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                      datetime.min.time())

def dataPortal(ds, **kwargs):
    #fdAd = FdaAdapter()
    #fdAd.processResponse(fdAd.getDsRequest())

    dp = DataPortal()
    dp.createDataPortal()


run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=dataPortal,
    dag=dag,
)
