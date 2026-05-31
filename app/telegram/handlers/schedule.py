from aiogram import Router
from app.utils.formatter import (
    format_date_title
)
from aiogram.types import (
    Message,
    CallbackQuery
)

from app.telegram.keyboards.schedule_keyboard import (
    get_schedule_keyboard,
    get_calendar_keyboard
)

from app.services.schedule_service import (
    get_bookings_by_date,
    get_free_slots
)
from app.content.contacts import (
    BOOKING_TEXT
)



router = Router()


@router.message(
    lambda message:
    message.text == "📅 Расписание"
)
async def schedule_menu(message: Message):

    await message.answer(
        "Выберите дату:",
        reply_markup=get_schedule_keyboard()
    )
@router.callback_query(
    lambda callback:
    callback.data == "open_calendar"
)
async def open_calendar(callback: CallbackQuery):

    await callback.answer()

    await callback.message.edit_text(
        "📅 Выберите дату:",
        reply_markup=get_calendar_keyboard()
    )

@router.callback_query(
    lambda callback:
    callback.data.startswith("schedule_")
)
async def schedule_by_date(callback: CallbackQuery):

    date = callback.data.replace(
        "schedule_",
        ""
    )

    bookings = get_bookings_by_date(date)

    free_slots = get_free_slots(date)

    beautiful_date = format_date_title(date)

    text = f"📅 {beautiful_date}\n\n"

    if bookings:

        text += "🔴 Занято:\n"

        for booking in bookings:

            text += (
                f"{booking['start']} - "
                f"{booking['end']}\n"
            )

            if booking["comment"]:

                text += (
                    f"🎉 {booking['comment']}\n"
                )

        text += "\n"

    else:

        text += (
            "🟢 Аренд нет\n\n"
        )

    text += "🟢 Свободно:\n"

    for slot in free_slots:

        text += (
            f"{slot['start']} - "
            f"{slot['end']}\n"
        )

    text += f"\n{BOOKING_TEXT}"

    await callback.message.edit_text(
        text,
        reply_markup=get_schedule_keyboard()
    )