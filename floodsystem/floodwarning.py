# Task 2G

def floodwarning(stations, tol_severe, tol_high, tol_moderate, tol_low):
    # Building a list of towns
    town_list = []


    for i in stations:
        if not i.town in town_list and not i.town is None:
            town_list.append(i.town)
    
    
    
    # Sorting stations into towns 
    # Creating a dictionary of towns as keys and empty lists as the values
    #town_stations_dict = dict.fromkeys(town_list, [])
    town_stations_dict = {k: [] for k in town_list}
    
    

    # Adding the water levels of the stations to the town keys

    for station in stations:
        if station.relative_water_level() is not None and station.town is not None:
            town_stations_dict[station.town].append(station.relative_water_level())
        


    #Finding the mean water level of each town
    for k in town_stations_dict:
        if len(town_stations_dict[k]) != 0: 
            town_stations_dict[k] = sum(town_stations_dict[k]) / len(town_stations_dict[k])
        else:
             town_stations_dict[k] = 0
    

    
    # Output
    severe = []
    high = []
    moderate = []
    low = []

    tol_severe = tol_severe
    tol_high = tol_high
    tol_moderate = tol_moderate
    tol_low = tol_low

    for j in town_stations_dict:
        if town_stations_dict[j] > tol_severe:
            severe.append(j)
        elif town_stations_dict[j] > tol_high:
            high.append(j)
        elif town_stations_dict[j] > tol_moderate:
            moderate.append(j)
        elif town_stations_dict[j] > tol_low:
            low.append(j)
        
       

    return severe, high, moderate, low

