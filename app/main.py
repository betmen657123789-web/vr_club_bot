import asyncio

from app.telegram.bot import bot, dp

from app.telegram.handlers import prices
from app.telegram.handlers.about import router as about_router


async def main():

    # подключаем доп. роутеры (которые не подключены в bot.py)
    dp.include_router(prices.router)
    dp.include_router(about_router)

    print("Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())