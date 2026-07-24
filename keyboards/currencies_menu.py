from telegram import ReplyKeyboardMarkup


def get_currencies_menu():

    keyboard = [
        [
            "➕ افزودن ارز",
            "📋 لیست ارزها"
        ],
        [
            "⬅️ بازگشت"
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
