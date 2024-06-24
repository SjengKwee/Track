# Aangemaakt door Sjeng
# progressive_algorithm.py
# Een algoritme dat tracks een voor een aanmaakt, en hierbij let op vorige tracks.

import random
from collections import defaultdict
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.score import *
from code.algoritmes.random_algoritme import *
from code.bouwblokjes.inladen import *
from code.classes.connection import *
import copy
import time


class Progressive_algorithm:

    """
    An iterative algorithm? that builds tracks sequentially, so it can be optimized with heuristics based on the previously chosen tracks.
    """

    # initieer algoritme
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        # parameters
        self._stations = copy.deepcopy(stations)
        self._number_of_connectinos = number_of_connections
        self._tracks = []
        self._trains = trains
        self._repetitions = repetitions
        self._times = times
        self._traveltime = traveltime

        # variables
        self.best_max_scores = {}
        self.best_max_score = 0
        self.best_max_tracks = {}
        self.score_list = {}
        self.max_scores = {}
        self.max_tracks = {}
        self.max_score = 0
        self.all_max_scores = []
        
    def next_start_station(self):

        start_station = self._stations[random.choice(list(self._stations.keys()))]

        return start_station

    def next_track(self):
        

        #Initialiseer parameters
        start_station = self.next_start_station()
        new_track = Traject(start_station)
        
        #Runt tot traject te lang wordt
        while True:
            connection = new_track._endstation._connection[random.choice(list(new_track._endstation._connection.keys()))]
            if int(new_track._traveltime) + int(connection[1]) > self._traveltime:
                break
            new_track.add_trajectconnection(connection[0])

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
                score = score_calc(copy_tracks, connections = self._number_of_connectinos)

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

            # onthoud de maximumscores
            self.all_max_scores.append(self.max_score)

            # onthoud de beste maximumscore
            if self.max_score > self.best_max_score:
                print("New best score found")
                self.best_max_score = self.max_score
                self.best_max_scores = copy.deepcopy(self.max_scores)
                self.best_max_tracks = copy.deepcopy(self.max_tracks)
    
        
class Progressive_connections(Progressive_algorithm):
    """
    A "Progressive_algorithm" that tries to build tracks that do not overlap with previous tracks
    """
     
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)
        self._total_used_connections = set()

        self._all_connections = set()

        # Make a list of all connections
        for station_name in self._stations.keys():
            station = self._stations[station_name]
                
            # for all connections in station
            for end_station in station._connection.keys():

                # if not in all_connections add to it
                connection = Connection((station._name, end_station))
                if connection not in self._all_connections:
                    self._all_connections.add(connection)
    
    def next_start_station(self):

        start_station = self._stations[random.choice(list(self._stations.keys()))]

        return start_station


    def next_track(self):

        #Initialiseer parameters
        start_station = self.next_start_station()
        traject = Traject(start_station)
        used_connections_temp = self._total_used_connections.copy()

        #Runt tot traject te lang wordt
        while True:
            # Maak een lijst van beschikbare connecties die nog niet gereden zijn.
            connections_choices = []
            connections_available = set()

            for station in traject._endstation._connection.keys():

                # add pairs to available
                connections_available.add(Connection((traject._endstation._name, station)))

            # select choices not in used_connections
            connections_choices = list(connections_available - used_connections_temp)
            if not connections_choices:
                connections_choices = list(connections_available)
            
            # select the station to go to
            choice = random.choice(connections_choices)

            # make connection
            for station_name in choice:
                if station_name != traject._endstation._name:
                    endstation_name = station_name
            connection = traject._endstation._connection[endstation_name]
            if int(traject._traveltime) + int(connection[1]) > self._traveltime:
                break
            traject.add_trajectconnection(connection[0])

            # add chosen connection to used_connections in both directions
            if choice not in used_connections_temp:
                used_connections_temp.add(choice)
            
            # !!! stop running if all connections have been used. !!!
            if used_connections_temp == self._all_connections:
                break

        #Return
        return traject
    
    def run(self):
        """
        Runs the algorithm
        """
        self.score_list.clear()
        self.max_scores.clear()
        self.max_tracks.clear()
        self._tracks.clear()
        self.max_score = 0

        self._total_used_connections = set()

        for track in range(self._trains):
            self.score_list[track] = []
            self.max_scores[track] = 0

            # find best track to add
            for n in range(self._repetitions):
                # copy the current tracks
                copy_tracks = copy.deepcopy(self._tracks)

                # maak track
                new_track = self.next_track()

                # voeg toe aan oplossing
                copy_tracks.append(new_track)

                # bereken score en sla op in dictionary
                score = score_calc(copy_tracks, connections = self._number_of_connectinos)

                # sla score op in dictionary
                self.score_list[track].append(score)

                # onthoud hoogste score, track, en gebruikte verbindingen
                if track == 0:
                    if score > self.max_scores[track]:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track

                else:
                    if score > self.max_scores[track] and score > self.max_scores[(track-1)] and self.max_scores[(track-1)] != 0:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track

            # add best track
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]

                # update total used connections
                for connection in self.max_tracks[track]._trajectconnection:
                    self._total_used_connections.add(connection)



