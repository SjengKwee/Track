# Aangemaakt door Alec van Duin
# score.py
# Hier berekenen we de score van een lijst aan trajecten

from Classes.Traject import *

#Berekent de score
def score_calc(stations: dict, trajecten: list):
    station_list = list(stations.keys())
    pairs = [{a, b} for idx, a in enumerate(station_list) for b in station_list[idx + 1:]]

    ridenpairs = []
    T = 0
    min = 0
    for traj in trajecten:
        min += traj._traveltime
        T += len(traj._stations) - 1
        for connect in traj._trajectconnection:
            if (connect in pairs) & (not connect in ridenpairs):
                ridenpairs.append(connect)

    p = len(ridenpairs)/len(pairs)
    k = p*1000 - T*100 - min
    return k