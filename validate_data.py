import sys
import pandas as pd
import great_expectations as gx


DATA_PATH = "data/train.csv"


def validate_data():

    print(f"Loading dataset: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    print(
        f"Dataset loaded: {len(df)} rows, {len(df.columns)} columns"
    )

    # ---------------------------------------------------------
    # Basic validation
    # ---------------------------------------------------------

    success = True

    # income tidak boleh NULL
    if df["income"].isnull().any():
        print("FAIL: Kolom income mengandung NULL")
        success = False
    else:
        print("PASS: income tidak mengandung NULL")

    # age harus 18-100
    invalid_age = ~df["age"].between(18, 100)

    if invalid_age.any():
        print(
            f"FAIL: Terdapat {invalid_age.sum()} nilai age "
            "di luar range 18-100"
        )
        success = False
    else:
        print("PASS: age berada pada range 18-100")

    # target harus 0 atau 1
    invalid_target = ~df["target"].isin([0, 1])

    if invalid_target.any():
        print(
            f"FAIL: Terdapat {invalid_target.sum()} "
            "nilai target selain 0/1"
        )
        success = False
    else:
        print("PASS: target hanya berisi 0 dan 1")

    # ---------------------------------------------------------
    # Pipeline gate
    # ---------------------------------------------------------

    if not success:
        print(
            "GAGAL: Data quality check tidak lolos "
            "— pipeline dihentikan"
        )
        sys.exit(1)

    print("LOLOS: Data quality check berhasil")


if __name__ == "__main__":
    validate_data()
