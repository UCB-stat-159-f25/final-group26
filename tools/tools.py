import pandas as pd


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