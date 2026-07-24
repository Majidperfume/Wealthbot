from telegram import Update
from telegram.ext import ContextTypes

from keyboards.accounts_menu import get_accounts_menu
from models.account import get_accounts


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


    await update.message.reply_text(
        text
    )
