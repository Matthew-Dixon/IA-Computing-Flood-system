from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.plot import plot_water_levels

def task2E():
    station = ""
    dates = []
    levels = []
    plot_water_levels(station, dates, levels)


task2E()