import os
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.environ.get("BOT_TOKEN")


if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN پیدا نشد. فایل .env را بررسی کنید."
    )


OWNER_ID = int(
    os.environ.get(
        "OWNER_ID",
        "0"
    )
)


DATABASE_PATH = "database/wealthbot.db"


TIMEZONE = "Asia/Tehran"
