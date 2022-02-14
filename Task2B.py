from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

def task2B(stations,tol):
    update_water_levels(stations)
    output = stations_level_over_threshold(stations, tol)
    print(output)
    print('\nTask 2B:\n', f"{output[0].name} {output[1]}")
    

#task2B(build_station_list(), 0.8)

station = build_station_list()
for i in station:
    print(i.relative_water_level())