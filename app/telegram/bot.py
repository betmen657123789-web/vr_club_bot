from aiogram import Bot, Dispatcher

from app.core.config import BOT_TOKEN

from app.telegram.handlers.start import router as start_router
from app.telegram.handlers.status import router as status_router
from app.telegram.handlers.schedule import router as schedule_router
from app.telegram.handlers.booking import router as booking_router
from app.telegram.handlers.faq import router as faq_router
from app.telegram.handlers.admin import router as admin_router  # 👈 добавил
from app.telegram.handlers.users import router as users_router

from app.telegram.middlewares.user import UserMiddleware  # 👈 если есть middleware


# bot
bot = Bot(token=BOT_TOKEN)

# dispatcher
dp = Dispatcher()

# middleware (ВАЖНО: если используешь трекинг пользователей)
dp.message.middleware(UserMiddleware())


# routers
dp.include_router(users_router)
dp.include_router(schedule_router)
dp.include_router(start_router)
dp.include_router(status_router)
dp.include_router(booking_router)
dp.include_router(faq_router)
dp.include_router(admin_router)
