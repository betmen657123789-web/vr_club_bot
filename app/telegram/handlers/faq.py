from aiogram import Router
from aiogram.types import (
    Message,
    CallbackQuery
)
from app.telegram.keyboards.faq_keyboard import (
    get_faq_back_keyboard
)

from app.services.faq_service import (
    get_faq_answer
)
from app.telegram.keyboards.faq_keyboard import (
    get_faq_keyboard
)


router = Router()


@router.message(
    lambda message:
    message.text == "❓ FAQ"
)
async def faq_menu(message: Message):

    await message.answer(
        "❓ Частые вопросы:",
        reply_markup=get_faq_keyboard()
    )


@router.callback_query(
    lambda callback:
    callback.data == "faq_back"
)
async def faq_back(callback: CallbackQuery):

    await callback.answer()

    await callback.message.edit_text(
        "❓ Частые вопросы:",
        reply_markup=get_faq_keyboard()
    )


@router.callback_query(
    lambda callback:
    callback.data.startswith("faq_")
)
async def faq_answer(callback: CallbackQuery):

    await callback.answer()

    question = callback.data.replace(
        "faq_",
        ""
    )

    answer = get_faq_answer(question)

    text = (
        f"❓ {question}\n\n"
        f"{answer}"
    )

    await callback.message.edit_text(
        text,
        reply_markup=get_faq_back_keyboard()
    )