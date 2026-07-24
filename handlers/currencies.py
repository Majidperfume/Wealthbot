from telegram import Update
from telegram.ext import ContextTypes

from keyboards.currencies_menu import get_currencies_menu

from models.currency import (
    get_currencies,
    create_currency
)


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


    await update.message.reply_text(text)



async def add_currency_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["adding_currency"] = {
        "step": 1
    }


    await update.message.reply_text(
        "نام ارز را وارد کنید:"
    )



async def add_currency_receive(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = context.user_data.get(
        "adding_currency"
    )


    if not data:
        return


    text = update.message.text


    if data["step"] == 1:

        data["name"] = text
        data["step"] = 2

        await update.message.reply_text(
            "کد ارز را وارد کنید.\nمثال: USD"
        )

        return


    if data["step"] == 2:

        data["code"] = text.upper()
        data["step"] = 3

        await update.message.reply_text(
            "نماد ارز را وارد کنید.\nمثال: $"
        )

        return


    if data["step"] == 3:

        data["symbol"] = text


        create_currency(
            data["name"],
            data["code"],
            data["symbol"]
        )


        context.user_data.pop(
            "adding_currency"
        )


        await update.message.reply_text(
            f"✅ ارز {data['name']} اضافه شد."
        )
