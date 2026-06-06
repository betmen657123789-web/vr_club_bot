import logging

from aiogram import Router
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto

from app.telegram.keyboards.about_back_keyboard import get_about_back_keyboard
from app.telegram.keyboards.about_keyboard import get_about_keyboard
from app.telegram.utils.banner import send_banner
from pathlib import Path


router = Router()
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parents[2]
@router.callback_query(lambda callback: callback.data == "club_photos")
async def club_photos(callback: CallbackQuery):
    logger.info("Callback: club_photos triggered")

    await callback.answer()


    photo_paths = [
         BASE_DIR / "photos" / "photo_2026-05-31_18-10-52.jpg",
        BASE_DIR / "photos" / "photo_2026-06-05_22-48-51.jpg",
        BASE_DIR / "photos" / "photo_2026-06-05_22-45-11.jpg",
        BASE_DIR / "photos" / "photo_2026-06-05_22-45-12.jpg",
        BASE_DIR / "photos" / "photo_2026-06-05_22-48-21.jpg",

    ]

    media = []

    for path in photo_paths:
        if not path.exists():
            logger.error("Missing file: %s", path)
            continue

        media.append(InputMediaPhoto(media=FSInputFile(str(path))))
    if len(media) < 2:
        await callback.message.answer("❌ Фото не найдены на сервере")
        return

    logger.info("Sending media group with %s photos", len(media))

    await callback.message.answer_media_group(media)

    await callback.message.answer(
        "⬇️ Вернуться в меню клуба:",
        reply_markup=get_about_back_keyboard()
    )


@router.callback_query(lambda callback: callback.data == "club_map")
async def club_map(callback: CallbackQuery):
    logger.info("Callback: club_map triggered")

    await callback.answer()

    text = (
        "📍 Адрес:\n"
        "Култукский тракт, 14а, Шелехов\n\n"
        "🚗 Есть бесплатная парковка\n\n"
        "🗺 2ГИС:\n"
        "https://2gis.ru/shelekhov/firm/70000001075771850"
    )

    await send_banner(
        callback.message,
        text,
        get_about_back_keyboard()
    )


@router.message(lambda message: message.text == "ℹ️ О клубе")
async def about_menu(message: Message):
    logger.info("Message: about menu opened")

    text = (
        "🏠 VR CLUB\n\n"
        "📍 Адрес:\n"
        "Култукский тракт, 14а, Шелехов\n\n"
        "🕐 Работаем ежедневно:\n"
        "12:00–21:00\n\n"
        "🚗 Парковка:\n"
        "есть бесплатная парковка\n\n"
        "👥 Вместимость:\n"
        "Оптимально — до 10 человек\n"
        "Комфортная рассадка:\n"
        "• 3 PS-зоны (1 зона = 3 игрока, комфортно — 2)\n"
        "• 4 VR-шлема (1 игрок = 1 шлем)\n"
        "Можно разместить больше 10 гостей — в этом случае добавляется доплата за каждого дополнительного человека.\n\n"
        "🍕 Можно со своей едой и напитками\n\n"
        "🎂 Проводим дни рождения и мероприятия"
    )

    await send_banner(
        message,
        text,
        get_about_keyboard()
    )


@router.callback_query(lambda callback: callback.data == "about_menu")
async def about_menu_callback(callback: CallbackQuery):
    logger.info("Callback: about_menu opened")

    await callback.answer()

    text = (
        "🏠 VR CLUB\n\n"
        "📍 Адрес:\n"
        "Култукский тракт, 14а, Шелехов\n\n"
        "🕐 Работаем ежедневно:\n"
        "13:00–20:00\n\n"
        "🚗 Парковка:\n"
        "есть бесплатная парковка\n\n"
        "👥 Вместимость:\n"
        "до 10 человек\n\n"
        "🍕 Можно со своей едой и напитками\n\n"
        "🎂 Проводим дни рождения и мероприятия"
    )

    await send_banner(
        callback.message,
        text,
        get_about_keyboard()
    )