from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from sqlalchemy import select

from app.database.session import async_session
from app.database.models.user import User
from app.core.config import ADMIN_IDS

router = Router()


@router.message(Command("users"))
async def users_list(message: Message):

    if message.from_user.id not in ADMIN_IDS:
        return

    async with async_session() as session:

        result = await session.execute(
            select(User).order_by(User.registered_at.desc()).limit(10)
        )

        users = result.scalars().all()

    if not users:
        await message.answer("Пользователей нет")
        return

    text = "👥 Последние пользователи:\n\n"

    for user in users:
        text += (
            f"🆔 {user.telegram_id}\n"
            f"👤 {user.username or 'no username'}\n"
            f"📅 {user.registered_at}\n"
            f"-----------------\n"
        )

    await message.answer(text)