from handlers.asset_handler import get_assets


def assets_menu():
    assets = get_assets()

    if not assets:
        return "هنوز هیچ دارایی ثبت نشده است."

    text = "📦 دارایی‌ها:\n\n"

    for asset in assets:
        text += (
            f"ID: {asset['id']}\n"
            f"نام: {asset['name']}\n"
            f"نوع: {asset['type']}\n"
            f"ارز: {asset['currency']}\n"
            f"----------------\n"
        )

    return text
