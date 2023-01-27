from airflow import DAG
from airflow.decorators import task

from datetime import datetime, timedelta
from textwrap import dedent


def simple_function_():
    print("Hello!")




with DAG(
    "CustomerChurnModel",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:
    @task.kubernetes(images = "python:3.8-slim-buster", namespace = "airflow", do_xcom_push=True)
    def simple_function():
        simple_function_()