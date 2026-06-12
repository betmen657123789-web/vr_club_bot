from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select, func
from datetime import datetime, timedelta

from app.database.session import async_session
from app.database.models.user import User
from app.core.config import ADMIN_IDS
from aiogram import Bot

router = Router()


@router.message(Command("stats"))
async def stats(message: Message):

    if message.from_user.id not in ADMIN_IDS:
        return

    async with async_session() as session:

        total_users = await session.scalar(
            select(func.count(User.telegram_id))
        )

        active_24h = await session.scalar(
            select(func.count(User.telegram_id)).where(
                User.last_activity >= datetime.utcnow() - timedelta(days=1)
            )
        )

    await message.answer(
        f"""📊 Статистика

👥 Всего пользователей: {total_users}
🔥 Активных за 24h: {active_24h}
"""
    )
@router.message(Command("broadcast"))
async def broadcast(message: Message, bot: Bot):

    if message.from_user.id not in ADMIN_IDS:
        return

    text = message.text.replace("/broadcast", "").strip()

    if not text:
        await message.answer("Напиши текст после /broadcast")
        return

    async with async_session() as session:

        users = await session.execute(
            select(User.telegram_id)
        )

        user_ids = users.scalars().all()

    sent = 0

    for user_id in user_ids:
        try:
            await bot.send_message(user_id, text)
            sent += 1
        except:
            pass

    await message.answer(f"✅ Отправлено: {sent}")