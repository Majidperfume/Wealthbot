import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8893799861:AAGFV4ghnz8Sh--1uOGkKafSFaopGTG2wjg")

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

DATABASE_PATH = "database/wealthbot.db"

TIMEZONE = "Asia/Tehran"
