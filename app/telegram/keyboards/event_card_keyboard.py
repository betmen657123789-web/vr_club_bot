from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_event_card_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📞 Забронировать",
                    callback_data="booking_menu"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="prices_menu"
                )
            ]
        ]
    )