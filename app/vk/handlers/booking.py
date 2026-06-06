from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()


@labeler.message(text="📞 Забронировать")
async def booking_handler(message: Message):

    await message.answer(
        """
📞 Для бронирования:

☎️ +7 XXX XXX XX XX

или напишите администратору.
"""
    )