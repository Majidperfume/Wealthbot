import sqlite3
from pathlib import Path


DATABASE_FILE = Path(__file__).parent / "wealthbot.db"
SCHEMA_FILE = Path(__file__).parent / "schema.sql"


def initialize_database():
    connection = sqlite3.connect(DATABASE_FILE)

    with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
        schema = file.read()

    connection.executescript(schema)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()
