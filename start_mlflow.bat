@echo off
echo ========================================
echo Starting MLflow Tracking Server
echo ========================================

mlflow db upgrade sqlite:///D:/pusilkom/mlops-training/mlflow.db

if errorlevel 1 (
    echo.
    echo ERROR: MLflow database migration failed!
    pause
    exit /b 1
)

echo.
echo Database ready.
echo.
echo Starting MLflow Server...
echo Open http://127.0.0.1:5000
echo.

mlflow server --backend-store-uri "sqlite:///D:/pusilkom/mlops-training/mlflow.db" --host 127.0.0.1 --port 5000

pause