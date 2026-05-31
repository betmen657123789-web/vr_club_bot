from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.telegram.keyboards.main_menu import main_menu


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):

    await message.answer(
        "🎮 Добро пожаловать в VR клуб Nexus Prime",
        reply_markup=main_menu
    )