class Progressive_stations(Progressive_connections):
    """
    Limits startstations to stations that still have connections that are unused.
    """
    
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)
        
        
    def next_start_station(self):
        """
        chooses a station that has connections left
        """

        unused_connections = (self._all_connections - self._total_used_connections)

        if not unused_connections:
            # If there are no unused connections, return a random station
            return self._stations[random.choice(list(self._stations.keys()))]

        #list all stations of interest
        stations = []
        for connection in unused_connections:
            for station in connection:
                if station not in stations:
                    stations.append(station)
        
        # choose random station
        start_station_name = random.choice(stations)

        start_station = self._stations[start_station_name]

        return start_station

class Progressive_stations1(Progressive_connections):
    """
    Limits startstations to stations that still have connections that are unused.
    Lets stations with only 1 connection left be prefered as startstation. 
    """
    
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)
        
        
    def next_start_station(self):
        """
        chooses a station that has connections left
        """

        unused_connections = (self._all_connections - self._total_used_connections)

        if not unused_connections:
            # If there are no unused connections, return a random station
            return self._stations[random.choice(list(self._stations.keys()))]

        #list all stations of interest
        stations = []
        single_stations = [] # stations with only 1 connection left
        for connection in unused_connections:
            for station in connection:
                if station not in stations:
                    stations.append(station)
                    single_stations.append(station)
                elif station in single_stations:
                    single_stations.remove(station)
        
        if not single_stations:
            # choose random station
            start_station_name = random.choice(stations)
        else:
            # choose random single_station
            start_station_name = random.choice(single_stations)

        start_station = self._stations[start_station_name]

        return start_station

class Progressive_filler(Progressive_connections):
    """
    prioritises connections that lead to stations that have 2 connections left, so 1 more to go to after
    """
    

    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)

    def next_track(self):

        #Initialiseer parameters
        start_station = self.next_start_station()
        traject = Traject(start_station)
        used_connections_temp = self._total_used_connections.copy()

        #Runt tot traject te lang wordt
        while True:
            # Maak een lijst van beschikbare connecties die nog niet gereden zijn.
            connections_choices = []
            connections_available = set()

            for station in traject._endstation._connection.keys():

                # add pairs to available
                connections_available.add(Connection((traject._endstation._name, station)))

            # select choices not in used_connections
            connections_choices = list(connections_available - used_connections_temp)
            if not connections_choices:
                connections_choices = list(connections_available)

            # for all available connections find the ones with an endstation that is in unused_connections_temp twice.
            unused_connections_temp = (self._all_connections - used_connections_temp)
            
            numbered_connections = defaultdict(list)
            for connection in connections_choices:
                endstation_name = connection.endstation(traject._endstation._name)
                connection_counter = 0
                for unused_connection in unused_connections_temp:
                    if unused_connection.has(endstation_name):
                        connection_counter += 1
                numbered_connections[connection_counter].append(connection)
            
            # Order the number of followup connections (+1) to favor
            if not numbered_connections[2]:
                numbers = [1, 3, 4, 5, 6, 7]
                random.shuffle(numbers)
                for number in numbers:
                    if not numbered_connections[number]:
                        continue
                    else:
                        connections_choices = numbered_connections[number]
                        break
            else:
                connections_choices = numbered_connections[2]                
            
            # select the station to go to
            choice = random.choice(connections_choices)

            # make connection
            for station_name in choice:
                if station_name != traject._endstation._name:
                    endstation_name = station_name
            connection = traject._endstation._connection[endstation_name]

            if int(traject._traveltime) + int(connection[1]) > self._traveltime:
                break
            traject.add_trajectconnection(connection[0])

            # add chosen connection to used_connections
            if choice not in used_connections_temp:
                used_connections_temp.add(choice)
            
            # !!! stop running if all connections have been used. !!!
            if used_connections_temp == self._all_connections:
                break

        #Return
        return traject
    
