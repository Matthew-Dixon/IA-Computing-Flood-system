from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def test_stations_by_distance():
    stations = build_station_list()
    x = stations_by_distance(stations, (52.2053,0.1218))

    assert type(x) is list

def test_stations_within_radius():
    stations = build_station_list()
    x = stations_within_radius(stations, (52.2053, 0.1218), 10) 
    
    assert type(x) is list 

    y = stations_within_radius(stations, (52.2053, 0.1218), 0) 

    assert len(y) == 0

def test_rivers_with_stations():
    stations = build_station_list()
    x = rivers_with_station(stations) 

    assert type(x) is list 

def test_stations_by_river():
    stations = build_station_list()
    x = stations_by_river(stations) 

    assert type(x) is dict