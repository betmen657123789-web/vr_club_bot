from pathlib import Path

import gspread
import time


BASE_DIR = Path(__file__).resolve().parent.parent.parent
records_cache = []


last_update = 0
faq_cache = []

faq_last_update = 0
games_cache = []

games_last_update = 0
prices_cache = []

prices_last_update = 0

CREDENTIALS_PATH = (
    BASE_DIR
    / "credentials"
    / "vr-club-bot-fb77cb3dd2a8.json"
)


# Подключение ОДИН раз

gc = gspread.service_account(
    filename=str(CREDENTIALS_PATH)
)

spreadsheet = gc.open_by_key(
    "1Pb-k_HK6hyeuVwXPXx82zQul-e9SRt-5BRhe39hIaPk"
)

main_sheet = spreadsheet.sheet1

faq_sheet = spreadsheet.get_worksheet(2)

price_sheet = spreadsheet.get_worksheet(1)

games_sheet = spreadsheet.get_worksheet(3)


# Основная таблица

def get_price_records():

    global prices_cache
    global prices_last_update

    now = time.time()

    if now - prices_last_update > 60:

        print("Обновляем Games Sheets")

        prices_cache = (
            price_sheet.get_all_records()
        )

        prices_last_update = now

    return prices_cache

def get_games_records():

    global games_cache
    global games_last_update

    now = time.time()

    if now - games_last_update > 60:

        print("Обновляем Games Sheets")

        games_cache = (
            games_sheet.get_all_records()
        )

        games_last_update = now

    return games_cache

def get_all_records():

    global records_cache
    global last_update

    now = time.time()

    # обновляем раз в 60 секунд
    if now - last_update > 60:

        print("Обновляем Google Sheets")

        records_cache = (
            main_sheet.get_all_records()
        )

        last_update = now

    return records_cache


# FAQ

def get_faq_records():

    global faq_cache
    global faq_last_update

    now = time.time()

    # обновляем FAQ раз в 60 секунд
    if now - faq_last_update > 60:

        print("Обновляем FAQ Sheets")

        start = time.time()

        faq_cache = (
            faq_sheet.get_all_records()
        )

        end = time.time()

        print(
            f"FAQ Sheets: {end - start}"
        )

        faq_last_update = now

    return faq_cache