from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def task1C(stations, centre, r):
    lst = []
    lst1 = stations_within_radius(stations, centre, r)
    for i in lst1:
        lst.append(i.name)
    
    print(sorted(lst))




centre = (52.2053, 0.1218)
r = 10

task1C(build_station_list(), centre, r)