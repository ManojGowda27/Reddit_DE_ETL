from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys
import  s3fs
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline


default_args = {
    'owner': '25exy',
    'start_date': datetime(2024, 3, 7)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']

)

#Extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    provide_context=True,
    op_kwargs = {
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

#upload to s3
upload_s3 = PythonOperator(
    task_id='reddit_upload_s3',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3