from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.floodwarning import floodwarning

def test_floodwarning():
    stations = build_station_list()
    update_water_levels(stations)

    # Edit the toleracnce levels
    tol_severe = 1
    tol_high = 0.7
    tol_moderate = 0.4
    tol_low = 0.1

    a, b, c, d = floodwarning(stations, tol_severe, tol_high, tol_moderate, tol_low)

    assert type(a) is list
    assert type(b) is list
    assert type(c) is list
    assert type(d) is list