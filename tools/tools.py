import pandas as pd
import re


def time_of_day(h):
    """
    Map hour-of-day to time-of-day category.

    Parameters
    ----------
    h : int or float
        Hour in [0, 23]. May be NaN.

    Returns
    -------
    str
        Time-of-day label.
    """
    if pd.isna(h):
        return "Unknown"
    if 0 <= h < 6:
        return "Night (00–05)"
    elif 6 <= h < 12:
        return "Morning (06–11)"
    elif 12 <= h < 18:
        return "Afternoon (12–17)"
    else:
        return "Evening (18–23)"

def extract_streets(loc):
    """
    Extract street names from a location string.

    Parameters
    ----------
    loc : str or NaN
        Raw location string (e.g. 'INTERSECTION OF A ST AND B ST')

    Returns
    -------
    list of str
        Cleaned list of street names
    """
    if pd.isna(loc):
        return []

    loc = loc.upper()

    # Remove boilerplate phrases
    loc = re.sub(r"INTERSECTION OF ", "", loc)
    loc = re.sub(r" BETWEEN .*", "", loc)

    # Split on common connectors
    streets = re.split(r" AND | AT | & |/", loc)

    return [s.strip() for s in streets if s.strip()]