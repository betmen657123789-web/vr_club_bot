from aiogram import Router
from aiogram.types import (
    Message,
    CallbackQuery
)

from app.telegram.keyboards.prices_keyboard import (
    get_prices_keyboard
)
from app.services.prices_service import (
    get_prices_by_category,
    get_games_by_type,
    get_coop_games
)

from app.telegram.keyboards.price_card_keyboard import (
    get_price_card_keyboard
)
from app.telegram.keyboards.games_back_keyboard import (
    get_games_back_keyboard
)
from app.telegram.keyboards.event_card_keyboard import (
    get_event_card_keyboard
)

router = Router()


@router.message(
    lambda message:
    message.text == "💰 Цены"
)
async def prices_menu(
    message: Message
):

    await message.answer(
        "💰 Выберите услугу:",
        reply_markup=get_prices_keyboard()
    )
@router.callback_query(
    lambda callback:
    callback.data == "price_ps"
)
async def ps_card(
    callback: CallbackQuery
):

    await callback.answer()

    prices = get_prices_by_category("PS")
    games = get_games_by_type("PS")
    coop_games = get_coop_games("PS")

    text = "🎮 PlayStation\n\n"

    text += "💰 Цены\n\n"

    for price in prices:
        text += (
            f"{price['name']} — "
            f"{price['price']} ₽\n"
        )

    text += "\n🎮 Игры\n\n"

    for game in games[:5]:
        text += f"• {game['title']}\n"

    text += "\n👥 Для игры вдвоём\n\n"

    for game in coop_games[:3]:
        text += (
            f"• {game['title']}\n"
        )

    remaining = len(coop_games) - 3

    if remaining > 0:
        text += (
            f"\nИ ещё {remaining} игр..."
        )

    await callback.message.edit_text(
        text,
        reply_markup=get_price_card_keyboard("PS")
    )

@router.callback_query(
    lambda callback:
    callback.data == "price_vr"
)
async def vr_card(
    callback: CallbackQuery
):
        await callback.answer()

        prices = get_prices_by_category("VR")

        games = get_games_by_type("VR")

        coop_games = get_coop_games("VR")

        text = "🥽 VR-шлемы\n\n"

        text += "💰 Цены\n\n"

        for price in prices:
            text += (
                f"{price['name']} — "
                f"{price['price']} ₽\n"
            )

        text += "\n🎮 Игры\n\n"

        for game in games[:5]:
            text += f"• {game['title']}\n"

        text += "\n👥 Кооператив\n\n"

        for game in coop_games[:3]:
            text += (
                f"• {game['title']}\n"
            )

        remaining = len(coop_games) - 3

        if remaining > 0:
            text += (
                f"\nИ ещё {remaining} игр..."
            )

        await callback.message.edit_text(
            text,
            reply_markup=get_price_card_keyboard(
                "VR"
            )
        )
@router.callback_query(
    lambda callback:
    callback.data == "prices_menu"
)
async def prices_menu_back(
    callback: CallbackQuery
):

    await callback.answer()

    await callback.message.edit_text(
        "💰 Выберите услугу:",
        reply_markup=get_prices_keyboard()
    )
@router.callback_query(
    lambda callback:
    callback.data == "price_event"
)
async def event_card(
    callback: CallbackQuery
):

    await callback.answer()

    prices = get_prices_by_category(
        "EVENT"
    )

    text = "🎉 Мероприятия\n\n"

    text += (
        "🏢 Вместимость зала: до 10 человек\n\n"
    )
    text += (
        "🏢 Дополнительный человек + 100 р\n\n"
    )

    text += "💰 Стоимость аренды\n\n"

    for price in prices:

        text += (
            f"{price['name']} — "
            f"{price['price']} ₽\n"
        )

    text += (
        "\n🍕 Можно приносить "
        "свою еду и напитки\n"
    )

    text += (
        "\n🎂 Подходит для:\n"
        "• Дней рождения\n"
        "• Корпоративов\n"
        "• Детских праздников\n"
        "• Встреч с друзьями"
    )

    await callback.message.edit_text(
        text,
        reply_markup=get_event_card_keyboard()
    )
@router.callback_query(
    lambda callback:
    callback.data == "price_extra"
)
async def extra_card(
    callback: CallbackQuery
):

    await callback.answer()

    extras = get_prices_by_category(
        "EXTRA"
    )

    text = "⭐ Дополнительные услуги\n\n"

    text += (
        "Сделайте отдых ещё комфортнее:\n\n"
    )

    for extra in extras:

        text += (
            f"• {extra['name']}"
        )

        if extra["price"]:

            text += (
                f" — {extra['price']} ₽"
            )

        text += "\n"

    await callback.message.edit_text(
        text,
        reply_markup=get_event_card_keyboard()
    )
@router.callback_query(
    lambda callback:
    callback.data.startswith(
        "all_games_"
    )
)
async def all_games(
    callback: CallbackQuery
):

    await callback.answer()

    game_type = (
        callback.data.replace(
            "all_games_",
            ""
        )
    )

    games = get_games_by_type(
        game_type
    )

    title = (
        "🎮 Все игры PlayStation"
        if game_type == "PS"
        else "🥽 Все VR игры"
    )

    text = f"{title}\n\n"

    for game in games:
        text += (
            f"• {game['title']}\n"
        )

    await callback.message.edit_text(
        text,
        reply_markup=get_games_back_keyboard(
            game_type
        )
    )

