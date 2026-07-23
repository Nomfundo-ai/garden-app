# garden_advice.py
# A small script that gives gardening tips based on the month and the season.

# TODO: Replace this hardcoded month/season data with proper functions so this
# logic can be reused and tested, instead of running top-to-bottom as a script.
# TODO: Add documentation (module + function docstrings, comments) explaining
# what this script does and how each part works.

month = "July"
season = "Winter"

if month == "January":
    print("Prune roses and fruit trees while they are dormant.")
elif month == "July":
    print("Protect tender plants from frost and reduce watering frequency.")
elif month == "December":
    print("Plant heat-tolerant vegetables like tomatoes and peppers.")
else:
    print("Check your local gardening calendar for advice this month.")

if season == "Winter":
    print("Water less frequently and watch out for frost damage.")
elif season == "Summer":
    print("Water early in the morning to reduce evaporation.")
elif season == "Spring":
    print("Start seedlings indoors and prepare garden beds.")
elif season == "Autumn":
    print("Clear fallen leaves and plant spring-flowering bulbs.")
else:
    print("Season not recognised.")
