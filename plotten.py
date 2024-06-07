#  sudo apt-get install python3-matplotlib 


import matplotlib.pyplot as plt
from inladen import make_stations



stations = make_stations()

station_names = list(stations.keys())
y = [float(stations[station]._coordinates[0]) for station in station_names]
x = [float(stations[station]._coordinates[1]) for station in station_names]
#print(st["Hoorn"]._coordinates[0])
#print(stations["Hoorn"]._x)


plt.figure(figsize=(15, 20))
plt.scatter(x, y)

for i, name in enumerate(station_names):
    plt.text(x[i], y[i], name, fontsize=9)
    
# plt.grid(True)
plt.savefig('images/plot_zuid_noord.png') 

plt.show()


