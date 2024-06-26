# Aangemaakt door Sjeng
# Connection.py

class Connection(set):

    def __hash__(self):
        items = tuple(self)
        if hash(items[0]) > hash(items[1]):
            items = (items[1], items[0])
        return hash(items)
    
    def endstation(self, startstation):
        """
        Returnt het station waarmee het gegeven station door deze connectie is verbonden
        """
        items = tuple(self)
        if items[0] == startstation:
            return items[1]
        elif items[1] == startstation:
            return items[0]
    
    def has(self, station):
        """
        Checkt of een station in deze connectie zit
        """

        items = tuple(self)
        if items[0] == station:
            return True
        elif items[1] == station:
            return True
        else:
            return False
