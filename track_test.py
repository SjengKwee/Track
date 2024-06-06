
import csv
from Classes.station import *
from Classes.traject import *
from inladen import *

stationDict = verbinding()
print(stationDict["Alkmaar"])
T1 = Traject(stationDict['Hoorn'])
T1.add_trajectverbinding(stationDict["Alkmaar"])
T1.add_trajectverbinding(stationDict["Hoorn"])
print(T1._reistijd)
print(T1._trajectverbindingen)
print(T1._stations)
T2 = Traject(stationDict["Alkmaar"])

filename = 'TestTraject.csv'

with open(filename, 'w', newline="") as file:
    writer = csv.writer(file,quoting=csv.QUOTE_NONE,
         quotechar='"', escapechar='\\')
    writer.writerows([T1._stations, T2._stations])

print("Jeei")