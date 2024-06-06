# Aangemaakt door Alec van Duin
# Station.py
# Hier definieren we de station class. Het leek me netjes de classes in aparte files te definieren

class Station():
    def __init__(self, naam : str):
        """
        Maakt een station zonder verbindingen
        """

        self._name: str = naam  
        # met welke stations de station verbinding heeft
        self._verbinding: dict = {}

    def add_verbinding(self,station, duur: int) -> None:
        """
        Voegt een verbinding toe naar station met bepaalde duur
        """

        verbinding = {station._name: (station, duur)}
        self._verbinding[station._name] = verbinding

    def __repr__(self):
        return f"Station({self._name})"