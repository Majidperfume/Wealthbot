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

from handlers.currencies import (
    currencies_menu,
    list_currencies,
    add_currency_start,
    add_currency_receive
)

from handlers.asset_menu import (
    assets_menu
)


def create_bot():

    app = Application.builder().token(
        BOT_TOKEN
    ).build()


    # Start

    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    # =================
    # Accounts
    # =================

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^🏦 حساب‌ها$"),
            accounts_menu
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^📋 لیست حساب‌ها$"),
            list_accounts
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^➕ افزودن حساب$"),
            add_account_start
        )
    )


    # =================
    # Currencies
    # =================

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^💱 ارزها$"),
            currencies_menu
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^📋 لیست ارزها$"),
            list_currencies
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^➕ افزودن ارز$"),
            add_currency_start
        )
    )


    # =================
    # Assets
    # =================

    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^📦 دارایی‌ها$"),
            assets_menu
        )
    )


    # =================
    # Receiving text inputs
    # =================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            add_account_receive
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            add_currency_receive
        )
    )


    return app



def run_bot():

    app = create_bot()

    print("WealthBot started...")

    app.run_polling()



if __name__ == "__main__":
    run_bot()
