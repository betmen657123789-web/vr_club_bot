from app.services.schedule_service import (
    check_current_status,
    get_next_booking,
    is_day_fully_free,
    had_bookings_today,
)


def get_club_status_text():

    current_status = check_current_status()

    if current_status["is_busy"]:

        return (
            "🔴 Сейчас идёт аренда\n\n"
            f"Клуб освободится:\n"
            f"в {current_status['end_time']}"
        )

    next_booking = get_next_booking()

    if next_booking:

        return (
            "🟢 Сейчас клуб свободен\n\n"
            f"Следующая аренда:\n"
            f"в {next_booking['Начало']}"
        )

    if is_day_fully_free():

        return (
            "🟢 Сегодня клуб свободен весь день\n\n"
            "Можно приходить 🎮"
        )

    if had_bookings_today():

        return (
            "🟢 Сейчас клуб свободен\n\n"
            "На сегодня аренды закончились 🎮"
        )

    return (
        "🟢 Сейчас клуб свободен"
    )