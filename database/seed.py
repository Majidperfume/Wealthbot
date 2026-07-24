from database.database import db


def seed_currencies():
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


def seed_asset_types():
    types = [
        "حساب بانکی",
        "پول نقد",
        "حساب بازی",
        "صندوق",
        "سرمایه گذاری",
        "سایر",
    ]

    for name in types:
        db.execute(
            """
            INSERT OR IGNORE INTO asset_types
            (name)
            VALUES (?)
            """,
            (name,),
        )


def seed_transaction_templates():
    templates = [
        ("انتقال", 1, 1),
        ("خرید", 1, 1),
        ("فروش", 1, 1),
        ("خرید ارز", 1, 1),
        ("فروش ارز", 1, 1),
        ("کمک مالی", 1, 1),
        ("هدیه", 1, 1),
        ("دریافت متفرقه", 0, 1),
        ("کاهش موجودی", 1, 0),
        ("افزایش موجودی", 0, 1),
    ]

    for name, source, destination in templates:
        db.execute(
            """
            INSERT OR IGNORE INTO transaction_templates
            (name, requires_source, requires_destination)
            VALUES (?, ?, ?)
            """,
            (name, source, destination),
        )


def seed():
    seed_currencies()
    seed_asset_types()
    seed_transaction_templates()


if __name__ == "__main__":
    seed()
