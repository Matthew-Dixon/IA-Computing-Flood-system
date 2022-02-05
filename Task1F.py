from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
inconsistent=inconsistent_typical_range_stations(stations)
l=[]
for s in inconsistent:
    l.append(s.name)
print('\nTask1F:\nInconsistent Stations:',l)


