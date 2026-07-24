import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "wealthbot.db"


def get_connection():
    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


def execute_query(query, params=()):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(query, params)

    connection.commit()

    result = cursor.fetchall()

    connection.close()

    return result


def execute_one(query, params=()):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(query, params)

    connection.commit()

    result = cursor.fetchone()

    connection.close()

    return result
