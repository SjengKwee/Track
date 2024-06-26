# Aangemaakt door Alec van Duin
# Random_algoritme.py
# Hier definieren we ons random algoritme

import random
import csv
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.score import *
import time

def random_traject(stations: dict, minutes=120): 
    """
    Deze functie maakt een willekeurig gemaakt traject van maximale lengte.
    """

    #Initialiseer parameters
    start_station = stations[random.choice(list(stations.keys()))]
    traject = Traject(start_station)
    
    #Runt tot traject te lang wordt
    while True:
        connection = traject._endstation._connection[random.choice(list(traject._endstation._connection.keys()))]
        if float(traject._traveltime) + float(connection[1]) > minutes:
            
            break
        traject.add_trajectconnection(connection[0])

    #Return
    return traject

def run_random_algoritme(stations: dict, n : int, minutes = 120):
    """
    Maakt n aantal random trajecten
    """

    #Initialiseer parameters
    lijst_traj = []

    #Maakt n random trajecten
    for i in range(n):
        traject = random_traject(stations, minutes)
        lijst_traj.append(traject)

    #Return
    return lijst_traj

def run_random_times(stations: dict, i : int, connections: int, minutes = 120, tracks = 7):
    """
    Maakt i keer 1-7 random trajecten en returnt een lijst van nuttige resultaten:
    [0]: een lijst met alle scores
    [1]: de maximaal gehaalde score
    [2]: het traject dat de maximale score heeft gehaald
    [3]: de minimaal gehaalde score
    [4]: het traject van minimale score
    [5]: de tijd die dit algoritme heeft gerunt
    """

    #Initialiseert parameters
    time0 = time.time()
    score_list = []
    max_score = 0
    min_score = 10000
    m = random.randint(1, tracks)

    #Runt algoritme i keer
    for n in range(i):
        traj = run_random_algoritme(stations, m, minutes)
        score_list.append(score_calc(traj, connections))
        if score_calc(traj, connections) > max_score:
            max_score = score_calc(traj, connections)
            max_traj = traj
        elif score_calc(traj, connections) < min_score:
            min_score = score_calc(traj, connections)
            min_traj = traj
    
    #Berekent laatste waardes
    time1 = time.time()

    #Return
    return [score_list, max_score, max_traj, min_score, min_traj, time1 - time0]