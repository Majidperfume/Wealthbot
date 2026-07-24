from telegram import Update
from telegram.ext import ContextTypes

from keyboards.currencies_menu import get_currencies_menu

from models.currency import get_currencies


async def currencies_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "💱 مدیریت ارزها",
        reply_markup=get_currencies_menu()
    )



async def list_currencies(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    currencies = get_currencies()


    if not currencies:
        await update.message.reply_text(
            "هیچ ارزی ثبت نشده است."
        )
        return


    text = "💱 ارزهای شما:\n\n"


    for currency in currencies:
        text += (
            f"• {currency['name']} "
            f"({currency['code']})\n"
        )


    await update.message.reply_text(
        text
    )
