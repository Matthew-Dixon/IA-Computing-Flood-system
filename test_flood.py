from floodsystem.flood import stations_level_over_threshold

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)

    tol = 0.8

    x = stations_level_over_threshold(stations, tol)

    assert type(x) is list