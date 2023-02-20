from airflow import DAG
from airflow.decorators import task
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
from textwrap import dedent


with DAG(
    "TestDAG",
    default_args={
        "depends_on_past": False,
        "retries": 0,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:
    run_this = PapermillOperator(
        task_id="run_example_notebook",
        input_nb="/tmp/test.ipynb",
        output_nb="/tmp/out-{{ execution_date }}.ipynb",
        parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"},
    )

    run_this

    # test = KubernetesPodOperator(
    #     namespace="airflow",
    #     image="quay.io/eformat/airflow-runner:2.5.1",
    #     cmds=["bash", "-cx"],
    #     arguments=["echo", "10", "echo pwd"],
    #     name="test",
    #     task_id="test",
    #     get_logs=True,
    # )

    # test