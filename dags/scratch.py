from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def print_hello():
    return 'Hello'


dag = DAG(
    'scratch',
    description='scratch',
    schedule_interval='0 11 * * *',
    start_date=datetime(2018, 4, 23),
)
   
 
t1 = PythonOperator(
    task_id='scratch',
    python_callable=print_hello,
    dag=dag
)

t1

