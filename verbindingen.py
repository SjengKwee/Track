import csv
from Station import *

stat = Station("Hoorn")
stationa = Station("Zaandam")
stationb = Station("Adam")
stat.add_verbinding(stationa,0)
stat.add_verbinding(stationb,0)


#print(f"Verbindingen van {stat._name}: {stat._verbinding}")

def stations_aanmaken():

    with open('StationsHolland.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        stations = []
        for row in csvreader:
            stations.append(row[0])
        
    return stations

def verbinding():
    with open('ConnectiesHolland.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        minuten = 0
        stations = stations_aanmaken()
        for row in csvreader:

            for station in stations:
                if row[0] == station:
                    huidige_station = Station(station)
                    verbinding_station = Station(row[1])
                    huidige_station.add_verbinding(verbinding_station,row[2])
                    print(f"Verbindingen van {huidige_station._name}: {huidige_station._verbinding}")
                 
                    
                    
        
              

st = verbinding()

