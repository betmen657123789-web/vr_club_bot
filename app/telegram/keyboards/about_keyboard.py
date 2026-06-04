from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_about_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📸 Фото клуба",
                    callback_data="club_photos"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📍 Как добраться",
                    callback_data="club_map"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📞 Забронировать",
                    callback_data="booking_menu"
                )
            ]
        ]
    )