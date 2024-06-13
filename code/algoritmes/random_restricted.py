# Aangemaakt door Alec van Duin
# Random_algoritme.py
# Hier definieren we een restricted random algoritme, waar tracks niet twee keer door hetzelfde station gaat

import random
import csv
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.score import *
import time

def random_restr_traject(stations: dict): 
    """
    Deze functie maakt een willekeurig gemaakt traject van maximale lengte.
    """

    #Initialiseer parameters
    start_station = stations[random.choice(list(stations.keys()))]
    traject = Traject(start_station)
    passing_stations = [start_station]
    
    #Runt tot traject te lang wordt
    stop = False
    while not stop:
        lijstje = list(traject._endstation._connection.keys())
        lijstje = random.shuffle(lijstje)
        stop = True
        for connection in lijstje:
            if not connection in passing_stations:
                if int(traject._traveltime) + int(connection[1]) > 120:
                    return traject
                conn_station = traject._endstation._connection[connection]
                traject.add_trajectconnection[conn_station[0]]
                stop = False
                break

    #Return
    return traject

def run_random_restr_algoritme(stations: dict, n : int):
    """
    Maakt n aantal random trajecten
    """

    #Initialiseer parameters
    lijst_traj = []

    #Maakt n random trajecten
    for i in range(n):
        traject = random_restr_traject(stations)
        lijst_traj.append(traject)

    #Return
    return lijst_traj

def run_random_restr_times(stations: dict, i : int):
    """
    Maakt i keer 1-7 random trajecten en returnt een lijst van nuttige resultaten:
    [0]: een lijst met alle scores
    [1]: de maximaal gehaalde score
    [2]: het traject dat de maximale score heeft gehaald
    [3]: de minimaal gehaalde score
    [4]: het traject van minimale score
    [5]: de tijd die dit algoritme heeft gerunt
    [6]: een traject dat op het gemiddelde van 6000-6500 score zit
    [7]: de score van [6]
    """

    #Initialiseert parameters
    time0 = time.time()
    score_list = []
    max_score = 0
    min_score = 10000
    m = random.randint(1, 7)

    #Runt algoritme i keer
    for n in range(i):
        traj = run_random_restr_algoritme(stations, m)
        score_list.append(score_calc(traj))
        if score_calc(traj) > max_score:
            max_score = score_calc(traj)
            max_traj = traj
        elif score_calc(traj) < min_score:
            min_score = score_calc(traj)
            min_traj = traj
        elif score_calc(traj) > 6000 and score_calc(traj) < 6500:
            medium_traj = traj
    
    #Berekent laatste waardes
    medium_score = score_calc(medium_traj)
    time1 = time.time()

    #Return
    return [score_list, max_score, max_traj, min_score, min_traj, time1 - time0, medium_traj, medium_score]