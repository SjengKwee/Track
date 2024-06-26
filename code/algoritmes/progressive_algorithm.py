# Aangemaakt door Sjeng
# progressive_algorithm.py
# Een algoritme dat tracks een voor een aanmaakt om ze op elkaar af te stemmen met heuristieken

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
    Een iteratief algoritme dat tracks een voor een bouwt, zodat ze op elkaar afgestemd kunnen worden met heuristieken
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

        # variabelen
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
        Runt het algoritme
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
                # kopieer de huidige tracks
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
    Een "Progressive_algorithm" dat trajecten bouwt met voorkeur voor onbereden connecties
    """
     
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)
        self._total_used_connections = set()

        self._all_connections = set()

        # Maak een lijst voor alle connecties
        for station_name in self._stations.keys():
            station = self._stations[station_name]
                
            # Voeg connecties toe
            for end_station in station._connection.keys():
                connection = Connection((station._name, end_station))

                # als ze er nog niet in zitten
                if connection not in self._all_connections:
                    self._all_connections.add(connection)
    
    def next_start_station(self):

        start_station = self._stations[random.choice(list(self._stations.keys()))]

        return start_station


    def next_track(self):

        # Initialiseer parameters
        start_station = self.next_start_station()
        traject = Traject(start_station)
        used_connections_temp = self._total_used_connections.copy()

        # Runt tot traject te lang wordt
        while True:
            # Maak een lijst van beschikbare connecties die nog niet gereden zijn.
            connections_choices = []
            connections_available = set()
            
            # Selecteer alle opties
            for station in traject._endstation._connection.keys():
                # voer paren toe aan available
                connections_available.add(Connection((traject._endstation._name, station)))

            # selecteer de onbereden opties
            connections_choices = list(connections_available - used_connections_temp)
            if not connections_choices:
                connections_choices = list(connections_available)
            
            # kies een optie
            choice = random.choice(connections_choices)

            # Voeg de connectie toe
            for station_name in choice:
                if station_name != traject._endstation._name:
                    endstation_name = station_name
            connection = traject._endstation._connection[endstation_name]
            if int(traject._traveltime) + int(connection[1]) > self._traveltime:
                break
            traject.add_trajectconnection(connection[0])

            # onthoud dat connectie is bereden
            if choice not in used_connections_temp:
                used_connections_temp.add(choice)
            
            # Stop het traject als alle verbindingen zijn bereden
            if used_connections_temp == self._all_connections:
                break

        #Return
        return traject
    
    def run(self):
        """
        Runt het algoritme
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

            # Vind het beste vervolg-traject
            for n in range(self._repetitions):

                # Kopieer huidige trajecten
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

            # voeg beste vervolg-traject toe aan lijnvoering
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]

                # update welke verbindingen zijn gebruikt
                for connection in self.max_tracks[track]._trajectconnection:
                    self._total_used_connections.add(connection)



class Progressive_stations(Progressive_connections):
    """
    Beperkt mogelijke startstations van trajecten tot stations die nog verbindingen hebben om te berijden.
    """
    
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)
        
        
    def next_start_station(self):
        """
        Kiest een station met nog te berijden verbindingen
        """

        # Selecteer onbereden verbindingen
        unused_connections = (self._all_connections - self._total_used_connections)
        if not unused_connections:

            # Als unused_connections leeg is, return een random startstation
            return self._stations[random.choice(list(self._stations.keys()))]

        # Selecteer alle stations met onbereden verbindingen
        stations = []
        for connection in unused_connections:
            for station in connection:
                if station not in stations:
                    stations.append(station)
        
        # Kies hieruit een willekeurig startstation 
        start_station_name = random.choice(stations)

        start_station = self._stations[start_station_name]

        return start_station

class Progressive_stations1(Progressive_connections):
    """
    Beperkt mogelijke startstations van trajecten tot stations die nog verbindingen hebben om te berijden.
    Heeft voorkeur voor stations met nog maar 1 verbinding over
    """
    
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)
        
        
    def next_start_station(self):
        """
        Kiest een station met nog te berijden verbindingen, met voorkeur voor 1 verbinding over.
        """
        # Selecteer onbereden verbindingen
        unused_connections = (self._all_connections - self._total_used_connections)
        if not unused_connections:

            # Als unused_connections leeg is, return een random startstation
            return self._stations[random.choice(list(self._stations.keys()))]

        # Selecteer alle stations met onbereden verbindingen
        stations = []
        single_stations = [] # stations met maar 1 verbinding over
        for connection in unused_connections:
            for station in connection:
                if station not in stations:
                    stations.append(station)
                    single_stations.append(station)
                elif station in single_stations:
                    single_stations.remove(station)
        
        if not single_stations:
            # # Kies hieruit een willekeurig startstation
            start_station_name = random.choice(stations)
        else:
            # # Kies hieruit een willekeurig startstation
            start_station_name = random.choice(single_stations)

        start_station = self._stations[start_station_name]

        return start_station

