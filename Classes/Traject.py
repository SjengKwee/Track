# Aangemaakt door Alec van Duin
# Traject.py
# Hier definieren we de traject class. Het leek me netjes de classes in aparte files te definieren

from Classes.station import *

class Traject():

    def __init__(self, start_station):
        """
        Maakt een traject aan met beginstation zonder verbindingen
        """

        self._trajectverbindingen = []
        self._stations = [start_station._name]
        self._reistijd: int = 0
        self._eindstation: Station = start_station

    def add_trajectverbinding(self, station) -> None:
        """
        Voegt een verbinding toe aan een traject
        """

        if station._name in self._eindstation._verbinding:
            stationTuple = self._eindstation._verbinding[station._name]
            tijd = int(stationTuple[1])
            self._reistijd += tijd
            newVerb = set()
            newVerb.add(self._eindstation._name)
            newVerb.add(station._name)
            self._trajectverbindingen.append(newVerb)
            self._eindstation = stationTuple[0]
            self._stations.append(station._name)
