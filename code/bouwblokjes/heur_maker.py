# Aangemaakt door Alec van Duin
# heur_maker.py
# Hier definieren we een aantal functies die heuristieken kunnen toevoegen aan de stations

import time
import copy
import random
from code.classes.station import *
from code.classes.traject import *

def max_connection_counter(stations:dict):
    """
    Maakt een heuristiek die berekent wordt door 1/aantal connecties station
    """

    #Initialiseer parameters
    returnstations = copy.deepcopy(stations)

    #Implementeer heuristiek
    for key in returnstations.keys():
        station = returnstations[key]
        for connection in station._apriori_heuristiek.keys():
            connecting_tuple = station._connection[connection]
            connecting_station = connecting_tuple[0]
            connected_number = -len(connecting_station._connection)
            station._apriori_heuristiek[connection] = int(connected_number)
        returnstations[key] = station

    #Return nieuwe stations
    return returnstations

def min_traveltime(stations:dict):
    """
    Maakt een heuristiek gelijk aan de traveltime naar dit station
    """

    #Initialiseer parameters
    returnstations = copy.deepcopy(stations)

    #Implementeer heuristiek
    for key in returnstations.keys():
        station = returnstations[key]
        for connection in station._apriori_heuristiek.keys():
            connecting_tuple = station._connection[connection]
            traveltime = connecting_tuple[1]
            station._apriori_heuristiek[connection] = traveltime
        returnstations[key] = station

    #Return nieuwe stations
    return returnstations

def combi(stations:dict, weight_conn: float, weight_trav: float):
    """
    Maakt een heuristiek die de connecties en traveltime combineert waar ook gewichten aan gezet kunnen worden
    """

    #Initialiseer parameters
    returnstations = copy.deepcopy(stations)

    #Implementeer heuristiek
    for key in returnstations.keys():
        station = returnstations[key]
        for connection in station._apriori_heuristiek.keys():
            connecting_tuple = station._connection[connection]
            traveltime = connecting_tuple[1]
            connecting_station = connecting_tuple[0]
            connected_number = len(connecting_station._connection)
            station._apriori_heuristiek[connection] = weight_trav*traveltime - weight_conn*connected_number
        returnstations[key] = station

    #Return nieuwe stations
    return returnstations
