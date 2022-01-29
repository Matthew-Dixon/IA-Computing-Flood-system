from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station

def task1Da(stations):
    lst = rivers_with_station(stations)

    print(f"Rivers with at least 1 monitoring station: {len(lst)}")
    print(f"First 10 rivers: {sorted(lst)[:10]}")


task1Da(build_station_list())

def task1Db(stations):
    dict = stations_by_river(stations)
    print(sorted(dict.get("River Aire")))
    print(sorted(dict.get("River Cam")))
    print(sorted(dict.get("River Thames")))


task1Db(build_station_list())
print(sorted(stations_by_river(build_station_list())))