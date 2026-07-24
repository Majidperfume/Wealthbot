from telegram import ReplyKeyboardMarkup


def get_main_menu():

    keyboard = [
        [
            "📊 داشبورد",
            "➕ ثبت تراکنش"
        ],
        [
            "🏦 حساب‌ها",
            "💱 ارزها"
        ],
        [
            "👤 اشخاص",
            "📑 گزارش‌ها"
        ],
        [
            "⚙️ تنظیمات"
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
