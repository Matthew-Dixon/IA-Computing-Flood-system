from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

def task2B():
    stations = build_station_list()
    update_water_levels(stations)

    tol = 0.8

    output = stations_level_over_threshold(stations, tol)
    
    print("Task 2B")
    for i in output:
        print(f"{i[0].name} {i[1]}")
    

task2B()


