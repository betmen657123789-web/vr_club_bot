from aiogram.types import (
    InputMediaPhoto,
    FSInputFile,
    Message,
)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = /app/app

async def send_banner(
    message: Message,
    text: str,
    keyboard=None,
    photo_path: str = None
):
    if photo_path is None:
        photo_path = os.path.join(BASE_DIR, "photos", "banner.png")

    photo = FSInputFile(photo_path)
    media = InputMediaPhoto(
        media=photo,
        caption=text
    )

    # если сообщение уже с фото → редактируем
    try:
        await message.edit_media(
            media=media,
            reply_markup=keyboard
        )

    # если нельзя редактировать (например старое текстовое)
    except Exception:
        await message.answer_photo(
            photo=photo,
            caption=text,
            reply_markup=keyboard
        )