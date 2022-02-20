import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def task2E():
    stations = build_station_list()
    update_water_levels(stations)

    output = stations_level_over_threshold(stations, 0.8)
    
    # The first datum is absurdly high, so i used the next 5 
    plots = output[1:6]
    #plots = output[:5]

    dt = 10

    for station in plots:
        station = station[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        plot_water_levels(station, dates, levels)


task2E()