from datetime import datetime
import pytz

from app.services.google_sheets import get_all_records

WORK_START = "12:00"
WORK_END = "21:00"

timezone = pytz.timezone("Asia/Irkutsk")


def get_today_records():

    records = get_all_records()

    now = datetime.now(timezone)
    current_date = now.strftime("%d.%m.%Y")

    today_records = []

    for row in records:

        if row["Дата"] == current_date:

            today_records.append(row)

    return today_records


def check_current_status():

    records = get_today_records()

    now = datetime.now(timezone)

    current_time = now.time()

    for row in records:

        if row["Статус"] != "RENT":
            continue

        start_time = datetime.strptime(
            row["Начало"],
            "%H:%M"
        ).time()

        end_time = datetime.strptime(
            row["Конец"],
            "%H:%M"
        ).time()

        if start_time <= current_time <= end_time:

            return {
                "is_busy": True,
                "end_time": row["Конец"]
            }

    return {
        "is_busy": False
    }


def get_next_booking():

    records = get_today_records()

    now = datetime.now(timezone)

    current_time = now.time()

    future_bookings = []

    for row in records:

        if row["Статус"] != "RENT":
            continue

        start_time = datetime.strptime(
            row["Начало"],
            "%H:%M"
        ).time()

        if start_time > current_time:

            future_bookings.append(row)

    if not future_bookings:
        return None

    future_bookings.sort(
        key=lambda booking: booking["Начало"]
    )

    return future_bookings[0]


def is_day_fully_free():

    records = get_today_records()

    for row in records:

        if row["Статус"] == "RENT":
            return False

    return True


def get_today_bookings():

    records = get_today_records()

    bookings = []

    for row in records:

        if row["Статус"] != "RENT":
            continue

        bookings.append({
            "start": row["Начало"],
            "end": row["Конец"],
            "comment": row["comment"]
        })

    return bookings


def had_bookings_today():

    records = get_today_records()

    for row in records:

        if row["Статус"] == "RENT":
            return True

    return False


def get_bookings_by_date(date):

    records = get_all_records()

    bookings = []

    for row in records:

        if row["Дата"] != date:
            continue

        if row["Статус"] != "RENT":
            continue

        bookings.append({
            "start": row["Начало"],
            "end": row["Конец"],
            "comment": row["comment"]
        })

    bookings.sort(
        key=lambda booking: booking["start"]
    )

    return bookings


def get_free_slots(date):

    bookings = get_bookings_by_date(date)

    if not bookings:

        return [
            {
                "start": WORK_START,
                "end": WORK_END
            }
        ]

    free_slots = []

    current_start = WORK_START

    for booking in bookings:

        booking_start = booking["start"]
        booking_end = booking["end"]

        if current_start < booking_start:

            free_slots.append({
                "start": current_start,
                "end": booking_start
            })

        current_start = booking_end

    if current_start < WORK_END:

        free_slots.append({
            "start": current_start,
            "end": WORK_END
        })

    return free_slots