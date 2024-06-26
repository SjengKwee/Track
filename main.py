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
from itertools import combinations

if __name__ == "__main__":
    random.seed(10)

    print("Welkom bij onze vette algoritmes")
    print("Wil je runnen voor holland of nederland?")
    regio = input("kies: holland / nederland \n")
    if(regio == "holland"):
        stations = make_connections()
        number_connections = 28
        stations_file = 'StationsHolland.csv'
        traveltime = 120
        trains = 7
        connecties_file = 'ConnectiesHolland.csv'
    elif(regio == "nederland"):
        stations = make_connections(stations_file = 'stationsnederland.csv', connecties_file = 'connectiesnederland.csv')
        number_connections = 89
        stations_file = 'stationsnederland.csv'
        traveltime = 180
        trains = 20
        connecties_file = 'connectiesnederland.csv'

    print("Om onze random baseline te runnen: Random")
    print("Om de restricted random nr 1 te runnen: Restricted_1")
    print("Om de restricted random nr 2 te runnen: Restricted_2")
    print("Om de restricted random nr 3 te runnen: Restricted_3")
    print("Om een greedy algoritme met apriori heuristieken: Greedy_apri")
    print('Om een progressive algoritme te runnen: Progressive')
    print('Om Hill climber te runnen type: Hill Climber')
    algoritme = input("Welk algoritme wil je runnen? ")

    #Random algoritme
    if(algoritme == "Random"):
        random_results = run_random_times(stations, 100000, number_connections, traveltime, trains)
        print("Het algoritme duurt", random_results[5], "seconden")
        run_plot_random_alg_score(random_results[0], 'data/images/baseline/scores_random_algoritme')
        tracks_writer(random_results[2], random_results[1], 'data/output/baseline/maximum.csv')
        tracks_writer(random_results[4], random_results[3], 'data/output/baseline/minimum.csv')
        run_plot_trajectories('data/output/baseline/maximum.csv', 'data/images/baseline/max_7_track.png', stations_file)
        run_plot_trajectories('data/output/baseline/minimum.csv', 'data/images/baseline/min_7_track.png', stations_file)

    #Restricted nr 1
    elif(algoritme == "Restricted_1"):
        restr1_results = run_random_restr_times(stations,10000, number_connections)
        print("Het algoritme duurt", restr1_results[5], "seconden")
        run_plot_random_alg_score(restr1_results[0], 'data/images/random_restr_1/scores_random_algoritme')
        tracks_writer(restr1_results[2], restr1_results[1], 'data/output/random_restr_1/maximum.csv')
        tracks_writer(restr1_results[4], restr1_results[3], 'data/output/random_restr_1/minimum.csv')
        run_plot_trajectories('data/output/random_restr_1/maximum.csv', 'data/images/random_restr_1/max_7_track.png', stations_file)
        run_plot_trajectories('data/output/random_restr_1/minimum.csv', 'data/images/random_restr_1/min_7_track.png', stations_file)

    #Restricted nr 2
    elif(algoritme == "Restricted_2"):
        alg = Restricted_2(stations)
        restr2_results = alg.run_random_restr2_times(10000, number_connections)
        print("Het algoritme duurt", restr2_results[5], "seconden")
        run_plot_random_alg_score(restr2_results[0], 'data/images/random_restr_2/scores_algoritme')
        tracks_writer(restr2_results[2], restr2_results[1], 'data/output/random_restr_2/maximum.csv')
        tracks_writer(restr2_results[4], restr2_results[3], 'data/output/random_restr_2/minimum.csv')
        run_plot_trajectories('data/output/random_restr_2/maximum.csv', 'data/images/random_restr_2/max_7_track.png', stations_file)
        run_plot_trajectories('data/output/random_restr_2/minimum.csv', 'data/images/random_restr_2/min_7_track.png', stations_file)

    #Restricted nr 3
    elif(algoritme == "Restricted_3"):
        alg = Restricted_3(stations)
        restr3_results = alg.run_random_restr3_times(10000, number_connections)
        print("Het algoritme duurt", restr3_results[5], "seconden")
        run_plot_random_alg_score(restr3_results[0], 'data/images/random_restr_3/scores_algoritme')
        tracks_writer(restr3_results[2], restr3_results[1], 'data/output/random_restr_3/maximum.csv')
        tracks_writer(restr3_results[4], restr3_results[3], 'data/output/random_restr_3/minimum.csv')
        run_plot_trajectories('data/output/random_restr_3/maximum.csv', 'data/images/random_restr_3/max_7_track.png', stations_file)
        run_plot_trajectories('data/output/random_restr_3/minimum.csv', 'data/images/random_restr_3/min_7_track.png', stations_file)

    #Greedy_apri
    elif(algoritme == "Greedy_apri"):
        print("Voor een even verdeelde standaard heuristiek: Basic")
        print("Voor een heuristiek gebasseerd het aantal verbindingen van groot naar klein: Max_connections")
        print("Voor een heuristiek gebasseerd op de minimale traveltime: Min_traveltime")
        heuristiek = input("Welke heuristiek wil je gebruiken? ")

        #Geen heuristiek
        if(heuristiek == "Basic"):
            heur_stat = stations
            alg = Greedy_apri(heur_stat)
            greed_results = alg.run_greedy_times(100000, number_connections, traveltime, trains)
            print("Het algoritme duurt", greed_results[5], "seconden")
            run_plot_random_alg_score(greed_results[0], 'data/images/greed_apri/zonder_heur/scores_algoritme')
            tracks_writer(greed_results[2], greed_results[1], 'data/output/greed_apri/zonder_heur/maximum.csv')
            tracks_writer(greed_results[4], greed_results[3], 'data/output/greed_apri/zonder_heur/minimum.csv')
            run_plot_trajectories('data/output/greed_apri/zonder_heur/maximum.csv', 'data/images/greed_apri/zonder_heur/max_track.png', stations_file)
            run_plot_trajectories('data/output/greed_apri/zonder_heur/minimum.csv', 'data/images/greed_apri/zonder_heur/min_track.png', stations_file)

        #Max connections heuristiek
        elif(heuristiek == "Max_connections"):
            heur_stat = max_connection_counter(stations)
            alg = Greedy_apri(heur_stat)
            greed_results = alg.run_greedy_times(100000, number_connections, traveltime, trains)
            print("Het algoritme duurt", greed_results[5], "seconden")
            run_plot_random_alg_score(greed_results[0], 'data/images/greed_apri/max_connections/scores_algoritme')
            tracks_writer(greed_results[2], greed_results[1], 'data/output/greed_apri/max_connections/maximum.csv')
            tracks_writer(greed_results[4], greed_results[3], 'data/output/greed_apri/max_connections/minimum.csv')
            run_plot_trajectories('data/output/greed_apri/max_connections/maximum.csv', 'data/images/greed_apri/max_connections/max_track.png', stations_file)
            run_plot_trajectories('data/output/greed_apri/max_connections/minimum.csv', 'data/images/greed_apri/max_connections/min_track.png', stations_file)

        #Min traveltime heuristiek
        elif(heuristiek == "Min_traveltime"):
            heur_stat = min_traveltime(stations)
            alg = Greedy_apri(heur_stat)
            greed_results = alg.run_greedy_times(100000, number_connections, traveltime, trains)
            print("Het algoritme duurt", greed_results[5], "seconden")
            run_plot_random_alg_score(greed_results[0], 'data/images/greed_apri/min_traveltime/scores_algoritme')
            tracks_writer(greed_results[2], greed_results[1], 'data/output/greed_apri/min_traveltime/maximum.csv')
            tracks_writer(greed_results[4], greed_results[3], 'data/output/greed_apri/min_traveltime/minimum.csv')
            run_plot_trajectories('data/output/greed_apri/min_traveltime/maximum.csv', 'data/images/greed_apri/min_traveltime/max_track.png', stations_file)
            run_plot_trajectories('data/output/greed_apri/min_traveltime/minimum.csv', 'data/images/greed_apri/min_traveltime/min_track.png', stations_file)

        #Min combi heuristiek
        elif(heuristiek == "Combi"):
            heur_stat1 = combi(stations,1,1)
            alg1 = Greedy_apri(heur_stat1)
            greed1_results = alg1.run_greedy_times(100000, traveltime, trains)
            print("De eerste combinatie duurt", greed1_results[5], "seconden")
            run_plot_random_alg_score(greed1_results[0], 'data/images/greed_apri/combi/1,1/scores_algoritme')
            tracks_writer(greed1_results[2], greed1_results[1], 'data/output/greed_apri/combi/1,1/maximum.csv')
            tracks_writer(greed1_results[4], greed1_results[3], 'data/output/greed_apri/combi/1,1/minimum.csv')
            run_plot_trajectories('data/output/greed_apri/combi/1,1/maximum.csv', 'data/images/greed_apri/combi/1,1/max_track.png', stations_file)
            run_plot_trajectories('data/output/greed_apri/combi/1,1/minimum.csv', 'data/images/greed_apri/combi/1,1/min_track.png', stations_file)

            heur_stat2 = combi(stations,1,2)
            alg2 = Greedy_apri(heur_stat2)
            greed2_results = alg2.run_greedy_times(10000)
            print("De tweede combinatie duurt", greed2_results[5], "seconden")
            run_plot_random_alg_score(greed2_results[0], 'data/images/greed_apri/combi/1,2/scores_algoritme')
            tracks_writer(greed2_results[2], greed2_results[1], 'data/output/greed_apri/combi/1,2/maximum.csv')
            tracks_writer(greed2_results[4], greed2_results[3], 'data/output/greed_apri/combi/1,2/minimum.csv')
            run_plot_trajectories('data/output/greed_apri/combi/1,2/maximum.csv', 'data/images/greed_apri/combi/1,2/max_track.png', stations_file)
            run_plot_trajectories('data/output/greed_apri/combi/1,2/minimum.csv', 'data/images/greed_apri/combi/1,2/min_track.png', stations_file)

            heur_stat3 = combi(stations,2,1)
            alg3 = Greedy_apri(heur_stat3)
            greed3_results = alg3.run_greedy_times(10000)
            print("De derde combinatie duurt", greed3_results[5], "seconden")
            run_plot_random_alg_score(greed3_results[0], 'data/images/greed_apri/combi/2,1/scores_algoritme')
            tracks_writer(greed3_results[2], greed3_results[1], 'data/output/greed_apri/combi/2,1/maximum.csv')
            tracks_writer(greed3_results[4], greed3_results[3], 'data/output/greed_apri/combi/2,1/minimum.csv')
            run_plot_trajectories('data/output/greed_apri/combi/2,1/maximum.csv', 'data/images/greed_apri/combi/2,1/max_track.png', stations_file)
            run_plot_trajectories('data/output/greed_apri/combi/2,1/minimum.csv', 'data/images/greed_apri/combi/2,1/min_track.png', stations_file)

        else:
            print("Verkeerde input")

    # Progressive_algorithm
    elif(algoritme == "Progressive"):
        print("Voor een greedy progressive met random trajecten: Random")
        print("Voor een greedy progressive met voorkeur voor ongebruikte connecties: Connections")
        print("Voor een Connections met voorkeur voor benodigde stations: Stations")
        print("Voor een Connections met voorkeur voor stations met 1 vervolgverbinding: Filler")
        print("Voor een stations met meerdere tracks tegelijkertijd: Group")
        heuristiek = input("Welke heuristiek wil je gebruiken? \n")
        repetitions = int(input("Hoeveel repetities per nieuwe track? \n"))
        times = int(input("Hoeveel scores wil je hebben? \n"))

        
        # initialise correct algorithm with inputted parameters
        if(heuristiek == "Random"):
            progressive = pr.Progressive_algorithm(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
        elif(heuristiek == "Connections"):
            progressive = pr.Progressive_connections(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
        elif(heuristiek == "Stations"):
            progressive = pr.Progressive_stations(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
        elif(heuristiek == "Filler"):
            progressive = pr.Progressive_randomstart(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections)
        elif(heuristiek == "Group"):
            groups = int(input("Hoeveel tracks tegelijkertijd toevoegen? \n"))
            progressive = pr.Progressive_group(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections, groups = groups)
        elif(heuristiek == "Even"):
            groups = int(input("Hoeveel tracks tegelijkertijd toevoegen? \n"))
            progressive = pr.Progressive_even(stations, repetitions=repetitions, trains=trains, traveltime=traveltime, times=times, number_of_connections = number_connections, groups = groups)
        else:
            print("verkeerde input")
        
        # run algorithm
        run_progressive_run_times(progressive, stations_file = stations_file)


    elif(algoritme== "Hill Climber"):

        # --------------------------- Hill Climber ---------------------------------
        number_random_startstate = 100
        hillclimber_iteration = 400
        hillclimber_restart_iteration= 1000
        number_traject = 7
        if stations_file == 'stationsnederland.csv':
            number_traject = 20
            print(stations_file, "209 main")
        
       
    

        print("Setting up Hill Climber...")
        possible_solutions = make_random_start_state( number_random_startstate, stations_file, connecties_file,number_traject)
        random_chosen_solution= random.choice(possible_solutions)
        score_chosen_solution = score_calc(random_chosen_solution)
        tracks_writer(random_chosen_solution, score_chosen_solution, f'data/output/hillclimber/{regio}/chosen_trajectories.csv')
        run_plot_trajectories(f"data/output/hillclimber/{regio}/chosen_trajectories.csv", f'data/images/hillclimber/{regio}/huidige_trajectories.png',stations_file )


        # Hillclimber compinatie van mutaties testen
        climber =  HillClimber(random_chosen_solution, stations_file, connecties_file)
        combination_name, function_combinations = make_compinations(climber)
        
        # beste compinatie opslaan en plotten
        best_score, best_trajectories, scores_after_iteration, best_combination, combination = test_combination(
            hillclimber_iteration,function_combinations, combination_name, random_chosen_solution, stations_file,connecties_file,regio)

        titel = f"Combination: {best_combination}"
        titel =  ' '.join(titel.split('__'))
        plot_iterations_scores(scores_after_iteration,hillclimber_iteration, f'data/images/hillclimber/{regio}/scores_of_best_combination.png', titel)
        tracks_writer(best_trajectories, best_score, f'data/output/hillclimber/{regio}/trajectories_of_best_combination.csv')
        run_plot_trajectories(f'data/output/hillclimber/{regio}/trajectories_of_best_combination.csv', f'data/images/hillclimber/{regio}/trajectories_of_best_combination.png', stations_file)

        # # hillclimber meerdere keren runnen en plotten
        print("restart Hill Climber...")
        hc_restart = restart_hillclimber(hillclimber_restart_iteration, hillclimber_iteration, stations_file,connecties_file, combination)
        run_plot_random_alg_score(hc_restart[1], f'data/images/hillclimber/{regio}/scores_iteration_hillclimber.png',"Restart Hill Climber scores")
        result_max = calculate_best_trajectory(hc_restart[0],hillclimber_restart_iteration)
        
        # de hilclimber met de beste score  plotten
        tracks_writer(result_max[1], result_max[0], f'data/output/hillclimber/{regio}/trajectories_after_more_hill.csv')
        run_plot_trajectories(f'data/output/hillclimber/{regio}/trajectories_after_more_hill.csv', f'data/images/hillclimber/{regio}/trajectories_after_more_hill.png', stations_file)

    else:
        print("Verkeerde input")
