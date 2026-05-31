from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)



def get_prices_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 PlayStation",
                    callback_data="price_ps"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🥽 VR",
                    callback_data="price_vr"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎉 Мероприятия",
                    callback_data="price_event"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⭐ Доп. услуги",
                    callback_data="price_extra"
                )
            ]
        ]
    )