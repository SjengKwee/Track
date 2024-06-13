from algoritmes.random_algoritme import *
from plotting.plot_trajectories import *
from bouwblokjes.inladen import *
from bouwblokjes.score import *
from bouwblokjes.writer import *

stations = make_connections()

random_results = run_random_times(stations, 10000)

print(random_results[1], random_results[3])
print("Het beste traject is: ")
for tracks in random_results[2]:
    print(tracks._stations)

print("Het slechtste traject is: ")
for tracks in random_results[4]:
    print(tracks._stations)

print("Het algoritme duurt", random_results[5], "seconden")
run_plot_random_alg_score(random_results[0], 'images/scores3_random_algoritme')


# write output for maximum score
tracks_writer(random_results[2], random_results[1], 'output/maximum3.csv')

# write output for minimum score
tracks_writer(random_results[4], random_results[3], 'output/minimum3.csv')
tracks_writer(random_results[6],random_results[7], 'output/medium3.csv')

# plot graph from written max score
run_plot_trajectories('output/maximum3.csv', 'images/max_7_track3.png')

# plot graph from written min score
run_plot_trajectories('output/minimum3.csv', 'images/min_7_track3.png')

run_plot_trajectories('output/medium3.csv', 'images/medium_7_track3.png')


