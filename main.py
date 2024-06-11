from algoritmes.random_algoritme import run_random_algoritme
from plotting.plot_trajectories import *
from bouwblokjes.inladen import *
from bouwblokjes.score import *

stations = make_connections()
score_list = []
for i in range(100):
    traj = run_random_algoritme(stations)
    score_list.append(score_calc(traj))

run_plot_random_alg_score(score_list)