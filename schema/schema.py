from pathlib import Path

csv_directory = Path(__file__).resolve().parent.parent / "1-lh_nautical_csv"
csv_files = sorted(csv_directory.glob("*.csv"))

sql_statements = []
for csv_path in csv_files:

    with csv_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()
        header = lines[0].strip().split(",")

    sql_statements.append(f"CREATE TABLE IF NOT EXISTS {csv_path.stem} ({', '.join(header)});")

# Print all generated SQL statements
# for stmt in sql_statements:
#     print(stmt)

current_directory = Path(__file__).resolve().parent
with open(current_directory / "schema.sql", "w", encoding="utf-8") as sql_file:
    sql_file.write("\n".join(sql_statements))