"""This module contains a collection of functions related to
plotting data.

"""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta 

from .datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)

    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.xticks(rotation=45)
    plt.title("")