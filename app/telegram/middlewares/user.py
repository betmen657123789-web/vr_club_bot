from aiogram import BaseMiddleware
from aiogram.types import Message
from datetime import datetime

from sqlalchemy import select

from app.database.session import async_session
from app.database.models.user import User


class UserMiddleware(BaseMiddleware):

    async def __call__(self, handler, event, data):

        if not isinstance(event, Message):
            return await handler(event, data)

        message = event
        user = message.from_user

        print("MIDDLEWARE WORKS:", user.id)

        async with async_session() as session:

            # 🔥 ВАЖНО: используем SELECT вместо get()
            result = await session.execute(
                select(User).where(User.telegram_id == user.id)
            )

            db_user = result.scalar_one_or_none()

            if db_user is None:
                db_user = User(
                    telegram_id=user.id,
                    username=user.username,
                    first_name=user.first_name,
                    registered_at=datetime.utcnow(),
                    last_activity=datetime.utcnow(),
                    messages_count=1
                )
                session.add(db_user)

            else:
                db_user.last_activity = datetime.utcnow()
                db_user.messages_count = (db_user.messages_count or 0) + 1

            await session.commit()
            await session.flush()  # 🔥 фикс для SQLite

        return await handler(event, data)