import asyncio
from telegram.handlers import prices
from telegram.bot import bot, dp
from telegram.handlers.about import router as about_router

dp.include_router(prices.router)
dp.include_router(about_router)

async def main():
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