class Progressive_filler(Progressive_connections):
    """
    Heeft voorkeur voor verbindingen naar stations met nog maar 2 te berijden verbindingen
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

                # voeg paren toe aan available
                connections_available.add(Connection((traject._endstation._name, station)))

            # Selecteer alle stations met onbereden verbindingen
            connections_choices = list(connections_available - used_connections_temp)
            if not connections_choices:
                connections_choices = list(connections_available)

            # Vind alle stations met 2 onbereden verbindingen
            unused_connections_temp = (self._all_connections - used_connections_temp)
            
            numbered_connections = defaultdict(list)
            for connection in connections_choices:
                endstation_name = connection.endstation(traject._endstation._name)
                connection_counter = 0
                for unused_connection in unused_connections_temp:
                    if unused_connection.has(endstation_name):
                        connection_counter += 1
                numbered_connections[connection_counter].append(connection)
            
            # Order het aantal vervolgverbindingen
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
            
            # selecteer hieruit een random station
            choice = random.choice(connections_choices)

            # Maak connectie
            for station_name in choice:
                if station_name != traject._endstation._name:
                    endstation_name = station_name
            connection = traject._endstation._connection[endstation_name]

            # Voeg connectie toe
            if int(traject._traveltime) + int(connection[1]) > self._traveltime:
                break
            traject.add_trajectconnection(connection[0])

            # onthoud dat gekozen traject is gebruikt
            if choice not in used_connections_temp:
                used_connections_temp.add(choice)
            
            # Stop traject bouwen als alle verbindingen zijn bereden
            if used_connections_temp == self._all_connections:
                break

        #Return
        return traject
    
# class Progressive_even(Progressive_filler):

class Progressive_group(Progressive_stations):
    """
    Maakt het toevoegen van meerdere tracks tegelijkertijd mogelijk
    """
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28, groups = 1):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections)

        self._track_groups = groups

    def run(self):
        """
        Runt het algoritme
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

            # zoek de beste track
            for n in range(self._repetitions):

                # kopieer huidige tracks
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

            # voeg beste track toe aan lijnvoering
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]

                # update de gebruikte connecties
                for connection in self.max_tracks[track]._trajectconnection:
                    self._total_used_connections.add(connection)
            else:
                self._track_groups -= 1

