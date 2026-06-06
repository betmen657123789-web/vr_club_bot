from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()


@labeler.message(text="ℹ️ О клубе")
async def about_handler(message: Message):

    await message.answer(
        """
🎮 VR CLUB NEXUS

📍 Шелехов

🥽 VR Quest 3
🎮 PlayStation 5

👥 До 10 человек

🎉 Дни рождения
🎉 Корпоративы
🎉 Праздники
"""
    )