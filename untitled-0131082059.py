from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled-0131082059",
}

dag = DAG(
    "untitled-0131082059",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: telecom-customer-churn-airflow/t.ipynb

op_b565f4b8_0983_442c_a817_fdbc70f3cc23 = KubernetesPodOperator(
    name="t",
    namespace="airflow",
    image="image-registry.openshift-image-registry.svc:5000/rainforest-ci-cd/airflow-runner:2.3.2",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'untitled' --cos-endpoint http://s3.openshift-storage.svc --cos-bucket airflow-storage-729b10d1-f44d-451d-badb-fbd140418763 --cos-directory 'untitled-0131082059' --cos-dependencies-archive 't-b565f4b8-0983-442c-a817-fdbc70f3cc23.tar.gz' --file 'telecom-customer-churn-airflow/t.ipynb' "
    ],
    task_id="t",
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

op_b565f4b8_0983_442c_a817_fdbc70f3cc23.image_pull_policy = "Always"