# class Progressive_even(Progressive_filler):

 
class Progressive_randomstart(Progressive_filler):
    """
    Makes sure the first track is not chosen based on the filler Heuristics
    """
    

    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)

    def first_track(self):  # same as Progressive_connections' next track

        #Initialiseer parameters
        start_station = self.next_start_station()
        new_track = Traject(start_station)
        
        #Runt tot traject te lang wordt
        while True:
            connection = new_track._endstation._connection[random.choice(list(new_track._endstation._connection.keys()))]
            if int(new_track._traveltime) + int(connection[1]) > self._traveltime:
                break
            new_track.add_trajectconnection(connection[0])

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

        self._total_used_connections = set()

        for track in range(self._trains):
            self.score_list[track] = []
            self.max_scores[track] = 0

            # find best track to add
            for n in range(self._repetitions):
                # copy the current tracks
                copy_tracks = copy.deepcopy(self._tracks)

                # maak track
                new_track = self.next_track()

                # voeg toe aan oplossing
                copy_tracks.append(new_track)

                # bereken score en sla op in dictionary
                score = score_calc(copy_tracks, connections = self._number_of_connectinos)

                # sla score op in dictionary
                self.score_list[track].append(score)

                # onthoud hoogste score, track, en gebruikte verbindingen
                if track == 0:
                    if score > self.max_scores[track]:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track

                else:
                    if score > self.max_scores[track] and score > self.max_scores[(track-1)] and self.max_scores[(track-1)] != 0:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track
                
                if track == 0:
                    break

            # add best track
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]

                # update total used connections
                for connection in self.max_tracks[track]._trajectconnection:
                    self._total_used_connections.add(connection)

class Progressive_group(Progressive_stations):
    """
    Adds 2 (or more) tracks at a time
    """
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28, groups = 1):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)

        self._track_groups = groups

    # Cut trajectories in 2
    def run(self):
        """
        Runs the algorithm
        """
        self.score_list.clear()
        self.max_scores.clear()
        self.max_tracks.clear()
        self._tracks.clear()
        self.max_score = 0

        self._total_used_connections = set()

        for track in range(self._trains):
            self.score_list[track] = []
            self.max_scores[track] = 0

            # find best track to add
            for n in range(self._repetitions):
                # copy the current tracks
                copy_tracks = copy.deepcopy(self._tracks)

                for n in range(self._track_groups):
                    # maak track
                    new_track = self.next_track()

                    # voeg toe aan oplossing
                    copy_tracks.append(new_track)

                # bereken score en sla op in dictionary
                score = score_calc(copy_tracks, connections = self._number_of_connectinos)

                # sla score op in dictionary
                self.score_list[track].append(score)

                # onthoud hoogste score, track, en gebruikte verbindingen
                if track == 0:
                    if score > self.max_scores[track]:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track

                else:
                    if score > self.max_scores[track] and score > self.max_scores[(track-1)] and self.max_scores[(track-1)] != 0:
                        self.max_scores[track] = score
                        self.max_tracks[track] = new_track

            # add best track
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]

                # update total used connections
                for connection in self.max_tracks[track]._trajectconnection:
                    self._total_used_connections.add(connection)
            else:
                self._track_groups -= 1

