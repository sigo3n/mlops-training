Write-Host "Starting MLflow Tracking Server..." -ForegroundColor Green

mlflow db upgrade sqlite:///D:/pusilkom/mlops-training/mlflow.db

if ($LASTEXITCODE -ne 0) {
    Write-Host "MLflow database migration failed!" -ForegroundColor Red
    exit 1
}

Write-Host "Database ready." -ForegroundColor Green
Write-Host "Starting MLflow Server..." -ForegroundColor Green

mlflow server `
    --backend-store-uri "sqlite:///D:/pusilkom/mlops-training/mlflow.db" `
    --host 127.0.0.1 `
    --port 5000