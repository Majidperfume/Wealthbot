    from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN

from handlers.start import start_command

from handlers.accounts import (
    accounts_menu,
    list_accounts,
    add_account_start,
    add_account_receive
)


def create_bot():

    app = Application.builder().token(
        BOT_TOKEN
    ).build()


    # start command
    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    # accounts menu
    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^🏦 حساب‌ها$"),
            accounts_menu
        )
    )


    # list accounts
    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^📋 لیست حساب‌ها$"),
            list_accounts
        )
    )


    # add account button
    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^➕ افزودن حساب$"),
            add_account_start
        )
    )


    # receive account name
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            add_account_receive
        )
    )


    return app



def run_bot():

    app = create_bot()

    print("WealthBot started...")

    app.run_polling()



if __name__ == "__main__":
    run_bot()
