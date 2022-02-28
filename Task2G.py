from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.floodwarning import floodwarning

def task2G():
    stations = build_station_list()
    update_water_levels(stations)

    # Edit the toleracnce levels
    tol_severe = 1
    tol_high = 0.7
    tol_moderate = 0.4
    tol_low = 0.1

    severe, high, moderate, low = floodwarning(stations, tol_severe, tol_high, tol_moderate, tol_low)

    #print(f"Severe: {severe}")
    #print(f"High: {high}")
    #print(f"Moderate: {moderate}")
    #print(f"Low: {low}")

task2G()