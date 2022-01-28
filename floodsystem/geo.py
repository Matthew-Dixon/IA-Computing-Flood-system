# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

import haversine 

def stations_by_distance(stations, p):
    list = []
    for station in stations:
        distance = haversine(station, p)
        list.append(tuple(station, distance))

    return sorted_by_key(list, 1)
