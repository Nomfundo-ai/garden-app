# garden_advice.py
# A small script that gives gardening tips based on the month and the season.

# TODO: Add documentation (module + function docstrings, comments) explaining
# what this script does and how each part works.

MONTHLY_ADVICE = {
    "January": "Prune roses and fruit trees while they are dormant.",
    "July": "Protect tender plants from frost and reduce watering frequency.",
    "December": "Plant heat-tolerant vegetables like tomatoes and peppers.",
}

SEASONAL_ADVICE = {
    "Winter": "Water less frequently and watch out for frost damage.",
    "Summer": "Water early in the morning to reduce evaporation.",
    "Spring": "Start seedlings indoors and prepare garden beds.",
    "Autumn": "Clear fallen leaves and plant spring-flowering bulbs.",
}


def get_monthly_advice(month):
    return MONTHLY_ADVICE.get(month, "Check your local gardening calendar for advice this month.")


def get_seasonal_advice(season):
    return SEASONAL_ADVICE.get(season, "Season not recognised.")


def main():
    month = "July"
    season = "Winter"

    print(get_monthly_advice(month))
    print(get_seasonal_advice(season))


if __name__ == "__main__":
    main()
