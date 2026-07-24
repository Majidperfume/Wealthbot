from database.database import db


def seed():
    currencies = [
        ("IRR", "تومان", "﷼"),
        ("USD", "دلار", "$"),
        ("EUR", "یورو", "€"),
        ("AED", "درهم", "AED"),
        ("GBP", "پوند", "£"),
        ("OMR", "ریال عمان", "OMR"),
    ]

    for code, name, symbol in currencies:
        db.execute(
            """
            INSERT OR IGNORE INTO currencies
            (code, name, symbol)
            VALUES (?, ?, ?)
            """,
            (code, name, symbol),
        )


if __name__ == "__main__":
    seed()
