from code.algoritmes.random_algoritme import *
from code.algoritmes.random_restricted import *
from code.algoritmes import progressive_algorithm as pr
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.score import *
from code.bouwblokjes.writer import *
import time

def run_progressive_run(algorithm, stations_file, csvname = 'None'):
        
    # run algorithm keeping track of runtime
    time0 = time.time()
    algorithm.run()
    time1 = time.time()

    # print maximumscore, print maximumtrack
    for track in algorithm.max_tracks.keys():
        print("beste score bij", (track+1),"tracks:", algorithm.max_scores[track])

    # print runtime
    print("runtime:", (time1 - time0))

    # plot score verdeling per hoeveelheid tracks

    # output in csv voor maximumtraject per hoeveelheid tracks
    for track in algorithm.max_tracks.keys():

        # generate track list
        track_list = []
        for i in range(track+1):
            track_list.append(algorithm.max_tracks[i])

        # generate filenames
        csvname = "data/output/random_progressive_output/maximum" + str(track+1) + "tracks.csv"
        pngname = "data/images/random_progressive_images/maximum" + str(track+1) + "tracks.png"
        tracks_writer(track_list, algorithm.max_scores[track], csvname)

        # # plot maximumtraject voor maximumtraject per hoeveelheid tracks

        # run_plot_trajectories(csvname, pngname)


def run_progressive_run_times(algorithm, stations_file, csv_location = 'data/output/random_progressive_output/maximum' , png_location = 'data/images/random_progressive_images/maximum', score_csv = 'data/output/random_progressive_output/scores'):
        
    # run algorithm keeping track of runtime
    time0 = time.time()
    algorithm.run_times()
    time1 = time.time()

    # print maximumscore, print maximumtrack
    for track in algorithm.best_max_tracks.keys():
        print("beste score bij", (track+1),"tracks:", algorithm.best_max_scores[track])
        absolutebest = algorithm.best_max_scores[track]

    # print runtime
    print("runtime:", (time1 - time0))

    # plot score verdeling per hoeveelheid tracks

    # output in csv voor maximumtraject per hoeveelheid tracks
    for track in algorithm.best_max_tracks.keys():

        # generate track list
        track_list = []
        for i in range(track+1):
            track_list.append(algorithm.best_max_tracks[i])


        # generate filenames if not given
        csvname = csv_location + str(track+1) + "tracks.csv"
        pngname = png_location + str(track+1) + "tracks.png"

        # write csv
        tracks_writer(track_list, algorithm.best_max_scores[track], csvname)

        # plot best score per added track
        run_plot_trajectories(csvname, pngname, stations_file = stations_file)

    # output alle scores
    scorename = score_csv
    all_scores = algorithm.all_max_scores
    gem_score = (sum(all_scores)/len(all_scores))

    scores_writer(score_csv, highscore=absolutebest, average=gem_score, all_scores=all_scores)

    # plot verdeling van de scores
    run_plot_random_alg_score(algorithm.all_max_scores, png_location + "plot.png")
