from code.algoritmes.random_algoritme import *
from code.algoritmes.hillClimber import *
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.score import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.writer import *

import math



if __name__ == "__main__":
    
    # --------------------------- Hill Climber ---------------------------------

    random.seed(10)
    print("Setting up Hill Climber...")
    stations = make_connections()

    # start state 1 oplossing = lijst[traject([stations)])]
    # een lijst met oplossing 1 oploss#ing kiezen 
    possible_solutions = []
    for i in range(5):
        solution = run_random_algoritme(stations,2)
        possible_solutions.append(solution)
    random_chosen_solution= random.choice(possible_solutions)

    # huidige trajectories opslaan en plotten
    # score_chosen_solution = score_calc(random_chosen_solution)
    # tracks_writer(random_chosen_solution, score_chosen_solution, 'data/output/hillclimber/chosen_trajectories.csv')
    # run_plot_trajectories('data/output/hillclimber/chosen_trajectories.csv', 'data/images/hillclimber/huidige_trajectories.png')
  
    
    climber =  HillClimber(random_chosen_solution)
    result =climber.run(1)
    trajectories = result[0]
    print(trajectories)
    
    # score na elke iteratie plotten 
    # scores = result[1]
    # plot_iterations_scores(scores,800, 'data/images/hillclimber/scores_na_wijziging.png')
    # de uiteindelijke traject plotten 
    # trajectories_after_hillclimber = result[0]
    # score_after_hillclimber = result[2]
    # tracks_writer(trajectories_after_hillclimber, score_after_hillclimber, 'data/output/hillclimber/trajectories_after_one_hill.csv')
    # run_plot_trajectories('data/output/hillclimber/trajectories_after_one_hill.csv', 'data/images/hillclimber/trajectories_after_one_hill.png')
  
    
    ###

    # hillclimber meerdere keren runnen en score na elke hilclimber printen 
    # hillclimber_results = []
    # scores_iteration_hillclimber = []
    # for i in range(10):

    #     climber =  HillClimber(random_chosen_solution)
    #     result =climber.run(8)
    #     hillclimber_results.append(result)
    #     scores_iteration_hillclimber.append(result[2])
    ###

    # # plot_iterations_scores(scores_iteration_hillclimber,10, 'data/images/hillclimber/scores_iteration_hillclimber.png')
    max_result = 0
    
    ###
    # for i in range(10):
    #     if int(hillclimber_results[i][2]) > max_result:
    #         max_result = int(hillclimber_results[i][2])
    #         best_trajectories = hillclimber_results[i][0]
           
    # print(max_result)

    ###

    # de hilclimber met de beste score  plotten
    # #tracks_writer(best_trajectories, max_result, 'data/output/hillclimber/trajectories_after_more_hill.csv')
    # # run_plot_trajectories('data/output/hillclimber/trajectories_after_more_hill.csv', 'data/images/hillclimber/trajectories_after_more_hill.png')

        

