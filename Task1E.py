from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
def task1E():
    
    stations = build_station_list()
    list=rivers_by_station_number(stations, 7)
    print(list)


task1E()
