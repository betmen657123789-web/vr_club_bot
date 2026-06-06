from aiogram import Router
from aiogram.types import Message, CallbackQuery
from app.utils.formatter import now

from app.telegram.utils.banner import send_banner
from app.services.schedule_service import (
    check_current_status,
    get_next_booking,
    is_day_fully_free,
    had_bookings_today,
)

from app.telegram.keyboards.main_menu import main_menu

router = Router()
from datetime import datetime


def is_after_working_hours():
    return now().hour >= 21


# =========================
# 📊 TEXT LOGIC
# =========================
def get_club_status_text():

    # ⛔ новый приоритетный статус
    if is_after_working_hours():
        return (
            "🌙 На сегодня мы уже завершили работу\n\n"
            "После 21:00 клуб отдыхает вместе с нами\n"
            "Ждём вас завтра с новыми играми 🎮💛"
        )

    current_status = check_current_status()

    if current_status["is_busy"]:
        return (
            "🔴 Сейчас идёт аренда\n\n"
            f"Клуб освободится:\n"
            f"в {current_status['end_time']}"
        )

    next_booking = get_next_booking()

    if next_booking:
        return (
            "🟢 Сейчас клуб свободен\n\n"
            f"Следующая аренда:\n"
            f"в {next_booking['Начало']}"
        )

    if is_day_fully_free():
        return (
            "🟢 Сегодня клуб свободен весь день\n\n"
            "Можно приходить 🎮"
        )

    if had_bookings_today():
        return (
            "🟢 Сейчас клуб свободен\n\n"
            "На сегодня аренды закончились 🎮"
        )

    return "🟢 Сейчас клуб свободен"


# =========================
# 📍 MENU BUTTON
# =========================
@router.message(lambda message: message.text == "📊 Статус клуба")
async def club_status(message: Message):

    text = get_club_status_text()

    await send_banner(
        message,
        text,
        main_menu   # ✅ ВОТ ЭТО ОБЯЗАТЕЛЬНО
    )


# =========================
# 🔁 CALLBACK
# =========================
@router.callback_query(lambda c: c.data == "club_status")
async def club_status_callback(callback: CallbackQuery):

    await callback.answer()

    if not callback.message:
        return

    text = get_club_status_text()

    await send_banner(
        callback.message,
        text,
        main_menu   # ✅ тоже добавили
    )