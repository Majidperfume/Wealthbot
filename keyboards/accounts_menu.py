from telegram import ReplyKeyboardMarkup


def get_accounts_menu():

    keyboard = [
        [
            "➕ افزودن حساب",
            "📋 لیست حساب‌ها"
        ],
        [
            "⬅️ بازگشت"
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
