from handlers.asset_handler import get_assets


async def assets_menu(update, context):

    assets = get_assets()

    if not assets:
        await update.message.reply_text(
            "هنوز هیچ دارایی ثبت نشده است."
        )
        return


    text = "📦 دارایی‌ها:\n\n"


    for asset in assets:

        text += (
            f"ID: {asset['id']}\n"
            f"نام: {asset['name']}\n"
            f"نوع: {asset['type']}\n"
            f"ارز: {asset['currency']}\n"
            f"----------------\n"
        )


    await update.message.reply_text(text)
