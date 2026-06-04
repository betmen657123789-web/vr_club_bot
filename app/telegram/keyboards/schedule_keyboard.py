

import pytz


timezone = pytz.timezone("Asia/Irkutsk")


from datetime import datetime, timedelta
import pytz

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

timezone = pytz.timezone("Asia/Irkutsk")


MONTHS = {
    1: "янв", 2: "фев", 3: "мар",
    4: "апр", 5: "мая", 6: "июн",
    7: "июл", 8: "авг", 9: "сен",
    10: "окт", 11: "ноя", 12: "дек"
}


def format_date(date):
    return f"{date.day} {MONTHS[date.month]}"


def get_schedule_keyboard():

    now = datetime.now(timezone)

    today = now.date()
    tomorrow = today + timedelta(days=1)

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📅 Сегодня",
                    callback_data=f"schedule_{today.strftime('%d.%m.%Y')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📅 Завтра",
                    callback_data=f"schedule_{tomorrow.strftime('%d.%m.%Y')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📅 Выбрать дату",
                    callback_data="open_calendar"
                )
            ]
        ]
    )

    return keyboard


def get_calendar_keyboard():

    now = datetime.now(timezone)
    today = now.date()

    buttons = []

    for i in range(14):

        date = today + timedelta(days=i)

        buttons.append(
            InlineKeyboardButton(
                text=f"📅 {format_date(date)}",
                callback_data=f"schedule_{date.strftime('%d.%m.%Y')}"
            )
        )

    keyboard = []

    for i in range(0, len(buttons), 2):
        keyboard.append(buttons[i:i+2])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)