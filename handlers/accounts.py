from telegram import Update
from telegram.ext import ContextTypes

from keyboards.accounts_menu import get_accounts_menu
from models.account import (
    get_accounts,
    create_account
)


async def accounts_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🏦 مدیریت حساب‌ها",
        reply_markup=get_accounts_menu()
    )


async def list_accounts(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    accounts = get_accounts()

    if not accounts:
        await update.message.reply_text(
            "هیچ حسابی ثبت نشده است."
        )
        return


    text = "🏦 حساب‌های شما:\n\n"

    for account in accounts:
        text += f"• {account['name']}\n"


    await update.message.reply_text(text)



async def add_account_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["adding_account"] = True

    await update.message.reply_text(
        "نام حساب جدید را وارد کنید:"
    )



async def add_account_receive(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not context.user_data.get(
        "adding_account"
    ):
        return


    name = update.message.text


    create_account(
        name
    )


    context.user_data[
        "adding_account"
    ] = False


    await update.message.reply_text(
        f"✅ حساب {name} اضافه شد."
    )
