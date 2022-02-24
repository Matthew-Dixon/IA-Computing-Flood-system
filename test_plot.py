import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

"""
def test_plot_water_levels():
    stations = build_station_list()
    update_water_levels(stations)

    output = stations_level_over_threshold(stations, 0.8)
    
    plots = output[:1]

    
    dt = 10
    for station in plots:
        station = station[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        x = plot_water_levels(station, dates, levels)

    assert x == x
"""