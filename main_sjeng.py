from code.algoritmes.random_algoritme import *
from code.algoritmes.random_restricted import *
from code.algoritmes import progressive_algorithm as pr
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.score import *
from code.bouwblokjes.writer import *
import time

stations = make_connections()

random_progressive = pr.Progressive_connections(stations, repetitions=1000)

def run_progressive_run():
        
    # run algorithm keeping track of runtime
    time0 = time.time()
    random_progressive.run()
    time1 = time.time()

    # print maximumscore, print maximumtrack
    for track in random_progressive.max_tracks.keys():
        print("beste score bij", (track+1),"tracks:", random_progressive.max_scores[track])

    # print runtime
    print("runtime:", (time1 - time0))

    # plot score verdeling per hoeveelheid tracks

    # output in csv voor maximumtraject per hoeveelheid tracks
    for track in random_progressive.max_tracks.keys():

        # generate track list
        track_list = []
        for i in range(track+1):
            track_list.append(random_progressive.max_tracks[i])

        # generate filenames
        csvname = "data/output/random_progressive_output/maximum" + str(track+1) + "tracks.csv"
        pngname = "data/images/random_progressive_images/maximum" + str(track+1) + "tracks.png"
        tracks_writer(track_list, random_progressive.max_scores[track], csvname)

        # # plot maximumtraject voor maximumtraject per hoeveelheid tracks

        # run_plot_trajectories(csvname, pngname)


def run_progressive_run_times():
        
    # run algorithm keeping track of runtime
    time0 = time.time()
    random_progressive.run_times()
    time1 = time.time()

    # print maximumscore, print maximumtrack
    for track in random_progressive.all_max_tracks.keys():
        print("beste score bij", (track+1),"tracks:", random_progressive.all_max_scores[track])

    # print runtime
    print("runtime:", (time1 - time0))

    # plot score verdeling per hoeveelheid tracks

    # output in csv voor maximumtraject per hoeveelheid tracks
    for track in random_progressive.all_max_tracks.keys():

        # generate track list
        track_list = []
        for i in range(track+1):
            track_list.append(random_progressive.all_max_tracks[i])

        # generate filenames
        csvname = "data/output/random_progressive_output/maximum" + str(track+1) + "tracks.csv"
        pngname = "data/images/random_progressive_images/maximum" + str(track+1) + "tracks.png"

        # write csv
        tracks_writer(track_list, random_progressive.all_max_scores[track], csvname)

        # plot best score per added track
        run_plot_trajectories(csvname, pngname)

        # run_plot_trajectories(csvname, pngname)

run_progressive_run_times()