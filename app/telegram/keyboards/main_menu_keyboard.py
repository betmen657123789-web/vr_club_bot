from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_main_menu_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️ Главное меню",
                    callback_data="main_menu"
                )
            ]
        ]
    )