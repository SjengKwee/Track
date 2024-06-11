from algoritmes.random_algoritme import run_random_algoritme
from plotting.plot_trajectories import run_plot_trajectories
from bouwblokjes.inladen import *

stations = make_connections()

run_random_algoritme(stations)


run_plot_trajectories()