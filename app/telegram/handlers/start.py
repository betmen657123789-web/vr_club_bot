from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.telegram.keyboards.main_menu import main_menu
from app.telegram.utils.banner import (
    send_banner
)


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await send_banner(
        message=message,
        text="🎮 Добро пожаловать в VR клуб Nexus Prime",
        keyboard=main_menu
    )