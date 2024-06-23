from code.algoritmes.random_algoritme import *
from code.algoritmes.hillClimber import *
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.score import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.writer import *
from itertools import combinations



if __name__ == "__main__":
    
    # --------------------------- Hill Climber ---------------------------------
    number_random_startstate = 100
    hillclimber_iteration = 800
    hillclimber_restart_iteration= 100
    stations_file = 'StationsHolland.csv'
    connecties_file = 'ConnectiesHolland.csv'
    
    print("Setting up Hill Climber...")
    random_chosen_solution = make_random_start_state( number_random_startstate, stations_file, connecties_file)
    score_chosen_solution = score_calc(random_chosen_solution)
    tracks_writer(random_chosen_solution, score_chosen_solution, 'data/output/hillclimber/chosen_trajectories.csv')
    run_plot_trajectories('data/output/hillclimber/chosen_trajectories.csv', 'data/images/hillclimber/huidige_trajectories.png',stations_file )


    # Hillclimber compinatie van mutaties testen
    climber =  HillClimber(random_chosen_solution, stations_file, connecties_file)
    combination_name, function_combinations = make_compinations(climber)
    
    # beste compinatie opslaan en plotten
    best_score, best_trajectories, scores_after_iteration, best_combination, combination = test_combination(
        hillclimber_iteration,function_combinations, combination_name, random_chosen_solution, stations_file,connecties_file)

    titel = f"Combination: {best_combination}"
    titel =  ' '.join(titel.split('__'))
    plot_iterations_scores(scores_after_iteration,hillclimber_iteration, 'data/images/hillclimber/scores_of_best_combination.png', titel)
    tracks_writer(best_trajectories, best_score, 'data/output/hillclimber/trajectories_of_best_combination.csv')
    run_plot_trajectories('data/output/hillclimber/trajectories_of_best_combination.csv', 'data/images/hillclimber/trajectories_of_best_combination.png', stations_file)

    print("restart Hill Climber...")

    # # hillclimber meerdere keren runnen en plotten
    hc_restart = restart_hillclimber(hillclimber_restart_iteration, hillclimber_iteration, random_chosen_solution, stations_file,connecties_file, combination)
    run_plot_random_alg_score(hc_restart[1],'data/images/hillclimber/scores_iteration_hillclimber.png',"Restart Hill Climber scores")
    result_max = calculate_best_trajectory(hc_restart[0],hillclimber_restart_iteration)
    
    # de hilclimber met de beste score  plotten
    tracks_writer(result_max[1], result_max[0], 'data/output/hillclimber/trajectories_after_more_hill.csv')
    run_plot_trajectories('data/output/hillclimber/trajectories_after_more_hill.csv', 'data/images/hillclimber/trajectories_after_more_hill.png', stations_file)