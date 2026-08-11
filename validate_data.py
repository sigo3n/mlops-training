import great_expectations as gx
import pandas as pd
import sys

context = gx.get_context()
validator = context.sources.pandas_default.read_csv("data/train.csv")

validator.expect_column_values_to_not_be_null("income")
validator.expect_column_values_to_be_between("age", min_value=18, max_value=100)
validator.expect_column_values_to_be_in_set("target", [0, 1])

results = validator.validate()
if not results.success:
    print("GAGAL: Data quality check tidak lolos — pipeline dihentikan")
    sys.exit(1)
print("LOLOS: Data quality check berhasil")
