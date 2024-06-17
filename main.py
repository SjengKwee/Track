from code.algoritmes.random_algoritme import *
from code.algoritmes.random_restricted import *
from code.algoritmes.random_restricted_2 import *
from code.algoritmes.random_restricted_3 import *
from code.algoritmes.greedy_apriori import *
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.score import *
from code.bouwblokjes.writer import *
import sys

random.seed(10)

stations = make_connections()

print("Welkom bij onze vette algoritmes")
print("Om onze random baseline te runnen: Random")
print("Om de restricted random nr 1 te runnen: Restricted_1")
print("Om de restricted random nr 2 te runnen: Restricted_2")
print("Om de restricted random nr 3 te runnen: Restricted_3")
print("Om een greedy algoritme met apriori heuristieken: Greedy_apri")
algoritme = input("Welk algoritme wil je runnen? ")

#Random algoritme
if(algoritme == "Random"):
    random_results = run_random_times(stations, 10000)
    print("Het algoritme duurt", random_results[5], "seconden")
    run_plot_random_alg_score(random_results[0], 'data/images/baseline/scores_random_algoritme')
    tracks_writer(random_results[2], random_results[1], 'data/output/baseline/maximum.csv')
    tracks_writer(random_results[4], random_results[3], 'data/output/baseline/minimum.csv')
    run_plot_trajectories('data/output/baseline/maximum.csv', 'data/images/baseline/max_7_track.png')
    run_plot_trajectories('data/output/baseline/minimum.csv', 'data/images/baseline/min_7_track.png')

#Restricted nr 1
elif(algoritme == "Restricted_1"):
    restr1_results = run_random_restr_times(stations,10000)
    print("Het algoritme duurt", restr1_results[5], "seconden")
    run_plot_random_alg_score(restr1_results[0], 'data/images/random_restricted_1/scores_random_algoritme')
    tracks_writer(restr1_results[2], restr1_results[1], 'data/output/random_restricted_1/maximum.csv')
    tracks_writer(restr1_results[4], restr1_results[3], 'data/output/random_restricted_1/minimum.csv')
    run_plot_trajectories('data/output/random_restricted_1/maximum.csv', 'data/images/random_restricted_1/max_7_track.png')
    run_plot_trajectories('data/output/random_restricted_1/minimum.csv', 'data/images/random_restricted_1/min_7_track.png')

#Restricted nr 2
elif(algoritme == "Restricted_2"):
    alg = Restricted_2(stations)
    restr2_results = alg.run_random_restr2_times(10000)
    print("Het algoritme duurt", restr2_results[5], "seconden")
    run_plot_random_alg_score(restr2_results[0], 'data/images/random_restr_2/scores_algoritme')
    tracks_writer(restr2_results[2], restr2_results[1], 'data/output/random_restr_2/maximum.csv')
    tracks_writer(restr2_results[4], restr2_results[3], 'data/output/random_restr_2/minimum.csv')
    run_plot_trajectories('data/output/random_restr_2/maximum.csv', 'data/images/random_restr_2/max_7_track.png')
    run_plot_trajectories('data/output/random_restr_2/minimum.csv', 'data/images/random_restr_2/min_7_track.png')

#Restricted nr 3
elif(algoritme == "Restricted_3"):
    alg = Restricted_3(stations)
    restr3_results = alg.run_random_restr3_times(10000)
    print("Het algoritme duurt", restr3_results[5], "seconden")
    run_plot_random_alg_score(restr3_results[0], 'data/images/random_restr_3/scores_algoritme')
    tracks_writer(restr3_results[2], restr3_results[1], 'data/output/random_restr_3/maximum.csv')
    tracks_writer(restr3_results[4], restr3_results[3], 'data/output/random_restr_3/minimum.csv')
    run_plot_trajectories('data/output/random_restr_3/maximum.csv', 'data/images/random_restr_3/max_7_track.png')
    run_plot_trajectories('data/output/random_restr_3/minimum.csv', 'data/images/random_restr_3/min_7_track.png')

#Greedy_apri
elif(algoritme == "Greedy_apri"):
    print("Voor een even verdeelde standaard heuristiek: Basic")
    heuristiek = input("Welke heuristiek wil je gebruiken? ")
    if(heuristiek == "Basic"):
        heur_stat = stations
        alg = Greedy_apri(heur_stat)
        greed_results = alg.run_greedy_times(10000)
        print("Het algoritme duurt", greed_results[5], "seconden")
        run_plot_random_alg_score(greed_results[0], 'data/images/greed_apri/zonder_heur/scores_algoritme')
        tracks_writer(greed_results[2], greed_results[1], 'data/output/greed_apri/zonder_heur/maximum.csv')
        tracks_writer(greed_results[4], greed_results[3], 'data/output/greed_apri/zonder_heur/minimum.csv')
        run_plot_trajectories('data/output/greed_apri/zonder_heur/maximum.csv', 'data/images/greed_apri/zonder_heur/max_track.png')
        run_plot_trajectories('data/output/greed_apri/zonder_heur/minimum.csv', 'data/images/greed_apri/zonder_heur/min_track.png')

    else:
        print("Verkeerde input")
    
else:
    print("Verkeerde input")