class Progressive_even(Progressive_group):
    """
    Kiest welk vervolg-traject toe te voegen aan de hand van score op basis van heuristieken in plaats van standaardformule
    meer verbindingen en meer stations met een even aantal ongebruikte verbindingen over, zorgen voor een hogere score.
    """
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28, groups = 1):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections, groups = groups)

        self._even_scores = {}
        self._all_connections = set()
        self._station_connections = defaultdict(set)

        # Maak een lijst voor alle connecties
        for station_name in self._stations.keys():
            station = self._stations[station_name]
                
            # selecteer alle connecties van alle stations
            for end_station in station._connection.keys():

                # Voeg toe als ze er nog niet in zitten
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

            # punten voor het compleet maken van een station
            if connections_counter == 0:
                score += 100

            # punten voor het overlaten van een even aantal verbindingen
            elif (connections_counter % 2) == 0:
                score += 100

            # minpunten voor het overlaten van een oneven aantal verbindingen
            else:
                score -= 100

        return score


    def next_track(self, connections_in = None):

        #Initialiseer parameters
        start_station = self.next_start_station()
        traject = Traject(start_station)
        if connections_in != None:
            used_connections_temp = connections_in
        else:
            used_connections_temp = self._total_used_connections.copy()

        #Runt tot traject te lang wordt
        while True:

            # Maak een lijst van beschikbare connecties die nog niet gereden zijn.
            connections_choices = []
            connections_available = set()

            for station in traject._endstation._connection.keys():

                # voeg paren toe aan available
                connections_available.add(Connection((traject._endstation._name, station)))

            # selecteer de connecties die nog niet zijn bereden
            connections_choices = list(connections_available - used_connections_temp)
            if not connections_choices:
                connections_choices = list(connections_available)
            
            # selecteer een station
            choice = random.choice(connections_choices)

            # maak de connectie
            for station_name in choice:
                if station_name != traject._endstation._name:
                    endstation_name = station_name
            connection = traject._endstation._connection[endstation_name]
            if int(traject._traveltime) + int(connection[1]) > self._traveltime:
                break
            traject.add_trajectconnection(connection[0])

            # Onthoud dat de gekozen verbinding is bereden
            if choice not in used_connections_temp:
                used_connections_temp.add(choice)
            
            # Stop met bouwen aan traject als alle verbindingen zijn bereden
            if used_connections_temp == self._all_connections:
                break

        #Return
        return traject, used_connections_temp
        
    def run(self):
        """
        Runt het algoritme
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

            # Zoek de beste vervolg-track
            for n in range(self._repetitions):

                # Kopieer huidige tracks
                copy_tracks = copy.deepcopy(self._tracks)
                
                
                connections_in = None

                for n in range(self._track_groups):
                    
                    # maak track
                    # maak eerste track in n
                    if connections_in == None:
                        new_track, connections_in = self.next_track()

                    # maak vervolgtracks in n
                    else:
                        new_track, connections_in = self.next_track(connections_in)

                    # voeg toe aan oplossing
                    copy_tracks.append(new_track)

                # bereken score
                score = score_calc(copy_tracks, connections = self._number_of_connectinos)

                # sla score op in dictionary
                self.score_list[track].append(score)
                
                # bereken score volgens heuristiek
                even_score = self.even_score(connections = connections_in, number_of_connections = self._number_of_connectinos)

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

            # voeg de beste track toe
            if self.max_tracks.get(track):
                self._tracks.append(self.max_tracks[track])
                self.max_score = self.max_scores[track]

                # update gebruikte connecties
                for connection in self.max_tracks[track]._trajectconnection:
                    self._total_used_connections.add(connection)

class Progressive_final(Progressive_even):
    """
    Als er geen onbereden verbindingen beschikbaar zijn in het bouwen van een traject, kijkt het algoritme eerst naar alle vervolgstations om te proberen een onbereden connectie te vinden.
    """
    
    def __init__(self, stations, repetitions=1000, trains=7, traveltime = 120, times = 10, number_of_connections = 28, groups = 1):
        super().__init__(stations, repetitions, trains, traveltime, times, number_of_connections, groups = groups)

    def next_track(self, connections_in = None):

        #Initialiseer parameters
        start_station = self.next_start_station()
        traject = Traject(start_station)
        if connections_in != None:
            used_connections_temp = connections_in
        else:
            used_connections_temp = self._total_used_connections.copy()

        #Runt tot traject te lang wordt
        while True:

            # Maak een lijst van beschikbare connecties die nog niet gereden zijn.
            connections_choices = []
            connections_available = set()
            connections_prefered = set()

            for station in traject._endstation._connection.keys():

                # voeg paren toe aan available
                connections_available.add(Connection((traject._endstation._name, station)))

            # selecteer de connecties die nog niet zijn bereden
            connections_choices = list(connections_available - used_connections_temp)
            if not connections_choices:
                # Selecteer vervolgstations
                for next_station in traject._endstation._connection.keys():

                    # Kijk of vervolgstations onbereden verbindingen hebben
                    next_connections = set()

                    # list alle vervolgverbindingen
                    for next_next_station in self._stations[next_station]._connection.keys():
                        next_connections.add((Connection((next_station, next_next_station))))

                    # bekijk welke onbereden zijn
                    next_unused_connections = list(next_connections - used_connections_temp)

                    # voeg station toe als er onbereden verbindingen zijn
                    if next_unused_connections:
                        connections_prefered.add((Connection((traject._endstation._name, next_station))))

                # als lookahead  stations vind met onbereden verbindingen kies dan voor een van deze stations        
                if connections_prefered:
                    connections_choices = list(connections_prefered)
                
                else:
                    # anders kies uit een van alle opties
                    connections_choices = list(connections_available)
            
            # selecteer een station
            choice = random.choice(connections_choices)

            # maak de connectie
            for station_name in choice:
                if station_name != traject._endstation._name:
                    endstation_name = station_name
            connection = traject._endstation._connection[endstation_name]
            if int(traject._traveltime) + int(connection[1]) > self._traveltime:
                break
            traject.add_trajectconnection(connection[0])

            # Onthoud dat de gekozen verbinding is bereden
            if choice not in used_connections_temp:
                used_connections_temp.add(choice)
            
            # Stop met bouwen aan traject als alle verbindingen zijn bereden
            if used_connections_temp == self._all_connections:
                break

        #Return
        return traject, used_connections_temp