from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "train_and_compare_models-0222105800",
}

dag = DAG(
    "train_and_compare_models-0222105800",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `train_and_compare_models.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/process_data.ipynb

op_9ca028c1_8616_4fee_971f_f8225b23a7c9 = KubernetesPodOperator(
    name="process_data",
    namespace="airflow",
    image="quay.io/opendatahub-contrib/runtime-images:cuda-datascience-ubi9-py39_2023b_latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint http://s3.openshift-storage.svc --cos-bucket airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809 --cos-directory 'train_and_compare_models-0222105800' --cos-dependencies-archive 'process_data-9ca028c1-8616-4fee-971f-f8225b23a7c9.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.openshift-storage.svc",
        "AWS_S3_BUCKET": "airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_819bd5cd_a021_4ce6_80b4_fc119da9fb73 = KubernetesPodOperator(
    name="model_randomforest",
    namespace="airflow",
    image="quay.io/opendatahub-contrib/runtime-images:cuda-datascience-ubi9-py39_2023b_latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint http://s3.openshift-storage.svc --cos-bucket airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809 --cos-directory 'train_and_compare_models-0222105800' --cos-dependencies-archive 'model_randomforest-819bd5cd-a021-4ce6-80b4-fc119da9fb73.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.openshift-storage.svc",
        "AWS_S3_BUCKET": "airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_819bd5cd_a021_4ce6_80b4_fc119da9fb73 << op_9ca028c1_8616_4fee_971f_f8225b23a7c9


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_6ce8942a_82e1_4599_a195_30ba5459e2a7 = KubernetesPodOperator(
    name="model_gradient_boost",
    namespace="airflow",
    image="quay.io/opendatahub-contrib/runtime-images:cuda-datascience-ubi9-py39_2023b_latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint http://s3.openshift-storage.svc --cos-bucket airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809 --cos-directory 'train_and_compare_models-0222105800' --cos-dependencies-archive 'model_gradient_boost-6ce8942a-82e1-4599-a195-30ba5459e2a7.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.openshift-storage.svc",
        "AWS_S3_BUCKET": "airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_6ce8942a_82e1_4599_a195_30ba5459e2a7 << op_9ca028c1_8616_4fee_971f_f8225b23a7c9


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_5c7a887a_6833_4b0e_8795_e0b8bbd6d2b9 = KubernetesPodOperator(
    name="compare_and_push",
    namespace="airflow",
    image="quay.io/opendatahub-contrib/runtime-images:cuda-datascience-ubi9-py39_2023b_latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint http://s3.openshift-storage.svc --cos-bucket airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809 --cos-directory 'train_and_compare_models-0222105800' --cos-dependencies-archive 'compare_and_push-5c7a887a-6833-4b0e-8795-e0b8bbd6d2b9.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "AWS_S3_ENDPOINT": "http://s3.openshift-storage.svc",
        "AWS_S3_BUCKET": "airflow-storage-6ddf8b2b-517b-4511-84bc-58ebbbbaf809",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_5c7a887a_6833_4b0e_8795_e0b8bbd6d2b9 << op_819bd5cd_a021_4ce6_80b4_fc119da9fb73

op_5c7a887a_6833_4b0e_8795_e0b8bbd6d2b9 << op_6ce8942a_82e1_4599_a195_30ba5459e2a7
