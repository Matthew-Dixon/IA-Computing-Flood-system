# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


# Task 1B
import math

from haversine import haversine


"""
def haversine(lon1, lat1, lon2, lat2):

    # convert decimal degrees to radians 
    lon1 = math.radians(lon1)
    lat1 = math.radians(lat1)
    lon2 = math.radians(lon2)
    lat2 = math.radians(lat2)

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 
    return c * r
"""

def stations_by_distance(stations, p):
    lst = []
    for station in stations:
        distance = haversine(station.coord[0], station.coord[1], p[0], p[1])
        lst.append((station, distance))

    return sorted_by_key(lst, 1)

# Task 1C

def stations_within_radius(stations, centre, r):
    lst = []
    for station in stations:
        distance = haversine(station.coord[0], station.coord[1], centre[0], centre[1])
        if distance <= r:
            lst.append(station)
    
    return lst


# Task 1D

def rivers_with_station(stations):
    lst = []
    for i in stations:
        if i.river in lst: 
            pass
        else:
            lst.append(i.river)
    
    return lst


def stations_by_river(stations):
    dict = {}
    rivers = rivers_with_station(stations)
    lst = []
    
    for river in rivers:
        for station in stations:
            if river == station.river:
                if river not in dict.keys():
                    dict[river] = [station] 
                else:
                    for j in dict[river]:
                        lst.append(j)
                    lst.append(station) 
                    dict[river] = lst
                    lst = []
            else:
                pass
    
    return dict

