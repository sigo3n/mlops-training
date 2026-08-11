from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd

app = FastAPI()
model = mlflow.pyfunc.load_model("PATH_MODEL_ANDA")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: dict):
    df = pd.DataFrame([payload])
    pred = model.predict(df)
    return {"prediction": float(pred[0])}
