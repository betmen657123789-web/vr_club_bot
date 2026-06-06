from aiogram import Router
from aiogram.types import Message, CallbackQuery

from app.telegram.utils.banner import send_banner
from app.telegram.keyboards.faq_keyboard import (
    get_faq_back_keyboard,
    get_faq_keyboard
)

from app.services.faq_service import get_faq_answer

router = Router()


# =========================
# 📌 FAQ MENU
# =========================
@router.message(lambda message: message.text == "❓ FAQ")
async def faq_menu(message: Message):

    await send_banner(
        message,
        "❓ Частые вопросы:",
        get_faq_keyboard()
    )


# =========================
# 🔙 BACK BUTTON
# =========================
@router.callback_query(lambda callback: callback.data == "faq_back")
async def faq_back(callback: CallbackQuery):

    await callback.answer()

    await send_banner(
        callback.message,
        "❓ Частые вопросы:",
        get_faq_keyboard()
    )


# =========================
# ❓ FAQ ANSWER
# =========================
@router.callback_query(lambda c: c.data.startswith("faq_"))
async def faq_answer(callback: CallbackQuery):

    await callback.answer()

    faq_id = int(callback.data.replace("faq_", ""))

    item = get_faq_answer(faq_id)

    text = (
        f"❓ {item['question']}\n\n"
        f"{item['answer']}"
    )

    await send_banner(
        callback.message,
        text,
        get_faq_back_keyboard()
    )