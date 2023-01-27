from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.decorators import task

from datetime import datetime, timedelta
from textwrap import dedent


def process_data_():
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    import pandas as pd

    telecom_cust = pd.read_csv('../data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

    # Converting Total Charges to a numerical data type.
    telecom_cust.TotalCharges = pd.to_numeric(telecom_cust.TotalCharges, errors='coerce')
    telecom_cust.isnull().sum()

    #Removing missing values 
    telecom_cust.dropna(inplace = True)
    #Remove customer IDs from the data set
    df2 = telecom_cust.iloc[:,1:]
    #Convertin the predictor variable in a binary numeric variable
    df2['Churn'].replace(to_replace='Yes', value=1, inplace=True)
    df2['Churn'].replace(to_replace='No',  value=0, inplace=True)

    #Let's convert all the categorical variables into dummy variables
    df_dummies = pd.get_dummies(df2)
    df_dummies.head()

    y = df_dummies['Churn'].values
    X = df_dummies.drop(columns = ['Churn'])

    # Scaling all the variables to a range of 0 to 1
    features = X.columns.values
    scaler = MinMaxScaler(feature_range = (0,1))
    scaler.fit(X)
    X = pd.DataFrame(scaler.transform(X))
    X.columns = features

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    print("Done!")
    #Save somewhere
    

def model_randomforest_():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import metrics

    X_train, y_train, X_test, y_test = load(save_location)

    model = RandomForestClassifier(n_estimators=1000 , oob_score = True, n_jobs = -1,
                                    random_state =50, max_features = "auto",
                                    max_leaf_nodes = 30)
    model.fit(X_train, y_train)

    model_location = save(model)
    ti.xcom_push(key='ModelLocation', value=model_location)

    prediction_test = model.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, prediction_test)
    return accuracy


def model_xgboost_():
    from xgboost import XGBClassifier
    from sklearn import metrics

    save_location = ti.xcom_pull(key='TrainingAndTestingStorage', task_id="process_data")

    X_train, y_train, X_test, y_test = load(save_location)

    model = XGBClassifier()
    model.fit(X_train, y_train)

    model_location = save(model)
    ti.xcom_push(key='ModelLocation', value=model_location)

    preds = model.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, preds)
    ti.xcom_push(key='Accuracy', value=accuracy)


def comapre_():
    xgboost_acc = ti.xcom_pull(key='Accuracy', task_id="XGBoostTrainAndEval")
    randomforest_acc = ti.xcom_pull(key='Accuracy', task_id="RandomForestTrainAndEval")

    if xgboost_acc>randomforest_acc:
        ti.xcom_push(key='BestModel', value=xgboost_acc.task_id)
    else:
        ti.xcom_push(key='BestModel', value=randomforest_acc.task_id)


def push_model_():
    prod_model_location = ""

    best_model_task_id = ti.xcom_pull(key='BestModel', task_id="CompareModels")
    best_model_location = ti.xcom_pull(key='ModelLocation', task_id=best_model_task_id)

    model = load(best_model_location)
    save(prod_model_location)


with DAG(
    "CustomerChurnModel",
    default_args={
        "depends_on_past": False,
        "retries": 1,
    },
    description="A simple tutorial DAG",
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:
    @task
    def process_data():
        process_data_()

    task1 = process_data()