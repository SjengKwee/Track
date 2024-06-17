# Aangemaakt door Alec van Duin
# Random_algoritme_3.py
# Hier definieren we een restricted random algoritme, waar geen enkele verbinding meer dan een keer wordt bereden

import copy
import time
import random
from code.classes.traject import *
from code.classes.station import *
from code.bouwblokjes.score import *

class Restricted_3():

    def __init__(self, stations: dict):
        """
        Init kopieert de stations, en initialiseert een lege lijst die de verbindingen bijhoudt
        """

        self._stations = copy.deepcopy(stations)
        self._ridentracks = []
    
    def random_restr3_traject(self):
        """
        Maakt een random traject met de restrictie dat iedere verbinding unieke is/nog niet in self._ridentracks staat
        """
        #Initialiseer parameters
        start_station = self._stations[random.choice(list(self._stations.keys()))]
        traject = Traject(start_station)
        tried_conn = []

        #add stop
        while True:
            connect_name = random.choice(list(traject._endstation._connection.keys()))
            connection = traject._endstation._connection[connect_name]
            if not {traject._endstation._name, connect_name} in self._ridentracks:
                if int(traject._traveltime) + int(connection[1]) > 120:
                    break
                self._ridentracks.append({traject._endstation._name, connect_name})
                traject.add_trajectconnection(connection[0])
                tried_conn = []

            elif connect_name not in tried_conn:
                tried_conn.append(connect_name)
            elif len(tried_conn) == len(traject._endstation._connection):
                break
        
        return traject
    
    def run_random_restr3_algoritme(self, n : int):
        """
        Maakt n aantal random trajecten, reset eerst ridentracks
        """

        #Initialiseer parameters
        lijst_traj = []
        self._ridentracks = []

        #Maakt n random trajecten
        for i in range(n):
            traject = self.random_restr3_traject()
            lijst_traj.append(traject)
        

        #Return
        return lijst_traj

    def run_random_restr3_times(self, i : int):
        """
        Maakt i keer 1-7 random trajecten met onze restrictie en returnt een lijst van nuttige resultaten:
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
        m = random.randint(1, 7)

        #Runt algoritme i keer
        for n in range(i):
            traj = self.run_random_restr3_algoritme(m)
            score_list.append(score_calc(traj))
            if score_calc(traj) > max_score:
                max_score = score_calc(traj)
                max_traj = traj
            elif score_calc(traj) < min_score:
                min_score = score_calc(traj)
                min_traj = traj
    
        #Berekent laatste waardes
        time1 = time.time()

        #Return
        return [score_list, max_score, max_traj, min_score, min_traj, time1 - time0]