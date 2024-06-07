# Aangemaakt door Addey
# Inladen.py
# Hier plotten we een voorbeeld van trajecten

import csv
import matplotlib.pyplot as plt
from inladen import make_stations

#Plot een track
def plot_track(track: list):
    """ elke track plotten"""
    stations = make_stations()
    stations_track  = row[1].strip('[]').replace("'",'' ).split(', ')
    y = [float(stations[station]._coordinates[0]) for station in stations_track]
    x = [float(stations[station]._coordinates[1]) for station in stations_track]
    return plt.plot(x,y)

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
        plot_track(row[1])
    
# opslaan en weergeven
plt.savefig('images/plot_zuid_noord.png') 
plt.show()


