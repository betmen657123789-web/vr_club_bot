from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_about_back_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="about_menu"
                )
            ]
        ]
    )