from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station

def task1Da(stations):
    lst = rivers_with_station(stations)

    print(f"\nTask1D:\nRivers with at least 1 monitoring station: {len(lst)}")
    print(f"First 10 rivers: {sorted(lst)[:10]}")


task1Da(build_station_list())


def task1Db(stations):
    dict = stations_by_river(stations)
    river_aire = []
    river_cam = []
    river_thames = []

    # River Aire
    for i in dict.get("River Aire"):
        river_aire.append(i.name)
    
    # River Cam
    for j in dict.get("River Cam"):
        river_cam.append(j.name)
    
    for k in dict.get("River Thames"):
        river_thames.append(k.name)


    print(sorted(river_aire))
    print(sorted(river_cam))
    print(sorted(river_thames))


task1Db(build_station_list())
