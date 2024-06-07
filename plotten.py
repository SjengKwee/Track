#  sudo apt-get install python3-matplotlib 


import matplotlib.pyplot as plt
from inladen import make_stations

stations = make_stations()

# data in een list stoppen
station_names = list(stations.keys())
y = [float(stations[station]._coordinates[0]) for station in station_names]
x = [float(stations[station]._coordinates[1]) for station in station_names]

# afmeting en plotten 
plt.figure(figsize=(15, 20))
plt.scatter(x, y)

# namen van stations weergeven
for i, name in enumerate(station_names):
    plt.text(x[i], y[i], name, fontsize=12)

# plt.grid(True
# opslaan en weergeven
plt.savefig('images/plot_zuid_noord.png') 
plt.show()


