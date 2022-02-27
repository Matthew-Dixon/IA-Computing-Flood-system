import datetime

from numpy import empty
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib


def task2F():
    stations = build_station_list()
    print('1')
    update_water_levels(stations)
    print('2')
    stations= stations_highest_rel_level(stations, 5)

    ddays = 2 #time difference in days

    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=ddays))
        #print(dates)
        if len(dates)>1: #occasionally had odd issues arrising from the returned dates being empty
            plot_water_levels_with_fit(station, dates, levels,4)
        else:
            print('no dates returned')


task2F()



""" stations = build_station_list()
update_water_levels(stations)
stations= stations_highest_rel_level(stations, 5)
dt=2
for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        print(dates,levels) """