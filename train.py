import sys
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import pandas as pd

n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 100
max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 5

df = pd.read_csv("data/train.csv")
X_train, X_test, y_train, y_test = train_test_split(
    df.drop("target", axis=1), df["target"], test_size=0.2, random_state=42
)

mlflow.set_experiment("training-siang")
with mlflow.start_run():
    params = {"n_estimators": n_estimators, "max_depth": max_depth, "random_state": 42}
    mlflow.log_params(params)
    model = RandomForestClassifier(**params).fit(X_train, y_train)
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    mlflow.log_metric("auc", auc)
    mlflow.sklearn.log_model(model, "model")
    print(f"n_estimators={n_estimators}, max_depth={max_depth} -> AUC: {auc:.4f}")
