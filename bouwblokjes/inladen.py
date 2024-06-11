# Aangemaakt door Addey
# Inladen.py
# Hier laden we de data in, koel

import csv
from classes.station import *

def make_stations():
    """
    Laad alle stations in, returnt een dictionary met alle lege stations
    """
    with open('Data/StationsHolland.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        stations = {}
        for row in csvreader:
            coordinates = (row[1], row[2])
            newStation = Station(row[0], coordinates)
            stations[row[0]] = newStation

        
    return stations


def make_connections():
    """
    Maakt alle stations met hun verbindingen, met behulp van stations_aanmaken(), returnt een dictionary
    """
    with open('Data/ConnectiesHolland.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        stations = make_stations()
        for row in csvreader:
            if (row[0] in stations) & (row[1] in stations):
                stations[row[0]].add_connection(stations[row[1]],row[2])
                stations[row[1]].add_connection(stations[row[0]], row[2])
        return stations
