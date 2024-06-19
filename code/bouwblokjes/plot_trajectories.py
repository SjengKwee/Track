# Aangemaakt door Addey
# Hier plotten we een voorbeeld van trajecten

import csv
import matplotlib.pyplot as plt
from code.bouwblokjes.inladen import make_stations
import numpy as np


def plot_track(track: list, stations_file = 'StationsHolland.csv'):
    """ Visualisatie code die matplotlib gebruikt om elke track te plotten"""
    stations = make_stations(stations_file=stations_file)

    # data bruikbaar maken voor plotten 
    stations_track  = track.strip('[]').replace("'",'' ).split(', ')
    
    y = [float(stations[station]._coordinates[0]) for station in stations_track]
    x = [float(stations[station]._coordinates[1]) for station in stations_track]
    return plt.plot(x,y)


def run_plot_trajectories(csv_file, save_file, stations_file = 'StationsHolland.csv'):
    """ Namen van stations plotten op de juiste plaats en de functie plot_track aanroepen. """
        
    stations = make_stations(stations_file = stations_file)
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
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) 
        for row in csvreader:
            if row[0] == "Score:":
                break
            plot_track(row[1], stations_file=stations_file)
        
    # opslaan en weergeven
    plt.savefig(save_file) 
    plt.show()


def run_plot_random_alg_score(scores, save_file):
    """ Scores van random algoritme plotten in een histogram. """
    # plotten 
    plt.hist(scores, bins=20, density=True, alpha=0.6, color='g', label='Scores')
    plt.grid(True)
    
    # opslaan en weergeven
    plt.savefig(save_file) 
    plt.show()

def plot_iterations_scores(scores,iterations, save_file):
    
    """ Scores van een algoritme plotten """
    y = [score for score in scores]
    x = [iteration for iteration in range(iterations)]
    plt.plot(x,y)
    plt.savefig(save_file) 
    plt.show()


