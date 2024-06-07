
import csv
from Classes.Station import *
from Classes.Traject import *
from inladen import *

stationDict = make_connections()
#print(stationDict["Alkmaar"])
T1 = Traject(stationDict['Alkmaar'])
T1.add_trajectconnection(stationDict["Hoorn"])
T1.add_trajectconnection(stationDict["Zaandam"])
T1.add_trajectconnection(stationDict["Beverwijk"])
T1.add_trajectconnection(stationDict["Castricum"])
print(T1._traveltime)
print(T1._trajectconnection)
print(T1._stations)
T2 = Traject(stationDict["Alkmaar"])
T2.add_trajectconnection(stationDict["Den Helder"])



filename = 'TestTraject.csv'

with open(filename, 'w', newline="") as file:
    writer = csv.writer(file,quoting=csv.QUOTE_MINIMAL, delimiter = ",")
    writer.writerows([["Tracks", "Stations"],["Track 1: ",T1._stations], ["Track 2: ", T2._stations]])

print("Jeei")

