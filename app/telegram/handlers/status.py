from aiogram import Router
from aiogram.types import Message

from app.services.status_service import (
    get_club_status_text
)


router = Router()


@router.message(
    lambda message:
    message.text == "🟢 Свободно ли сейчас"
)
async def status_handler(message: Message):

    text = get_club_status_text()

    await message.answer(text)