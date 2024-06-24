from code.algoritmes.random_algoritme import *
from code.algoritmes.random_restricted import *
from code.algoritmes.random_restricted_2 import *
from code.algoritmes.random_restricted_3 import *
from code.algoritmes.greedy_apriori import *
from code.algoritmes.progressive_algorithm import Progressive_algorithm as pr
from code.algoritmes.hillClimber import *
from main_sjeng import *
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.score import *
from code.bouwblokjes.writer import *
from code.bouwblokjes.heur_maker import *
import sys

for repetitions in [1, 10, 100]:

    repetitions_name = str(repetitions)
        
    # holland
    stations = make_connections()
    number_connections = 28
    stations_file = 'StationsHolland.csv'
    traveltime = 120
    trains = 7
    times = 1000


    # random
    csvname = "data/output/progressive/holland/random/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/holland/random/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/holland/random/" + repetitions_name + "scores"
    progressive = pr.Progressive_algorithm(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

    # Connections
    csvname = "data/output/progressive/holland/connections/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/holland/connections/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/holland/connections/" + repetitions_name + "scores"
    progressive = pr.Progressive_connections(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

    # Stations
    csvname = "data/output/progressive/holland/stations/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/holland/stations/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/holland/stations/" + repetitions_name + "scores"
    progressive = pr.Progressive_stations(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

    # Filler
    csvname = "data/output/progressive/holland/filler/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/holland/filler/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/holland/filler/" + repetitions_name + "scores"
    progressive = pr.Progressive_filler(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

    # nederland
    stations = make_connections(stations_file = 'stationsnederland.csv', connecties_file = 'connectiesnederland.csv')
    number_connections = 89
    stations_file = 'stationsnederland.csv'
    traveltime = 180
    trains = 20
    times = 1000

    # random
    csvname = "data/output/progressive/nederland/random/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/nederland/random/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/nederland/random/" + repetitions_name + "scores"
    progressive = pr.Progressive_algorithm(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

    # Connections
    csvname = "data/output/progressive/nederland/connections/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/nederland/connections/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/nederland/connections/" + repetitions_name + "scores"
    progressive = pr.Progressive_connections(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

    # Stations
    csvname = "data/output/progressive/nederland/stations/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/nederland/stations/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/nederland/stations/" + repetitions_name + "scores"
    progressive = pr.Progressive_stations(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

    # Filler
    csvname = "data/output/progressive/nederland/filler/" + repetitions_name + "maximum"
    pngname = "data/images/progressive/nederland/filler/" + repetitions_name + "maximum"
    score_csv = "data/output/progressive/nederland/filler/" + repetitions_name + "scores"
    progressive = pr.Progressive_filler(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
    run_progressive_run_times(progressive, stations_file=stations_file, csv_location=csvname, png_location=pngname, score_csv=score_csv)

