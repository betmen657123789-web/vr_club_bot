from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


main_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(
                text="🟢 Свободно ли сейчас"
            )
        ],
[
            KeyboardButton(
                text="📞 Забронировать"
            ),
KeyboardButton(
                text="ℹ️ О клубе"
            )


        ],
[

        ],

        [
            KeyboardButton(
                text="🎮 Тарифы и услуги"
            ),

            KeyboardButton(
                text="❓ FAQ"
            )
        ]

    ],
    resize_keyboard=True
)
