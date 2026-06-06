import logging
from pathlib import Path

from aiogram import Router
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto

from app.telegram.keyboards.about_back_keyboard import get_about_back_keyboard
from app.telegram.keyboards.about_keyboard import get_about_keyboard
from app.telegram.utils.banner import send_banner

router = Router()
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PHOTO_DIR = PROJECT_ROOT / "photos"

# =========================
# CACHE
# =========================
PHOTO_CACHE: list[str] = []
PHOTO_MESSAGE_IDS: list[int] = []


@router.callback_query(lambda c: c.data == "club_photos")
async def club_photos(callback: CallbackQuery):
    await callback.answer()

    chat_id = callback.message.chat.id

    # =========================
    # 0. УДАЛЯЕМ СТАРЫЙ АЛЬБОМ
    # =========================
    for msg_id in PHOTO_MESSAGE_IDS:
        try:
            await callback.message.bot.delete_message(chat_id, msg_id)
        except Exception:
            pass

    PHOTO_MESSAGE_IDS.clear()

    # =========================
    # 1. MEDIA (cache / disk)
    # =========================
    if PHOTO_CACHE:
        media = [InputMediaPhoto(media=fid) for fid in PHOTO_CACHE]
    else:
        photo_paths = [
            PHOTO_DIR / "photo_2026-05-31_18-10-52.jpg",
            PHOTO_DIR / "photo_2026-06-05_22-48-51.jpg",
            PHOTO_DIR / "photo_2026-06-05_22-45-11.jpg",
            PHOTO_DIR / "photo_2026-06-05_22-45-12.jpg",
            PHOTO_DIR / "photo_2026-06-05_22-48-21.jpg",
        ]

        media = [
            InputMediaPhoto(media=FSInputFile(str(p)))
            for p in photo_paths
            if p.exists()
        ]

    if not media:
        await callback.message.answer("❌ Фото не найдены")
        return

    # =========================
    # 2. SEND ALBUM
    # =========================
    messages = await callback.message.bot.send_media_group(
        chat_id=chat_id,
        media=media
    )

    # =========================
    # 3. CACHE UPDATE (важно: порядок сохраняем)
    # =========================
    if not PHOTO_CACHE:
        for msg in messages:
            if msg.photo:
                PHOTO_CACHE.append(msg.photo[-1].file_id)

    PHOTO_MESSAGE_IDS.extend([m.message_id for m in messages])

    # =========================
    # 4. BACK BUTTON
    # =========================
    await callback.message.answer(
        "Вернуться в меню клуба:",
        reply_markup=get_about_back_keyboard()
    )


# =========================
# 🔙 BACK (как в расписании)
# =========================
@router.callback_query(lambda c: c.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery):
    await callback.answer()

    chat_id = callback.message.chat.id

    # удаляем альбом
    for msg_id in PHOTO_MESSAGE_IDS:
        try:
            await callback.message.bot.delete_message(chat_id, msg_id)
        except Exception:
            pass

    PHOTO_MESSAGE_IDS.clear()

    await callback.message.answer(
        "🏠 VR CLUB",
        reply_markup=get_about_keyboard()
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