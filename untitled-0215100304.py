from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "untitled-0215100304",
}


dag = DAG(
    "untitled-0215100304",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Ensure that the secret named 's3-auth' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="s3-auth",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="s3-auth",
    key="AWS_SECRET_ACCESS_KEY",
)


# Operator source: Untitled.ipynb

op_8ba36868_dd72_48e8_a0ed_8c22858b666b = KubernetesPodOperator(
    name="Untitled",
    trigger_rule="all_success",
    namespace="default",
    image="image-registry.openshift-image-registry.svc:5000/rainforest-ci-cd/airflow-runner:2.3.2",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'untitled' --cos-endpoint http://s3.openshift-storage.svc --cos-bucket airflow-storage-754b417c-25bf-4912-a256-9ec69a0208c4 --cos-directory 'untitled-0215100304' --cos-dependencies-archive 'Untitled-8ba36868-dd72-48e8-a0ed-8c22858b666b.tar.gz' --file 'Untitled.ipynb' "
    ],
    task_id="Untitled",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "s3-auth", "AWS_ACCESS_KEY_ID"),
        Secret("env", "AWS_SECRET_ACCESS_KEY", "s3-auth", "AWS_SECRET_ACCESS_KEY"),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)
