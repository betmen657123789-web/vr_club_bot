from datetime import datetime, timedelta

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

import pytz


timezone = pytz.timezone("Asia/Irkutsk")


MONTHS = {
    1: "янв",
    2: "фев",
    3: "мар",
    4: "апр",
    5: "мая",
    6: "июн",
    7: "июл",
    8: "авг",
    9: "сен",
    10: "окт",
    11: "ноя",
    12: "дек"
}


def format_date(date):

    return (
        f"{date.day} "
        f"{MONTHS[date.month]}"
    )


def get_schedule_keyboard():

    now = datetime.now(timezone)

    today = now.date()
    tomorrow = today + timedelta(days=1)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📅 Сегодня",
                    callback_data=f"schedule_{today}"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📅 Завтра",
                    callback_data=f"schedule_{tomorrow}"
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

    keyboard = []

    dates = []

    for i in range(14):

        date = today + timedelta(days=i)

        beautiful_date = format_date(date)

        dates.append(
            InlineKeyboardButton(
                text=f"📅 {beautiful_date}",
                callback_data=f"schedule_{date}"
            )
        )

    for i in range(0, len(dates), 2):

        keyboard.append(dates[i:i + 2])

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )