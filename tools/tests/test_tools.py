import sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]  # .../final-group26
sys.path.insert(0, str(ROOT))
from tools.tools import time_of_day

def test_time_of_day_basic():
    assert time_of_day(0) == "Night (00–05)"
    assert time_of_day(5) == "Night (00–05)"
    assert time_of_day(6) == "Morning (06–11)"
    assert time_of_day(11) == "Morning (06–11)"
    assert time_of_day(12) == "Afternoon (12–17)"
    assert time_of_day(17) == "Afternoon (12–17)"
    assert time_of_day(18) == "Evening (18–23)"
    assert time_of_day(23) == "Evening (18–23)"


def test_time_of_day_nan():
    assert time_of_day(np.nan) == "Unknown"