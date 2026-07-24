from telegram.ext import Application

from config import BOT_TOKEN


def create_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    return app


def run_bot():
    app = create_bot()

    print("WealthBot started...")

    app.run_polling()


if __name__ == "__main__":
    run_bot()
