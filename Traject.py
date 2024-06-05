# Aangemaakt door Alec van Duin
# Traject.py
# Hier definieren we de traject class. Het leek me netjes de classes in aparte files te definieren

class Traject():

    def __init__(self, start_station: Station):
        """
        Maakt een traject aan met beginstation zonder verbindingen
        """

        self._trajectverbindingen: set = {}
        self._reistijd: int = 0
        self._eindstation: Station = start_station

    def add_trajectverbinding(self, station: Station) -> None:
        """
        Voegt een verbinding toe aan een traject
        """

        if station._name in self._eindstation._verbinding:
            self._reistijd += self._eindstation._verbinding[station._name][1]
            self._trajectverbindingen.add({self._eindstation._name, station._name})
            self._eindstation = self._eindstation._verbinding[station._name][0]
