from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()


@labeler.message(text="❓ FAQ")
async def faq_handler(message: Message):

    await message.answer(
        """
❓ Частые вопросы

• Можно ли со своей едой? Да

• Есть ли парковка? Да

• Сколько человек помещается?
До 10 человек
"""
    )