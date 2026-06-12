import asyncio

from app.telegram.bot import bot, dp

from app.telegram.handlers import prices
from app.telegram.handlers.about import router as about_router

from app.database.base import Base
from app.database.session import engine

# Важно: импортируем модели, чтобы SQLAlchemy их увидел
from app.database.models.user import User


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():

    # Создаём таблицы если их нет
    await create_tables()

    # Подключаем роутеры
    dp.include_router(prices.router)
    dp.include_router(about_router)

    print("Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())