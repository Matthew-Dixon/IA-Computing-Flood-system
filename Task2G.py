from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.floodwarning import floodwarning
from colorama import init
init()
def task2G():
    stations = build_station_list()
    update_water_levels(stations)

    # towns with mean relative levels above these 
    # thresholds are assigned to these categories
    tol_severe = 2
    tol_high = 1.6
    tol_moderate = 1.3
    tol_low = 1

    severe, high, moderate, low = floodwarning(stations, tol_severe, tol_high, tol_moderate, tol_low)

    print('\x1b[1;31;40m' + f"Severe: {severe}"+'\x1b[0m')
    print('\x1b[1;33;40m' + f"High: {high}"+ '\x1b[0m')
    print('\x1b[1;32;40m' +f"Moderate: {moderate}"+ '\x1b[0m')
    print('\x1b[1;34;40m' +f"Low: {low}"+ '\x1b[0m')
    

task2G()