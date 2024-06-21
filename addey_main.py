from code.algoritmes.random_algoritme import *
from code.algoritmes.hillClimber import *
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.score import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.writer import *

import math



if __name__ == "__main__":
    
    # --------------------------- Hill Climber ---------------------------------
    number_random_startstate = 5
    hillclimber_iteration = 800
    hillclimber_restart_iteration= 10


    print("Setting up Hill Climber...")
    random_chosen_solution = make_random_start_state( number_random_startstate)
    # huidige trajectories opslaan en plotten
    score_chosen_solution = score_calc(random_chosen_solution)
    tracks_writer(random_chosen_solution, score_chosen_solution, 'data/output/hillclimber/chosen_trajectories.csv')
    run_plot_trajectories('data/output/hillclimber/chosen_trajectories.csv', 'data/images/hillclimber/huidige_trajectories.png')
  
    # 1 Hillclimber runnen en scores opslaan 
    climber =  HillClimber(random_chosen_solution)
    result =climber.run(hillclimber_iteration)
    trajectories = result[0]
    scores_after_iteration = result[1]
    plot_iterations_scores(scores_after_iteration,hillclimber_iteration, 'data/images/hillclimber/scores_na_wijziging.png')
    trajectories_after_1_hillclimber = result[0]
    score_after_1_hillclimber = result[2]
    tracks_writer(trajectories_after_1_hillclimber, score_after_1_hillclimber, 'data/output/hillclimber/trajectories_after_one_hill.csv')
    run_plot_trajectories('data/output/hillclimber/trajectories_after_one_hill.csv', 'data/images/hillclimber/trajectories_after_one_hill.png')
  
    # hillclimber meerdere keren runnen en plotten
    hc_restart = restart_hillclimber(hillclimber_restart_iteration, hillclimber_iteration, random_chosen_solution)
    plot_iterations_scores(hc_restart[1],hillclimber_restart_iteration, 'data/images/hillclimber/scores_iteration_hillclimber.png')
    result_max = calculate_best_trajectory(hc_restart[0],hillclimber_restart_iteration)
    
    # de hilclimber met de beste score  plotten
    tracks_writer(result_max[1], result_max[0], 'data/output/hillclimber/trajectories_after_more_hill.csv')
    run_plot_trajectories('data/output/hillclimber/trajectories_after_more_hill.csv', 'data/images/hillclimber/trajectories_after_more_hill.png')

        

