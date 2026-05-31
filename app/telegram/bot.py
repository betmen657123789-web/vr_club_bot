from aiogram import Bot
from aiogram import Dispatcher

from app.core.config import BOT_TOKEN

from app.telegram.handlers.start import (
    router as start_router
)

from app.telegram.handlers.status import (
    router as status_router
)

from app.telegram.handlers.schedule import (
    router as schedule_router
)
from app.telegram.handlers.booking import (
    router as booking_router
)
from app.telegram.handlers.faq import (
    router as faq_router
)


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()
dp.include_router(schedule_router)
dp.include_router(start_router)
dp.include_router(status_router)
dp.include_router(booking_router)
dp.include_router(faq_router)