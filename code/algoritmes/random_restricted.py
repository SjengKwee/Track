# Aangemaakt door Alec van Duin
# Random_algoritme.py
# Hier definieren we een restricted random algoritme, waar tracks niet twee keer door hetzelfde station gaat

import random
import csv
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.score import *
import time


class Restricted_1():

    def __init__(self, stations: dict):
        """
        Copieert stations en slaat deze op
        """

        self._stations = copy.deepcopy(stations)


    def random_restr_traject(self, minutes = 120): 
        """
        Deze functie maakt een willekeurig gemaakt traject van maximale lengte.
        """

        #Initialiseer parameters
        start_station = self._stations[random.choice(list(self._stations.keys()))]
        traject = Traject(start_station)
        passing_stations = [start_station._name]
        
        #Runt tot traject te lang wordt, of er geen stations over zijn
        stop = False
        while not stop:
            lijstje = list(traject._endstation._connection.keys())
            random.shuffle(lijstje)
            stop = True
            for connection in lijstje:
                if connection in passing_stations:
                    stop = True
                else:
                    conn_station = traject._endstation._connection[connection]
                    if int(traject._traveltime) + int(conn_station[1]) > minutes:
                        return traject
                    traject.add_trajectconnection(conn_station[0])
                    passing_stations.append(connection)
                    stop = False
                    break

        #Return
        return traject

    def run_random_restr_algoritme(self, n : int, minutes = 120):
        """
        Maakt n aantal random trajecten
        """

        #Initialiseer parameters
        lijst_traj = []

        #Maakt n random trajecten
        for i in range(n):
            traject = self.random_restr_traject(minutes)
            lijst_traj.append(traject)

        #Return
        return lijst_traj

    def run_random_restr_times(self, i : int, connections: int, minutes = 120, tracks = 7):
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
            traj = self.run_random_restr_algoritme(m, minutes)
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