from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

centre = (52.2053, 0.1218)
r = 10
print(stations_within_radius(build_station_list, centre, r))