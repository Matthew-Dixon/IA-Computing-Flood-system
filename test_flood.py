from floodsystem.flood import stations_level_over_threshold,stations_highest_rel_level

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)

    tol = 0.8

    x = stations_level_over_threshold(stations, tol)

    assert type(x) is list

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    N=12
    x = stations_highest_rel_level(stations,N)
    assert type(x) is list
    assert len(x) == N
    assert x[0].relative_water_level() >= x[1].relative_water_level()
