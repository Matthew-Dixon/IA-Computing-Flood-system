# Task 2G

def floodwarning(stations, tol_severe, tol_high, tol_moderate, tol_low):
    # Building a list of towns
    town_list = []


    for i in stations:
        if i.town in town_list:
            pass
        else:
            town_list.append(i.town)
    
    
    # Sorting stations into towns 
    # Creating a dictionary of towns as keys and empty lists as the values
    town_stations_dict = dict.fromkeys(town_list, [])
    print(town_stations_dict)
    
    # Adding the water levels of the stations to the town keys
    for station in stations:
        town_stations_dict[station.town].append(station.latest_level)

    # Removing all empty data
    for n in town_stations_dict:
        L = town_stations_dict[n]
        town_stations_dict[n] = [x for x in L if x is not None] 

        """ 
        lst = []
        for num in town_stations_dict[n]:
            if num != None:
                lst.append(num)
            else: 
                pass
            town_stations_dict[n] = lst
            lst = []
        """


    # Finding the mean water level of each town
    for k in town_stations_dict:
        town_stations_dict[k] = sum(town_stations_dict[k]) / len(town_stations_dict[k])
    
    #print(town_stations_dict)

    
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
            severe.append(f"{n} ({town_stations_dict[j]})")
        elif town_stations_dict[j] > tol_high:
            high.append(f"{n} ({town_stations_dict[j]})")
        elif town_stations_dict[j] > tol_moderate:
            moderate.append(f"{n} ({town_stations_dict[j]})")
        elif town_stations_dict[j] > tol_low:
            low.append(f"{n} ({town_stations_dict[j]})")
        else:
            low.append(f"{n} ({town_stations_dict[j]})")

    return severe, high, moderate, low