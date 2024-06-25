# Aangemaakt door Alec van Duin
# greedy_apriori.py
# Hier definieren we een greedy algoritme, die gebruikt maakt van heuristieken.

import time
import copy
import random
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.score import *

class Greedy_apri():

    def __init__(self,stations):
        """
        init, slaat de dictionary van de stations op, en houdt bij welke trajecten gepasseert zijn
        """

        self._stations = copy.deepcopy(stations)
        self._ridentracks = []

    def greedy_traject(self):
        """
        Maakt een greedy traject op mbv een random startstation en heuristieken meegegeven bij de stations
        """

        #Initialise variabelen
        traject = Traject(self._stations[random.choice(list(self._stations.keys()))])
        tried_conn = []

        #Bouwt langzaam een traject
        while True:
            first_connections = sorted(traject._endstation._apriori_heuristiek.items(), key=lambda item: item[1])
            sorted_connections = []
            for items in first_connections:
                sorted_connections.append(items[0])
            for connection in sorted_connections:
                if not {traject._endstation._name, connection} in self._ridentracks:
                    new_conn = traject._endstation._connection[connection]
                    if int(traject._traveltime) + int(new_conn[1]) > 120:
                        return traject
                    self._ridentracks.append({traject._endstation._name, connection})
                    traject.add_trajectconnection(new_conn[0])
                    tried_conn = []
                    break
                
                #Houdt bij welke verbindingen geprobeerd zijn
                elif connection not in tried_conn:
                    tried_conn.append(connection)

                #Escape als er geen verbindingen meer gelegd kunnen worden
                elif len(tried_conn) == len(traject._endstation._connection):
                    return traject

    def greedy_alg(self,n: int):
        """
        Maakt i aantal greedy trajecten, die geen verbindingen dubbel doen
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

    def run_greedy_times(self, i : int, connections: int):
        """
        Maakt i keer 1-7 greedy trajecten en returnt een lijst van nuttige resultaten:
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