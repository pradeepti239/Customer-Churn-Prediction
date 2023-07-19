import mlflow
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler
from datetime import datetime

mlflow.set_experiment("CustomerChurn")

df = pd.read_csv("./data/telecom_churn.csv")

X = df.drop('Churn', axis=1)
y = df['Churn']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

X_train = np.array(X_train)
y_train = np.array(y_train)

timestamp = datetime.now().strftime("%Y-%m-%d %H%M%S")

with mlflow.start_run(run_name=f"Regression in Unbalanced data_{timestamp}"):

    mlflow.autolog(disable=True)

    mlflow.log_param("model", "LogisticRegression")

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mlflow.log_artifact('./model/prediction1.joblib')

    report = classification_report(y_test, y_pred, output_dict=True)
    recall = report['1']['recall']
    f1_score = report['1']['f1-score']
    accuracy = report['accuracy']

    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1-score", f1_score)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.end_run()

with mlflow.start_run(run_name=f"Regression in Balanced data_{timestamp}"):

    mlflow.autolog(disable=True)

    mlflow.log_param("oversampler", "RandomOverSampler")
    mlflow.log_param("model", "LogisticRegression")

    oversampler = RandomOverSampler(random_state=42)
    X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train, y_train)

    model1 = LogisticRegression()
    model1.fit(X_train_resampled, y_train_resampled)
    y_pred = model1.predict(X_test)

    mlflow.log_artifact('./model/prediction2.joblib')

    report = classification_report(y_test, y_pred, output_dict=True)
    recall = report['1']['recall']
    f1_score = report['1']['f1-score']
    accuracy = report['accuracy']

    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1-score", f1_score)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.end_run()