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
T1 = Traject(stationDict['Beverwijk'])
T1.add_trajectconnection(stationDict["Castricum"])
T1.add_trajectconnection(stationDict["Alkmaar"])
T1.add_trajectconnection(stationDict["Hoorn"])
T1.add_trajectconnection(stationDict["Zaandam"])

T2 = Traject(stationDict["Amsterdam Sloterdijk"])
T2.add_trajectconnection(stationDict["Amsterdam Centraal"])
T2.add_trajectconnection(stationDict["Amsterdam Amstel"])
T2.add_trajectconnection(stationDict["Amsterdam Zuid"])
T2.add_trajectconnection(stationDict["Schiphol Airport"])
T2.add_trajectconnection(stationDict["Alkmaar"])

T3 = Traject(stationDict["Rotterdam Alexander"])
T3.add_trajectconnection(stationDict["Gouda"])
T3.add_trajectconnection(stationDict["Alphen a/d Rijn"])
T3.add_trajectconnection(stationDict["Leiden Centraal"])
T3.add_trajectconnection(stationDict["Schiphol Airport"])
T3.add_trajectconnection(stationDict["Amsterdam Zuid"])
sc = score_calc(stationDict,[T1,T2,T3])


filename = 'TestTraject.csv'

#Maak csv bestand
with open(filename, 'w', newline="") as file:
    writer = csv.writer(file,quoting=csv.QUOTE_MINIMAL, delimiter = ",")
    writer.writerows([["Tracks", "Stations"],["Track 1: ",T1._stations], ["Track 2: ", T2._stations],["Track 3: ", T3._stations], ["Score:", sc]])

#"Het is gelukt"
print("Jeei")

