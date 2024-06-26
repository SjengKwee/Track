# Aangemaakt door Addey
# Inladen.py
# Hier laden we de data in, koel

import csv
from code.classes.station import *

def make_stations(stations_file = 'StationsHolland.csv'):
    """
    Laad alle stations in, returnt een dictionary met alle lege stations
    """

    #Maakt stations
    csvlocation = 'data/input/' + str(stations_file)
    with open(csvlocation, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        stations = {}
        for row in csvreader:
            coordinates = (row[1], row[2])
            newStation = Station(row[0], coordinates)
            stations[row[0]] = newStation
    
    #Return
    return stations


def make_connections(stations_file = 'StationsHolland.csv', connecties_file = 'ConnectiesHolland.csv'):
    """
    Maakt alle stations met hun verbindingen, met behulp van stations_aanmaken(), returnt een dictionary
    """

    #Itereerd door bestanden en maakt de volledige verbindingen
    csvlocation = 'data/input/' + str(connecties_file)
    with open(csvlocation, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        stations = make_stations(stations_file = stations_file)
        for row in csvreader:
            if (row[0] in stations) & (row[1] in stations):
                stations[row[0]].add_connection(stations[row[1]],row[2], 1)
                stations[row[1]].add_connection(stations[row[0]], row[2], 1)

        #Return
        return stations

def save_connections():
    """
    Slaat de ingeladen data op in een csv bestand
    """

    with open('data/input/ConnectiesHolland.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader) # skip the header

        # make a dictionary for connections
        all_connections = []

        # save all connections
        for row in csvreader:
            new_connection = set()
            new_connection.add(row[0])
            new_connection.add(row[1])
            all_connections.append(new_connection)
        
        # return
        return all_connections
        
