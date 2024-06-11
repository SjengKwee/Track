from algoritmes.random_algoritme import run_random_algoritme
from plotting.plot_trajectories import *
from bouwblokjes.inladen import *
from bouwblokjes.score import *

stations = make_connections()

random_results = run_random_times(stations, 10000)

print(random_results[1], random_results[3])
print("Het beste traject is: ")
for tracks in random_results[2]:
    print(tracks._stations)

print("Het slechtste traject is: ")
for tracks in random_results[4]:
    print(tracks._stations)

run_plot_random_alg_score(random_results[0])