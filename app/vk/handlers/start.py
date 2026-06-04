from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()


@labeler.message(text="Начать")
async def start_handler(message: Message):
    await message.answer(
        "Привет! Я бот VR CLUB 🎮"
    )