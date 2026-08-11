from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd

df_training = pd.read_csv("data/train.csv")
df_production = pd.read_csv("data/production_simulasi.csv")

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=df_training, current_data=df_production)
report.save_html("drift_report.html")
print("Laporan drift tersimpan di drift_report.html")