class Progressive_even(Progressive_group):
    """
    Picks which track to add based on heuristic score, instead of regular formula
    """
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28, groups = 1):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections, groups = groups)

        self._even_scores = {}
        self._all_connections = set()
        self._station_connections = defaultdict(set)

        # Make a list of all connections
        for station_name in self._stations.keys():
            station = self._stations[station_name]
                
            # for all connections in station
            for end_station in station._connection.keys():

                # if not in all_connections add to it
                connection = Connection((station._name, end_station))
                self._station_connections[station_name].add(connection)
                if connection not in self._all_connections:
                    self._all_connections.add(connection)


    def even_score(self, connections, number_of_connections):
        
        score = 0
        # Punten voor het aantal gereden verbindingen?
        score += (len(connections) * 100)

        # punten voor de verhouding even/oneven verbindingen bij stations
        for station_name in self._station_connections.keys():
            
            connections_counter = 0

            for connection in self._station_connections[station_name]:
                if connection not in connections:
                     connections_counter += 1

            # if station is finished, increase score 
            if connections_counter == 0:
                score += 100

            # if number of connections is even, increase score
            elif (connections_counter % 2) == 0:
                score += 100

            # if number of connections is odd, decrease score
            else:
                score -= 100

        return score


    def next_track(self):

        #Initialiseer parameters
        start_station = self.next_start_station()
        traject = Traject(start_station)
        used_connections_temp = self._total_used_connections.copy()

        #Runt tot traject te lang wordt
        while True:
            # Maak een lijst van beschikbare connecties die nog niet gereden zijn.
            connections_choices = []
            connections_available = set()

            for station in traject._endstation._connection.keys():

                # add pairs to available
                connections_available.add(Connection((traject._endstation._name, station)))

            # select choices not in used_connections
            connections_choices = list(connections_available - used_connections_temp)
            if not connections_choices:
                connections_choices = list(connections_available)
            
            # select the station to go to
            choice = random.choice(connections_choices)

            # make connection
            for station_name in choice:
                if station_name != traject._endstation._name:
                    endstation_name = station_name
            connection = traject._endstation._connection[endstation_name]
            if int(traject._traveltime) + int(connection[1]) > self._traveltime:
                break
            traject.add_trajectconnection(connection[0])

            # add chosen connection to used_connections in both directions
            if choice not in used_connections_temp:
                used_connections_temp.add(choice)
            
            # !!! stop running if all connections have been used. !!!
            if used_connections_temp == self._all_connections:
                break

        #Return
        return traject, used_connections_temp
        
    def run(self):
        """
        Runs the algorithm
        """
        self.score_list.clear()
        self.max_scores.clear()
        self.max_tracks.clear()
        self._tracks.clear()
        self.max_score = 0
        self._even_scores.clear()

        self._total_used_connections = set()

        for track in range(self._trains):
            self.score_list[track] = []
            self.max_scores[track] = 0
            self._even_scores[track] = 0

            # find best track to add
            for n in range(self._repetitions):
                # copy the current tracks
                copy_tracks = copy.deepcopy(self._tracks)

                # maak track
                new_track, connections = self.next_track()

                # voeg toe aan oplossing
                copy_tracks.append(new_track)

                # bereken score
                score = score_calc(copy_tracks, connections = self._number_of_connectinos)

                # sla score op in dictionary ?????
                self.score_list[track].append(score)
                
                # bereken score volgens heuristiek
                even_score = self.even_score(connections = connections, number_of_connections = self._number_of_connectinos)

                # onthoud hoogste score, track, en gebruikte verbindingen
                if track == 0:
                    if even_score > self._even_scores[track]:
                        self.max_scores[track] = score
                        self._even_scores[track] = even_score
                        self.max_tracks[track] = new_track

                else:
                    if even_score > self._even_scores[track] and even_score > self._even_scores[(track-1)] and self._even_scores[(track-1)] != 0:
                        self.max_scores[track] = score
                        self._even_scores[track] = even_score
                        self.max_tracks[track] = new_track

            # add best track
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]

                # update total used connections
                for connection in self.max_tracks[track]._trajectconnection:
                    self._total_used_connections.add(connection)
 