import random
import csv
from classes.station import *
from classes.traject import *
from bouwblokjes.score import *
import time

def random_traject(stations: dict):    
    start_station = stations[random.choice(list(stations.keys()))]
    traject = Traject(start_station)
    # print(traject)
    
    while True:
        connection = traject._endstation._connection[random.choice(list(traject._endstation._connection.keys()))]
        # print(connection)
        if int(traject._traveltime) + int(connection[1]) > 120:
            break
        traject.add_trajectconnection(connection[0])
    
    return traject

def run_random_algoritme(stations: dict):
    lijst_traj = []
    for i in range(7):
        traject = random_traject(stations)
        lijst_traj.append(traject)
        # print(traject)
    
    # print(len(lijst_traj), score_calc(lijst_traj))

    return lijst_traj

def run_random_times(stations: dict, i : int):
    time0 = time.time()
    score_list = []
    max_score = 0
    min_score = 10000

    for n in range(i):
        traj = run_random_algoritme(stations)
        score_list.append(score_calc(traj))
        if score_calc(traj) > max_score:
            max_score = score_calc(traj)
            max_traj = traj
        elif score_calc(traj) < min_score:
            min_score = score_calc(traj)
            min_traj = traj

    time1 = time.time()
    return [score_list, max_score, max_traj, min_score, min_traj, time1 - time0]