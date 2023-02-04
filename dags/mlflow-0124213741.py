from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.kubernetes.secret import Secret


args = {
    "project_id": "mlflow-0124213741",
}


dag = DAG(
    "mlflow-0124213741",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.10.1 pipeline editor using `mlflow.pipeline`.
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


# Operator source: aiml-demos/mlflow/model_package.py

op_e3cac8c9_eefc_47e9_a383_9864c7455251 = KubernetesPodOperator(
    name="model_package",
    trigger_rule="all_success",
    namespace="daintree-dev",
    image="image-registry.openshift-image-registry.svc:5000/rainforest-ci-cd/airflow-runner:2.3.2",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mlflow' --cos-endpoint http://minio.rainforest-ci-cd.svc.cluster.local:9000 --cos-bucket airflow-daintree-dev --cos-directory 'mlflow-0124213741' --cos-dependencies-archive 'model_package-e3cac8c9-eefc-47e9-a383-9864c7455251.tar.gz' --file 'aiml-demos/mlflow/model_package.py' --outputs 'build.info' "
    ],
    task_id="model_package",
    env_vars={
        "MODEL_NAME": "TestModel",
        "MODEL_VERSION": "1",
        "IMAGE_TAG": "latest",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mlflow-{{ ts_nodash }}",
    },
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_e3cac8c9_eefc_47e9_a383_9864c7455251.image_pull_policy = "Always"


# Operator source: aiml-demos/mlflow/model_deploy.py

op_3b8696a6_b732_45e5_b33d_72b77e685ce6 = KubernetesPodOperator(
    name="model_deploy",
    trigger_rule="all_success",
    namespace="daintree-dev",
    image="image-registry.openshift-image-registry.svc:5000/rainforest-ci-cd/airflow-runner:2.3.2",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'mlflow' --cos-endpoint http://minio.rainforest-ci-cd.svc.cluster.local:9000 --cos-bucket airflow-daintree-dev --cos-directory 'mlflow-0124213741' --cos-dependencies-archive 'model_deploy-3b8696a6-b732-45e5-b33d-72b77e685ce6.tar.gz' --file 'aiml-demos/mlflow/model_deploy.py' --inputs 'build.info' "
    ],
    task_id="model_deploy",
    env_vars={
        "MODEL_NAME": "TestModel",
        "MODEL_VERSION": "1",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "mlflow-{{ ts_nodash }}",
    },
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_3b8696a6_b732_45e5_b33d_72b77e685ce6.image_pull_policy = "Always"

op_3b8696a6_b732_45e5_b33d_72b77e685ce6 << op_e3cac8c9_eefc_47e9_a383_9864c7455251
