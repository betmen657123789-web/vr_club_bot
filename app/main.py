import asyncio
from app.telegram.handlers import prices

from app.telegram.bot import (
    bot,
    dp
)
dp.include_router(prices.router)
from app.telegram.handlers.about import (
    router as about_router
)

dp.include_router(
    about_router
)



async def main():

    print("Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())
