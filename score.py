# Aangemaakt door Alec van Duin
# score.py
# Hier berekenen we de score van een lijst aan trajecten

from Classes.Traject import *

#Berekent de score
def score_calc(trajecten: list):
    ridenpairs = []
    T = 0
    min = 0
    for traj in trajecten:
        min += traj._traveltime
        T += len(traj._stations) - 1
        for connect in traj._trajectconnection:
            if (not connect in ridenpairs):
                ridenpairs.append(connect)

    p = len(ridenpairs)/28
    k = p*1000 - T*100 - min
    return k