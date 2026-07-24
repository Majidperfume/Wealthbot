import os
from dotenv import load_dotenv

load_dotenv()

print("CONFIG TEST")
print("BOT_TOKEN exists:", bool(os.getenv("BOT_TOKEN")))
print("TOKEN_ID exists:", bool(os.getenv("TOKEN_ID")))

BOT_TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TOKEN_ID")

if not BOT_TOKEN:
    raise ValueError(
        "No Telegram token found"
    )

OWNER_ID = int(
    os.getenv("OWNER_ID", "0")
)

DATABASE_PATH = "database/wealthbot.db"

TIMEZONE = "Asia/Tehran"
