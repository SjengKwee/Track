from algoritmes.random_algoritme import run_random_algoritme
from plotting.plot_trajectories import *
from bouwblokjes.inladen import *
from bouwblokjes.score import *

stations = make_connections()
score_list = []
max_score = 0
min_score = 10000

for i in range(10000):
    traj = run_random_algoritme(stations)
    score_list.append(score_calc(traj))
    if score_calc(traj) > max_score:
        max_score = score_calc(traj)
        max_traj = traj
    elif score_calc(traj) < min_score:
        min_score = score_calc(traj)
        min_traj = traj

print(max_score, min_score)
print("Het beste traject is: ")
for tracks in max_traj:
    print(tracks._stations)
    
print("Het slechtste traject is: ")
for tracks in min_traj:
    print(tracks._stations)

run_plot_random_alg_score(score_list)