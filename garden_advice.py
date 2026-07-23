"""garden_advice.py

Gives gardening tips and advice based on the current month and season.

Part of the "garden-app" project for gardening enthusiasts: this module
looks up a short, practical tip for a given month (e.g. what to plant or
prune) and a given season (e.g. watering habits), and prints both.
"""

# Advice keyed by month name. Add more months here as the tip library grows.
MONTHLY_ADVICE = {
    "January": "Prune roses and fruit trees while they are dormant.",
    "July": "Protect tender plants from frost and reduce watering frequency.",
    "December": "Plant heat-tolerant vegetables like tomatoes and peppers.",
}

# Advice keyed by season name.
SEASONAL_ADVICE = {
    "Winter": "Water less frequently and watch out for frost damage.",
    "Summer": "Water early in the morning to reduce evaporation.",
    "Spring": "Start seedlings indoors and prepare garden beds.",
    "Autumn": "Clear fallen leaves and plant spring-flowering bulbs.",
}


def get_monthly_advice(month):
    """Return a gardening tip for the given month.

    :param month: Name of the month, e.g. "July".
    :return: A tip string, or a fallback message if the month isn't in
        MONTHLY_ADVICE yet.
    """
    return MONTHLY_ADVICE.get(month, "Check your local gardening calendar for advice this month.")


def get_seasonal_advice(season):
    """Return a gardening tip for the given season.

    :param season: Name of the season, e.g. "Winter".
    :return: A tip string, or a fallback message if the season isn't
        recognised.
    """
    return SEASONAL_ADVICE.get(season, "Season not recognised.")


def main():
    """Print gardening advice for a hardcoded month and season.

    In a future version, month/season could instead be read from the
    system date or passed in as arguments.
    """
    month = "July"
    season = "Winter"

    print(get_monthly_advice(month))
    print(get_seasonal_advice(season))


if __name__ == "__main__":
    main()
