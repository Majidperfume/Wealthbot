import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "database"
DATABASE_FILE = DATABASE_DIR / "wealthbot.db"
SCHEMA_FILE = DATABASE_DIR / "schema.sql"


class Database:
    def __init__(self):
        DATABASE_DIR.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(DATABASE_FILE)
        self.connection.row_factory = sqlite3.Row

        self._create_schema()

    def _create_schema(self):
        with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
            self.connection.executescript(file.read())

        self.connection.commit()

    def execute(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def executemany(self, query, params):
        cursor = self.connection.cursor()
        cursor.executemany(query, params)
        self.connection.commit()
        return cursor

    def fetchone(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def fetchall(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def close(self):
        self.connection.close()


db = Database()
