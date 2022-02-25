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

def stations_highest_rel_level(stations, N):

    '''Returns a list of N stations with the highest relative
    water level, sorted into descending order '''

    list = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            list.append((station, station.relative_water_level()))
            
    sortedlist = sorted_by_key(list, 1, reverse=True)
    return [item[0] for item in sortedlist[0:N]]
            