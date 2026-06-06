from vkbottle.bot import BotLabeler, Message

from app.vk.keyboards.prices_keyboard import (
    get_prices_keyboard
)

labeler = BotLabeler()


@labeler.message(text="🎮 Тарифы и услуги")
async def prices_handler(message: Message):

    await message.answer(
        "💰 Выберите услугу:",
        keyboard=get_prices_keyboard()
    )