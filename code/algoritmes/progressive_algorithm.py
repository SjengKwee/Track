# Aangemaakt door Sjeng
# progressive_algorithm.py
# Een algoritme dat tracks een voor een aanmaakt, en hierbij let op vorige tracks.

import random
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.score import *
from code.algoritmes.random_algoritme import *
from code.bouwblokjes.inladen import *
import copy
import time

class Progressive_algorithm:

    """
    An iterative algorithm? that builds tracks sequentially, so it can be optimized with heuristics based on the previously chosen tracks.
    """

    # initieer algoritme
    def __init__(self, stations, repetitions=1000, trains=7, times = 10):
        self._stations = copy.deepcopy(stations)
        self._tracks = []
        self._trains = trains
        self._repetitions = repetitions
        self._times = times
        self.all_max_scores = {}
        self.all_max_score = 0
        self.all_max_tracks = {}
        self.score_list = {}
        self.max_scores = {}
        self.max_tracks = {}
        self.max_score = 0
        
    def update_connections(self):
        raise NotImplementedError
    
    def next_start_station(self):
        raise NotImplementedError

    def next_track(self):
        
        new_track = random_traject(self._stations)

        return new_track

    def run(self):
        """
        Runs the algorithm
        """
        self.score_list.clear()
        self.max_scores.clear()
        self.max_tracks.clear()
        self._tracks.clear()
        self.max_score = 0

        for track in range(self._trains):
            self.score_list[track] = []
            self.max_scores[track] = 0

            for n in range(self._repetitions):
                # copy the current tracks
                copy_tracks = copy.deepcopy(self._tracks)

                # maak track
                new_track = self.next_track()

                # voeg toe aan oplossing
                copy_tracks.append(new_track)

                # bereken score en sla op in dictionary
                score = score_calc(copy_tracks)

                # sla score op in dictionary
                self.score_list[track].append(score)

                # onthoud hoogste score en track
                if track == 0:
                    if score > self.max_scores[track]:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track
                else:
                    if score > self.max_scores[track] and score > self.max_scores[(track-1)] and self.max_scores[(track-1)] != 0:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track

            # voeg beste volgende traject toe
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]
            

    def run_times(self):

        for i in range(self._times):
            self.run()
            print(self.max_score)
            if self.max_score > self.all_max_score:
                print("New best score found")
                self.all_max_score = self.max_score
                self.all_max_scores = copy.deepcopy(self.max_scores)
                self.all_max_tracks = copy.deepcopy(self.max_tracks)
    
        
class Progressive_connections(Progressive_algorithm):
    """
    A "Progressive_algorithm" that tries to build tracks that do not overlap with previous tracks
    """
     
    def __init__(self, stations, repetitions=1000, trains=7, times = 10):
        super().__init__(stations, repetitions=1000, trains=7, times = 10)
        self._used_connections = set()
    
    def next_track(self):

        #Initialiseer parameters
        start_station = self._stations[random.choice(list(self._stations.keys()))]
        traject = Traject(start_station)

        #Runt tot traject te lang wordt
        while True:
            # Maak een lijst van beschikbare connecties die nog niet gereden zijn.
            connections_choices = []
            connections_available = set()
            for station in traject._endstation._connection.keys():

                # add pairs to available
                connections_available.add((traject._endstation._name, station))

            # select choices not in used_connections
            connections_choices = list(connections_available - self._used_connections)
            if not connections_choices:
                connections_choices = connections_available
            
            # select the station to go to
            choice = random.choice(list(connections_choices))

            # make connection
            connection = traject._endstation._connection[choice[1]]
            if int(traject._traveltime) + int(connection[1]) > 120:
                break
            traject.add_trajectconnection(connection[0])

            # add chosen connection to used_connections in both directions
            if choice not in self._used_connections:
                self._used_connections.add(choice)
                self._used_connections.add((choice[1], choice[0]))

        #Return
        return traject


class Progressive_stations(Progressive_algorithm):

    def __init__(self, stations, repetitions=1000, trains=7, times = 10):
        super(Progressive_algorithm, self).__init__(stations, repetitions=1000, trains=7, times = 10)
        self._unused_stations = stations
        

 
# def next_traject(stations: dict): 
#     """
#     Deze functie maakt een traject dat zo min mogelijk overlapt met de vorige trajecten.
#     """

#     #Initialiseer parameters
#     start_station = stations[random.choice(list(stations.keys()))]
#     traject = Traject(start_station)
    
#     #Runt tot traject te lang wordt
#     while True:
        
#         connection = traject._endstation._connection[random.choice(list(traject._endstation._connection.keys()))]
#         if int(traject._traveltime) + int(connection[1]) > 120:
#             break
#         traject.add_trajectconnection(connection[0])

#     #Return
#     return traject

# first_track = random_traject()








    
