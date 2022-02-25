from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

list=stations_highest_rel_level(stations, 10)
print('Task 2C')
for i in list:
    print(i.name,' : ',i.relative_water_level())