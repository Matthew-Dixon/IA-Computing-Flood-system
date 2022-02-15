"""This module contains a collection of functions related to
plotting data.

"""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta 

from .datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels, color="b")
    plt.axhline(y = station.typical_range[0], color="g")
    plt.axhline(y = station.typical_range[1], color="r")

    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.xticks(rotation=90)
    plt.title(station.name)

    plt.show()