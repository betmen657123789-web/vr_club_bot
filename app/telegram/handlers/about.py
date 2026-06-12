import logging
from pathlib import Path

from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    FSInputFile,
    InputMediaPhoto,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from app.telegram.keyboards.about_keyboard import get_about_keyboard

logger = logging.getLogger(__name__)
router = Router()

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PHOTO_DIR = PROJECT_ROOT / "photos"

BANNER_PATH = PHOTO_DIR / "banner.png"


# =========================
# SAFE UI ENTRY
# =========================
async def open_about_ui(message, text, keyboard):
    photo = FSInputFile(str(BANNER_PATH))

    try:
        await message.edit_media(
            media=InputMediaPhoto(
                media=photo,
                caption=text
            ),
            reply_markup=keyboard
        )
    except Exception:
        await message.answer_photo(
            photo=photo,
            caption=text,
            reply_markup=keyboard
        )


# =========================
# PHOTOS
# =========================
PHOTO_FILES = [
    PHOTO_DIR / "photo_2026-05-31_18-10-52.jpg",
    PHOTO_DIR / "photo_2026-06-05_22-48-51.jpg",
    PHOTO_DIR / "photo_2026-06-05_22-45-11.jpg",
    PHOTO_DIR / "photo_2026-06-05_22-45-12.jpg",
    PHOTO_DIR / "photo_2026-06-05_22-48-21.jpg",
]


# =========================
# ABOUT MENU
# =========================
@router.callback_query(F.data == "about_menu")
async def about_menu(callback: CallbackQuery):
    await callback.answer()

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
        "Можно разместить больше 10 гостей — в этом случае\n"
        "добавляется доплата за каждого дополнительного человека.\n\n"
        "🍕 Можно со своей едой и напитками\n\n"
        "🎂 Проводим дни рождения и мероприятия\n"
    )

    await open_about_ui(callback.message, text, get_about_keyboard())


# =========================
# MAP KEYBOARD (FIXED)
# =========================
def get_map_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔙 Назад",
                    callback_data="about_menu"
                )
            ]
        ]
    )


# =========================
# HOW TO GET THERE
# =========================
@router.callback_query(F.data == "club_map")
async def club_map(callback: CallbackQuery):
    await callback.answer()

    text = (
        "📍 Адрес:\n\n"
        "Култукский тракт, 14а, Шелехов\n\n"
        "🚗 Есть бесплатная парковка\n\n"
        "🗺 2ГИС:\n"
        "https://2gis.ru/shelekhov/firm/70000001075771850"
    )

    await open_about_ui(callback.message, text, get_map_keyboard())


# =========================
# OPEN GALLERY
# =========================
@router.callback_query(F.data == "club_photos")
async def open_gallery(callback: CallbackQuery):
    await callback.answer()

    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(str(PHOTO_FILES[0])),
            caption=f"📸 Фото клуба (1/{len(PHOTO_FILES)})"
        ),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="◀️",
                        callback_data="photo_0"
                    ),
                    InlineKeyboardButton(
                        text="▶️",
                        callback_data="photo_1"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🔙 Назад",
                        callback_data="about_menu"
                    )
                ]
            ]
        )
    )


# =========================
# SWITCH PHOTO
# =========================
@router.callback_query(F.data.startswith("photo_"))
async def switch_photo(callback: CallbackQuery):
    await callback.answer()

    index = int(callback.data.split("_")[1])

    if index < 0 or index >= len(PHOTO_FILES):
        return

    buttons = []

    row = []
    if index > 0:
        row.append(InlineKeyboardButton(text="◀️", callback_data=f"photo_{index - 1}"))
    if index < len(PHOTO_FILES) - 1:
        row.append(InlineKeyboardButton(text="▶️", callback_data=f"photo_{index + 1}"))

    if row:
        buttons.append(row)

    buttons.append([
        InlineKeyboardButton(text="🔙 Назад", callback_data="about_menu")
    ])

    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(str(PHOTO_FILES[index])),
            caption=f"📸 Фото клуба ({index + 1}/{len(PHOTO_FILES)})"
        ),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )


# =========================
# TEXT ENTRY (fallback)
# =========================
@router.message(F.text == "ℹ️ О клубе")
async def about_menu_message(message: Message):
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
        "Можно разместить больше 10 гостей — в этом случае\n"
        "добавляется доплата за каждого дополнительного человека.\n\n"
        "🍕 Можно со своей едой и напитками\n\n"
        "🎂 Проводим дни рождения и мероприятия\n"
    )

    await open_about_ui(message, text, get_about_keyboard())