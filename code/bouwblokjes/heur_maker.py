# Aangemaakt door Alec van Duin
# heur_maker.py
# Hier definieren we een aantal functies die heuristieken kunnen toevoegen aan de connecties

import time
import copy
import random
from code.classes.station import *
from code.classes.traject import *

def max_connection_counter(stations:dict):
    returnstations = copy.deepcopy(stations)
    for key in returnstations.keys():
        station = returnstations[key]
        for connection in station._apriori_heuristiek.keys():
            connecting_tuple = station._connection[connection]
            connecting_station = connecting_tuple[0]
            connected_number = len(connecting_station._connection)
            station._apriori_heuristiek[connection] = 1/connected_number
        returnstations[key] = station
    return returnstations

def min_traveltime(stations:dict):
    returnstations = copy.deepcopy(stations)
    for key in returnstations.keys():
        station = returnstations[key]
        for connection in station._apriori_heuristiek.keys():
            connecting_tuple = station._connection[connection]
            traveltime = connecting_tuple[1]
            station._apriori_heuristiek[connection] = traveltime
        returnstations[key] = station
    return returnstations