# Aangemaakt door Alec van Duin
# score.py
# Hier berekenen we de score van een lijst aan trajecten

from code.classes.traject import *

#Berekent de score
def score_calc(trajecten: list) -> int:
    """
    Berekent de score van een lijst aan trajecten
    """

    #Initialiseert parameters
    ridenpairs = []
    T = len(trajecten)
    min = 0

    #Runt door trajecten en kijkt score
    for traj in trajecten:
        min += traj._traveltime
        for connect in traj._trajectconnection:
            if (not connect in ridenpairs):
                ridenpairs.append(connect)

    #Berekent laatste stukjes
    p = len(ridenpairs)/28
    k = p*10000 - T*100 - min

    #Return
    return k