# Aangemaakt door Alec van Duin
# track_test.py
# Hier testen we een manualy made traject en sturen de resultaten in een csv

import csv
from Classes.Station import *
from Classes.Traject import *
from inladen import *
from score import *

#Maak tracks en bereken score
stationDict = make_connections()
T1 = Traject(stationDict['Hoorn'])
T1.add_trajectconnection(stationDict["Zaandam"])
T1.add_trajectconnection(stationDict["Beverwijk"])
T1.add_trajectconnection(stationDict["Castricum"])
T2 = Traject(stationDict["Den Helder"])
T2.add_trajectconnection(stationDict["Alkmaar"])
sc = score_calc(stationDict,[T1,T2])

filename = 'TestTraject.csv'

#Maak csv bestand
with open(filename, 'w', newline="") as file:
    writer = csv.writer(file,quoting=csv.QUOTE_MINIMAL, delimiter = ",")
    writer.writerows([["Tracks", "Stations"],["Track 1: ",T1._stations], ["Track 2: ", T2._stations], ["Score:", sc]])

#"Het is gelukt"
print("Jeei")

