# Aangemaakt door Alec van Duin
# greedy_apriori.py
# Hier definieren we een greedy algoritme, die gebruikt maakt van heuristieken.

import time
import copy
import random
from code.classes.station import *
from code.classes.traject import *

class Greedy_apri():

    def __init__(self,stations):
        self._stations = copy.deepcopy(stations)
        self._ridentracks = []

    def greedy_traject(self):
        traject = Traject(self._stations[random.choice(list(self._stations.keys()))])
        tried_conn = []

        while True:
            sorted_connections = sorted(traject._endstation._apriori_heuristiek)
            for connection in sorted_connections:
                if not {traject._endstation._name, connection} in self._ridentracks:
                    new_conn = traject._endstation._connection[connection]
                    if int(traject._traveltime) + int(new_conn[1]) > 120:
                        return traject
                    traject.add_trajectconnection(new_conn[0])
                    tried_conn = []
                    self._ridentracks.append({traject._endstation._name, connection})
                elif connect_name not in tried_conn:
                    tried_conn.append(connect_name)
                elif len(tried_conn) == len(traject._endstation._connection):
                    return traject

    def greedy_alg(self,n: int):
        """
        Maakt i aantal random trajecten
        """

        #Initialiseer parameters
        lijst_traj = []
        self._ridentracks = []

        #Maakt n random trajecten
        for i in range(n):
            traject = self.greedy_traject()
            lijst_traj.append(traject)
        
        #Return
        return lijst_traj

    def run_greedy_times(self, i : int):
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
        m = random.randint(1, 7)

        #Runt algoritme i keer
        for n in range(i):
            traj = self.greedy_alg(m)
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