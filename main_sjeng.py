from code.algoritmes.random_algoritme import *
from code.algoritmes.random_restricted import *
from code.algoritmes import progressive_algorithm as pr
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.score import *
from code.bouwblokjes.writer import *
import time

stations = make_connections()

random_progressive_results = pr.Progressive_algorithm(stations)

# run algorithm keeping track of runtime
time0 = time.time()
random_progressive_results.run()
time1 = time.time()

# print maximumscore, print maximumtrack
for track in random_progressive_results.max_tracks.keys():
    print("beste score bij", track,"tracks:", random_progressive_results.max_scores[track])

# plot score verdeling per hoeveelheid tracks

# output in csv voor maximumtraject per hoeveelheid tracks

# plot maximumtraject voor maximumtraject per hoeveelheid tracks


# print(random_results[1], random_results[3])
# print("Het beste traject is: ")
# for tracks in random_results[2]:
#     print(tracks._stations)

# print("Het slechtste traject is: ")
# for tracks in random_results[4]:
#     print(tracks._stations)

# print("Het algoritme duurt", random_results[5], "seconden")
# run_plot_random_alg_score(random_results[0], 'data/images/scores3_random_algoritme')

# # write output for maximum score
# tracks_writer(random_results[2], random_results[1], 'data/output/maximum3.csv')

# # plot graph from written max score
# run_plot_trajectories('data/output/maximum3.csv', 'data/images/max_7_track3.png')



