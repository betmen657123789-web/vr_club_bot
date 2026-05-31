from datetime import datetime
from datetime import timedelta
import pytz


timezone = pytz.timezone("Asia/Irkutsk")


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


def format_date(date_string):

    date = datetime.strptime(
        date_string,
        "%Y-%m-%d"
    )

    day = date.day

    month = MONTHS[date.month]

    return f"{day} {month}"


def format_date_title(date_string):

    date = datetime.strptime(
        date_string,
        "%Y-%m-%d"
    ).date()

    now = datetime.now(timezone).date()

    if date == now:
        return f"Сегодня — {format_date(date_string)}"

    if date == now + timedelta(days=1):
        return f"Завтра — {format_date(date_string)}"

    return format_date(date_string)