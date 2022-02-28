"""This module contains a collection of functions related to
plotting data.

"""

import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta 
from .analysis import polyfit

from .datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels, color="b", label="Water level")
    plt.axhline(y = station.typical_range[0], color="g", label="Typical low")
    plt.axhline(y = station.typical_range[1], color="r", label="Typical high")

    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.xticks(rotation=90)
    plt.title(station.name)

    plt.legend()
    plt.show()

def plot_water_levels_with_fit(station, dates, levels, p):

    plt.plot(dates, levels, color="b", label="Relative Water level")
    (poly,d0)= polyfit(dates, levels, p)
    plevels= poly(matplotlib.dates.date2num(dates)-d0)
    plt.plot(dates, plevels, color="r", label="Polynomial fit")

    plt.xlabel("Date")
    plt.ylabel("Relative Water level")
    plt.xticks(rotation=90)
    plt.title(station.name)

    plt.legend()
    plt.show()