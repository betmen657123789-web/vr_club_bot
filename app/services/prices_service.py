from app.services.google_sheets import (
    get_price_records,
    get_games_records
)


def get_prices_by_category(category):

    return [
        row
        for row in get_price_records()
        if row["category"] == category
    ]


def get_games_by_type(game_type):

    return [
        row
        for row in get_games_records()
        if row["type"] == game_type
    ]


def get_coop_games(game_type):

    return [
        row
        for row in get_games_records()
        if (
            row["type"] == game_type
            and row["coop"] == "Да"
        )
    ]