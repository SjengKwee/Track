# Aangemaakt door Addey
# Inladen.py
# Hier laden we de data in, koel

import csv
from Classes.station import *

def stations_aanmaken():
    """
    Laad alle stations in, returnt een dictionary met alle lege stations
    """
    with open('Data/StationsHolland.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        stations = {}
        for row in csvreader:
            newStation = Station(row[0])
            stations[row[0]] = newStation
        
    return stations


def verbinding():
    """
    Maakt alle stations met hun verbindingen, met behulp van stations_aanmaken(), returnt een dictionary
    """
    with open('Data/ConnectiesHolland.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        stations = stations_aanmaken()
        for row in csvreader:
            if (row[0] in stations) & (row[1] in stations):
                stations[row[0]].add_verbinding(stations[row[1]],row[2])
                stations[row[1]].add_verbinding(stations[row[0]], row[2])
        return stations
                    
st = verbinding()
