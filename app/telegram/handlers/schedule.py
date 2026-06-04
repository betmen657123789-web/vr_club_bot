from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery

from app.telegram.keyboards.schedule_keyboard import (
    get_schedule_keyboard,
    get_calendar_keyboard
)

from app.services.schedule_service import (
    get_bookings_by_date,
    get_free_slots
)

from app.content.contacts import BOOKING_TEXT
from app.utils.formatter import format_date_title
from app.telegram.utils.banner import send_banner

router = Router()


# =========================
# 📅 MAIN MENU
# =========================
@router.message(lambda message: message.text == "📅 Расписание")
async def schedule_menu(message: Message):

    await send_banner(
        message,
        "📅 Выберите дату:",
        get_schedule_keyboard()
    )


# =========================
# 📅 OPEN CALENDAR
# =========================
@router.callback_query(lambda c: c.data == "open_calendar")
async def open_calendar(callback: CallbackQuery):

    await callback.answer()

    await send_banner(
        callback.message,
        "📅 Выберите дату:",
        get_calendar_keyboard()
    )


# =========================
# 📅 SELECT DATE
# =========================
@router.callback_query(lambda c: c.data.startswith("schedule_"))
async def schedule_by_date(callback: CallbackQuery):

    await callback.answer()

    date = callback.data.split("_")[1]

    bookings = get_bookings_by_date(date)
    free_slots = get_free_slots(date)
    beautiful_date = format_date_title(date)

    text = f"📅 {beautiful_date}\n\n"

    # 🔴 занятые слоты
    if bookings:
        text += "🔴 Занято:\n"
        for booking in bookings:
            text += f"{booking['start']} - {booking['end']}\n"
            if booking.get("comment"):
                text += f"🎉 {booking['comment']}\n"
        text += "\n"
    else:
        text += "🟢 Аренд нет\n\n"

    # 🟢 свободные
    text += "🟢 Свободно:\n"
    for slot in free_slots:
        text += f"{slot['start']} - {slot['end']}\n"

    text += f"\n{BOOKING_TEXT}"

    # ❗ ВАЖНО: НЕ edit_text если ты используешь banner
    await send_banner(
        callback.message,
        text,
        get_schedule_keyboard()
    )
