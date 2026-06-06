from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from app.services.faq_service import (
    get_faq_questions
)


def get_faq_keyboard():

    questions = get_faq_questions()

    keyboard = []

    for i, question in enumerate(questions):

        keyboard.append([
            InlineKeyboardButton(
                text=f"❓ {question}",
                callback_data=f"faq_{i}"
            )
        ])

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )


def get_faq_back_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="⬅️ К вопросам",
                    callback_data="faq_back"
                )
            ],



        ]
    )