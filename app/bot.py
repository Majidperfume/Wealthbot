from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN

from handlers.start import start_command


def create_bot():

    app = Application.builder().token(
        BOT_TOKEN
    ).build()


    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    return app



def run_bot():

    app = create_bot()

    print("WealthBot started...")

    app.run_polling()



if __name__ == "__main__":
    run_bot()
