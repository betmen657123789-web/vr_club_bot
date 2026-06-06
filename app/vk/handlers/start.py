from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()

from app.vk.keyboards.main_keyboard import get_main_keyboard


@labeler.message(text=["начать", "Начать"])
async def start_handler(message: Message):

    await message.answer(
        "Главное меню",
        keyboard=get_main_keyboard()
    )