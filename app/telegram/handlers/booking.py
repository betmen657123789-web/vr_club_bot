from aiogram import Router
from aiogram.types import (
    Message,
    CallbackQuery
)

from app.content.contacts import (
    BOOKING_TEXT
)

from app.telegram.keyboards.schedule_keyboard import (
    get_schedule_keyboard
)

router = Router()


@router.message(
    lambda message:
    message.text == "📞 Забронировать"
)
async def booking_handler(message: Message):

    await message.answer(
        "📅 Выберите дату:",
        reply_markup=get_schedule_keyboard()
    )


@router.callback_query(
    lambda callback:
    callback.data == "booking_menu"
)
async def booking_callback(
    callback: CallbackQuery
):

    await callback.answer()

    if callback.message:

        await callback.message.edit_text(
            "📅 Выберите дату:",
            reply_markup=get_schedule_keyboard()
        )