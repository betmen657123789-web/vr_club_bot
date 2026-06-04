from aiogram.types import (
    InputMediaPhoto,
    FSInputFile,
    Message,
)

async def send_banner(
    message: Message,
    text: str,
    keyboard=None,
    photo_path: str = "photos/banner.png"
):

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