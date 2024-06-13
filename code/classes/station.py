# Aangemaakt door Alec van Duin
# Station.py
# Hier definieren we de station class. Het leek me netjes de classes in aparte files te definieren

class Station():
    def __init__(self, name : str, coordinates):
        """
        Maakt een station zonder verbindingen
        """

        self._name: str = name
        self._coordinates = coordinates
      
        # met welke stations de station verbinding heeft
        self._connection: dict = {}

    def add_connection(self,station, length: int) -> None:
        """
        Voegt een verbinding toe naar station met bepaalde duur
        """

        connection = (station, length)
        self._connection[station._name] = connection
    
    def __repr__(self):
        return f"Station({self._name})"


    