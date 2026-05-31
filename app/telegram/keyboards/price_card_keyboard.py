from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_price_card_keyboard(
    games_type
):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📋 Все игры",
                    callback_data=f"all_games_{games_type}"
                )
            ],
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