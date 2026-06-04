
from aiogram import Router, F
from aiogram.types import Message
from app.services.status_service import (
    get_club_status_text
)
from app.telegram.utils.banner import send_banner


router = Router()



@router.message(lambda message: message.text == "🟢 Свободно ли сейчас")
async def status_handler(message: Message):

    print("STATUS CLICKED")

    text = get_club_status_text()

    await send_banner(
        message,
        text
    )