# Aangemaakt door Alec van Duin
# score.py
# Hier berekenen we de score van een lijst aan trajecten

from classes.traject import *

#Berekent de score
def score_calc(trajecten: list):
    ridenpairs = []
    T = len(trajecten)
    min = 0
    for traj in trajecten:
        min += traj._traveltime
        for connect in traj._trajectconnection:
            if (not connect in ridenpairs):
                ridenpairs.append(connect)

    p = len(ridenpairs)/28
    k = p*10000 - T*100 - min
    print(p)
    print(T)
    print(min)
    print(k)
    return k