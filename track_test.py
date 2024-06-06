
import csv
from Classes.station import *
from Classes.traject import *
from inladen import *

stationDict = make_connections()
print(stationDict["Alkmaar"])
T1 = Traject(stationDict['Hoorn'])
T1.add_trajectconnection(stationDict["Alkmaar"])
T1.add_trajectconnection(stationDict["Hoorn"])
print(T1._traveltime)
print(T1._trajectconnection)
print(T1._stations)
T2 = Traject(stationDict["Alkmaar"])

filename = 'TestTraject.csv'

with open(filename, 'w', newline="") as file:
    writer = csv.writer(file,quoting=csv.QUOTE_NONE,
         quotechar='"', escapechar='\\')
    writer.writerows([T1._stations, T2._stations])

print("Jeei")