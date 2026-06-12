from pathlib import Path
from aiogram.types import FSInputFile, InputMediaPhoto

# нормальный путь от файла utils/banner.py
BASE_DIR = Path(__file__).resolve().parents[2]
PHOTO_DIR = BASE_DIR / "photos"
DEFAULT_BANNER = PHOTO_DIR / "banner.png"


async def send_banner(message, text, keyboard=None, photo_path=None):
    # fallback путь
    if photo_path is None:
        photo_path = DEFAULT_BANNER

    photo_path = Path(photo_path)

    # защита от отсутствующего файла
    if not photo_path.exists():
        photo_path = DEFAULT_BANNER

    photo = FSInputFile(str(photo_path))

    media = InputMediaPhoto(
        media=photo,
        caption=text
    )

    try:
        # пробуем обновить текущее фото-сообщение
        await message.edit_media(
            media=media,
            reply_markup=keyboard
        )
        return

    except Exception:
        pass

    # fallback (если сообщение не редактируется)
    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=keyboard
    )