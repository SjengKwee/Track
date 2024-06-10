# Aangemaakt door Addey
# Inladen.py
# Hier plotten we een voorbeeld van trajecten

import csv
import matplotlib.pyplot as plt
from inladen import make_stations
import numpy as np

#Plot een track
def plot_track(track: list):
    """ elke track plotten"""
    stations = make_stations()
    stations_track  = track.strip('[]').replace("'",'' ).split(', ')
    
    y = [float(stations[station]._coordinates[0]) for station in stations_track]
    x = [float(stations[station]._coordinates[1]) for station in stations_track]
    return plt.plot(x,y)


def run_plot_trajectories():
        
    stations = make_stations()
    # data in list stoppen
    station_names = list(stations.keys())
    y = [float(stations[station]._coordinates[0]) for station in station_names]
    x = [float(stations[station]._coordinates[1]) for station in station_names]

    # afmeting aangeven en plotten 
    plt.figure(figsize=(15, 20))
    plt.scatter(x, y)

    # namen van stations weergeven
    for i, name in enumerate(station_names):
        plt.text(x[i], y[i], name, fontsize=12)

    # Gereden trajecten inlezen en plotten
    with open('TestTraject.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) 
        for row in csvreader:
            if row[0] == "Score:":
                break
            plot_track(row[1])
        
    # opslaan en weergeven
    plt.savefig('images/plot_zuid_noord.png') 
    plt.show()


def run_plot_random_alg_score():
    scores = []
    with open('random_algoritme_score.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            scores.append(row)
    plt.hist(scores, bins=30, density=True, alpha=0.6, color='g', label='Scores')
    plt.grid(True)
    plt.show()
