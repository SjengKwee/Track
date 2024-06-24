# Aangemaakt door Addey

import csv
import matplotlib.pyplot as plt
import pandas as pd
from code.bouwblokjes.inladen import make_stations
import numpy as np
from adjustText import adjust_text


def plot_track(track: list, stations_file = 'StationsHolland.csv'):
    """ Visualisatie code die matplotlib gebruikt om elke track te plotten"""
    stations = make_stations(stations_file=stations_file)

    # data bruikbaar maken voor plotten 
    stations_track  = track.strip('[]').replace("'",'' ).split(', ')
    
    y = [float(stations[station]._coordinates[0]) for station in stations_track]
    x = [float(stations[station]._coordinates[1]) for station in stations_track]
    return plt.plot(x,y)


def run_plot_trajectories(csv_file, save_file, stations_file = 'StationsHolland.csv'):
    """Namen van stations plotten op de juiste plaats en de functie plot_track aanroepen."""
        
    stations = make_stations(stations_file = stations_file)
    # data in list stoppen
    station_names = list(stations.keys())
    y = [float(stations[station]._coordinates[0]) for station in station_names]
    x = [float(stations[station]._coordinates[1]) for station in station_names]

    # afmeting aangeven en plotten 
    plt.figure(figsize=(15, 20))
    plt.scatter(x, y)

    # namen van stations weergeven
    texts = []
    if stations_file == 'StationsHolland.csv':

        
        for i, name in enumerate(station_names):
            texts.append(plt.text(x[i], y[i], name, fontsize=18))

    # Gereden trajecten inlezen en plotten
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) 
        for row in csvreader:
            if row[0] == "Score:":
                break
            plot_track(row[1], stations_file=stations_file)
        
    # opslaan en weergeven'
    adjust_text(texts)
    plt.title("Weergave van verbindingen", fontsize=25)
    plt.savefig(save_file) 


def run_plot_random_alg_score(scores, save_file,titel='Histogram van Algoritme Scores' ):
    """ Scores van algoritme plotten in een histogram. """
    # plotten 
    plt.figure(figsize=(15, 15))
    plt.hist(scores, bins=20, density=True, alpha=0.6, color='g', label='Scores')
    plt.grid(True)
    plt.xlabel('Score', fontsize=16)  
    plt.ylabel('Dichtheid', fontsize=16)  
    plt.title(titel, fontsize=20)
    # opslaan en weergeven
    plt.savefig(save_file) 
    plt.show()

def plot_iterations_scores(scores,iterations, save_file, titel='Score per iteratie'):
    
    """ Score na elke iteratie plotten """
    y = [score for score in scores]
    x = [iteration for iteration in range(iterations)]
    plt.figure(figsize=(14, 10))
    plt.plot(x,y)
    
    plt.xlabel('Iteratie', fontsize=16)  
    plt.ylabel('Score', fontsize=16)  
    plt.title(titel,fontsize=20)
    plt.savefig(save_file) 
    plt.show()


def plot_meer_histogrammen(data1_x, data2_x, data3_x, data4_x,save_file):

    # Laad de data van de Excel-bestanden, waarbij de eerste twee rijen worden overgeslagen
    data1 = pd.read_excel(data1_x, skiprows=2).values.flatten()
    data2 = pd.read_excel(data2_x, skiprows=2).values.flatten()
    data3 = pd.read_excel(data3_x, skiprows=2).values.flatten()
    data4 = pd.read_excel(data4_x, skiprows=2).values.flatten()

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # Bepaal de gemeenschappelijke grenzen voor de assen
    all_data = np.concatenate([data1, data2, data3, data4])
    x_min, x_max = min(all_data), max(all_data)
    y_max = max(max(np.histogram(data1, bins=30)[0]), 
                max(np.histogram(data2, bins=30)[0]), 
                max(np.histogram(data3, bins=30)[0]), 
                max(np.histogram(data4, bins=30)[0]))

    # Eerste histogram
    axes[0, 0].hist(data1, bins=30, alpha=0.75, color='blue')
    axes[0, 0].set_title('Histogram 1')
    axes[0, 0].set_xlim(x_min, x_max)
    axes[0, 0].set_ylim(0, y_max)

    # Tweede histogram
    axes[0, 1].hist(data2, bins=30, alpha=0.75, color='green')
    axes[0, 1].set_title('Histogram 2')
    axes[0, 1].set_xlim(x_min, x_max)
    axes[0, 1].set_ylim(0, y_max)

    # Derde histogram
    axes[1, 0].hist(data3, bins=30, alpha=0.75, color='red')
    axes[1, 0].set_title('Histogram 3')
    axes[1, 0].set_xlim(x_min, x_max)
    axes[1, 0].set_ylim(0, y_max)

    # Vierde histogram
    axes[1, 1].hist(data4, bins=30, alpha=0.75, color='purple')
    axes[1, 1].set_title('Histogram 4')
    axes[1, 1].set_xlim(x_min, x_max)
    axes[1, 1].set_ylim(0, y_max)

    plt.tight_layout()
    plt.show()
