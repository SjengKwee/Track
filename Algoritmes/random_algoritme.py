import random
import csv
from classes.station import *
from classes.traject import *
from inladen import *
from score import *

def random_traject():
    stations = make_connections()
    start_station = stations[random.choice(stations.keys())]
    traject = Traject(start_station)
    while True:
        connection = traject._endstation._connection[random.choice(traject._endstation._connection.keys())]
        if traject._traveltime + connection[1] > 120:
            break
        traject.add_trajectconnection(connection[0])
    
    return traject

def run_random_algoritme():

    lijst_traj = []
    for i in range(6):
        traject = random_traject()
        lijst_traj.append(traject)

    print(len(lijst_traj), score_calc(lijst_traj))
