
"""This module provides functions for analysing monitoring station level data
"""

import numpy as np
import matplotlib.dates



def polyfit(dates, levels, p):
    times = matplotlib.dates.date2num(dates)
    normalised_times= times - times[0]
    p_coeff = np.polyfit(normalised_times, levels, p)
    poly = np.poly1d(p_coeff)
    d0=times[0]
    return (poly,d0)