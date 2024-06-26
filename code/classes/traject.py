# Aangemaakt door Alec van Duin
# Traject.py
# Hier definieren we de traject class. Het leek me netjes de classes in aparte files te definieren

from code.classes.station import *
from code.classes.connection import Connection

class Traject():

    def __init__(self, start_station):
        """
        Maakt een traject aan met beginstation zonder verbindingen
        """

        self._trajectconnection = []
        self._stations = [start_station._name]
        self._traveltime: int = 0
        self._endstation: Station = start_station

    def add_trajectconnection(self, station) -> None:
        """
        Voegt een verbinding toe aan een traject
        """

        stationTuple = self._endstation._connection[station._name]
        time = float(stationTuple[1])
        self._traveltime += time
        newConn = Connection()
        newConn.add(self._endstation._name)
        newConn.add(station._name)
        self._trajectconnection.append(newConn)
        self._endstation = stationTuple[0]
        self._stations.append(station._name)

    def __repr__(self):
        return f"traject{self._stations}"
        # return f" {self._trajectconnection}"
