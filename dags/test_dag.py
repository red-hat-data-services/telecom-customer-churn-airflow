from airflow import DAG
from airflow.decorators import task
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

from datetime import datetime, timedelta
from textwrap import dedent


def simple_function_():
    print("Hello!")




with DAG(
    "CustomerChurnModel2",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:
    # @task
    # def simple_function():
    #     simple_function_()

    # res = simple_function()

    # res
    test = KubernetesPodOperator(
        namespace="airflow",
        image="quay.io/apache/bash",
        cmds=["bash", "-cx"],
        arguments=["echo", "10", "echo pwd"],
        name="test",
        # is_delete_operator_pod=True,
        # in_cluster=True,
        task_id="test",
        get_logs=True,
    )

    test