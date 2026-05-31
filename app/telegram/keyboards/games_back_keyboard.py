from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_games_back_keyboard(
    game_type
):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data=f"price_{game_type.lower()}"
                )
            ]
        ]
    )