from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

OUTPUT_FILE = PROCESSED_DIR / "CIC-IDS2017-cleaned-combined.csv"


def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    return df


def main():

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    csv_files = list(RAW_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {RAW_DIR}"
        )

    print(f"Found {len(csv_files)} CSV files.")

    dataframes = []

    for file in csv_files:

        print(f"Reading: {file.name}")

        df = pd.read_csv(
            file,
            encoding="latin1",
            low_memory=False
        )

        df = clean_columns(df)

        if "Label" not in df.columns:
            print(f"Skipping {file.name}: Label column not found.")
            continue

        dataframes.append(df)

        print(f"Rows: {len(df)}")

    if not dataframes:
        raise ValueError("No valid datasets found.")

    combined = pd.concat(
        dataframes,
        ignore_index=True
    )

    combined = combined.replace(
        [float("inf"), float("-inf")],
        pd.NA
    )

    combined = combined.dropna()

    combined.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nDataset created successfully.")
    print(f"Rows: {len(combined)}")
    print(f"Columns: {len(combined.columns)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()