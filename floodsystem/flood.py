"""This module contains a collection of functions related to
flooding.

"""
from .utils import sorted_by_key
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    lst = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            if station.relative_water_level() > tol:
                lst.append((station, station.relative_water_level()))
            else:
                pass

    return sorted_by_key(lst, 1, reverse=True)

