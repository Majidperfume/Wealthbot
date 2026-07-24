from handlers.asset_menu import assets_menu


def route(action):

    if action == "assets":
        return assets_menu()

    if action == "transactions":
        return "📝 بخش ثبت تراکنش"

    if action == "reports":
        return "📊 بخش گزارش‌ها"

    if action == "settings":
        return "⚙️ بخش تنظیمات"

    return "دستور نامعتبر است"
