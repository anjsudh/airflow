from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'anjana',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 21),
    'email': ['anjsudh24@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG('Helloworld', default_args=default_args) as dag:

    t1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello World from Task 1"',
        dag=dag)

    t2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Hello World from Task 2"',
        dag=dag)

    t3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Hello World from Task 3"',
        dag=dag)

    t4 = BashOperator(
        task_id='task_4',
        bash_command='echo "Hello World from Task 4"',
        dag=dag)

    t2.set_upstream(t1)
    t3.set_upstream(t1)
    t4.set_upstream(t2)
    t4.set_upstream(t3)
