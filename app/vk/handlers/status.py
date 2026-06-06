from vkbottle.bot import BotLabeler, Message

from app.services.status_service import (
    get_club_status_text
)

labeler = BotLabeler()


labeler = BotLabeler()


@labeler.message(text="🟢 Свободно ли сейчас")
async def status_handler(message: Message):

    await message.answer("Клуб открыт ✅")