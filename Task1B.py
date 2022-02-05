from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

# Task 1B
def task1B():
    lst = stations_by_distance(build_station_list(),(52.2053,0.1218))
    station = build_station_list()
    lst_closest = []
    lst_furthest = []

    closest = lst[:10]
    furthest = lst[-10:]

    for i in closest:
        lst_closest.append((i[0].name, i[0].town, i[1]))
    for j in furthest:
        lst_furthest.append((j[0].name, j[0].town, j[1]))

    print(f"\nTask1B:\nClosest 10 stations: {lst_closest}")
    print(f"Furthest 10 stations: {lst_furthest}")

task1B()

