from pathlib import Path
import csv
from helpers.helpers import is_integer, is_numeric, is_boolean, is_date, is_timestamp

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_DIR = BASE_DIR / "1-lh_nautical_csv"
OUTPUT_PATH = BASE_DIR / "schema" / "schema.sql"

def infer_type(values):
    values = [value.strip() for value in values if value.strip()]

    if not values:
        return "TEXT"

    if all(is_boolean(value) for value in values):
        return "BOOLEAN"

    if all(is_integer(value) for value in values):
        return "INTEGER"

    if all(is_numeric(value) for value in values):
        return "NUMERIC"

    if all(is_date(value) for value in values):
        return "DATE"

    if all(is_timestamp(value) for value in values):
        return "TIMESTAMP"

    return "TEXT"


def infer_table_schema(csv_path):
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)

        columns = {column: [] for column in header}

        for row in reader:
            for column, value in zip(header, row):
                columns[column].append(value)

    return [
        (column.strip(), infer_type(values))
        for column, values in columns.items()
    ]


def generate_sql():
    sql_blocks = []

    for csv_path in sorted(CSV_DIR.glob("*.csv")):
        table_name = csv_path.stem
        columns = infer_table_schema(csv_path)

        columns_sql = ",\n    ".join(
            f'"{name}" {data_type}'
            for name, data_type in columns
        )

        sql = (
            f'CREATE TABLE IF NOT EXISTS "{table_name}" (\n'
            f'    {columns_sql}\n'
            f');'
        )

        sql_blocks.append(sql)

    OUTPUT_PATH.write_text(
        "\n\n".join(sql_blocks),
        encoding="utf-8"
    )


if __name__ == "__main__":
    generate_sql()
    print(f"Schema criado em: {OUTPUT_PATH}")