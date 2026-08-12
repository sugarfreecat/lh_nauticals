import os
import psycopg
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DB_HOST = os.environ.get("POSTGRES_HOST", "localhost")
DB_PORT = os.environ.get("POSTGRES_PORT", "5432")
DB_USER = os.environ.get("POSTGRES_USER", "postgres")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
DB_NAME = os.environ.get("POSTGRES_DB", "lh_nauticals")

SCHEMA_FILE = BASE_DIR / "schema/schema.sql"
CSV_DIRECTORY = BASE_DIR / "1-lh_nautical_csv"

def create_database():
    with psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname="postgres",
    ) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
            cursor.execute(f"CREATE DATABASE {DB_NAME};")
            cursor.close()

def create_tables():
    with psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
    ) as conn:
        with conn.cursor() as cursor:
            with open(SCHEMA_FILE, "r", encoding="utf-8") as schema_file:
                schema_sql = schema_file.read()
            cursor.execute(schema_sql)
            cursor.close()
        conn.commit()

def load_csv_files():
    csv_files = sorted(CSV_DIRECTORY.glob("*.csv"))

    with psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
    ) as conn:
        with conn.cursor() as cursor:
            for csv_path in csv_files:
                table_name = csv_path.stem
                with csv_path.open("r", encoding="utf-8", newline="") as f:
                    # Use the copy() context manager and stream the file contents into it
                    with cursor.copy(f"COPY {table_name} FROM STDIN WITH CSV HEADER") as copy:
                        for line in f:
                            copy.write(line)
        conn.commit()

if __name__ == "__main__":
    create_database()
    create_tables()
    load_csv_files()