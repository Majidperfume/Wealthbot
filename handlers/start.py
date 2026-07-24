from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main_menu import get_main_menu


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    message = f"""
سلام {user.first_name} 👋

به WealthBot خوش آمدی.

سیستم مدیریت دارایی شخصی شما آماده است.
"""


    await update.message.reply_text(
        message,
        reply_markup=get_main_menu()
    )
