from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 🌍 один источник правды для таймзоны
TIMEZONE = ZoneInfo("Asia/Irkutsk")


MONTHS = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}


def now():
    return datetime.now(TIMEZONE)


def format_date(date_string: str) -> str:
    date = datetime.strptime(date_string, "%d.%m.%Y")
    return f"{date.day} {MONTHS[date.month]}"


def format_date_title(date_string: str) -> str:
    date = datetime.strptime(date_string, "%d.%m.%Y").date()
    today = now().date()

    if date == today:
        return f"Сегодня — {format_date(date_string)}"

    if date == today + timedelta(days=1):
        return f"Завтра — {format_date(date_string)}"

    return format_date(date_string)