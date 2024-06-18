from code.algoritmes.random_algoritme import *
from code.algoritmes.hillClimber import *
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.score import *
from code.bouwblokjes.inladen import *
from code.bouwblokjes.writer import *



if __name__ == "__main__":
    
    # --------------------------- Hill Climber ---------------------------------

    random.seed(10)
    print("Setting up Hill Climber...")
    stations = make_connections()

    # start state 1 oplossing = lijst[traject([stations)])]
    # een lijst met oplossing 1 oploss#ing kiezen 
    possible_solutions = []
    for i in range(5):
        solution = run_random_algoritme(stations,7)
        possible_solutions.append(solution)
    # huidige trajectories opslaan en plotten
    random_chosen_solution= random.choice(possible_solutions)
    # score_chosen_solution = score_calc(random_chosen_solution)
    # tracks_writer(random_chosen_solution, score_chosen_solution, 'data/output/hillclimber/chosen_trajectories.csv')
    # run_plot_trajectories('data/output/hillclimber/chosen_trajectories.csv', 'data/images/hillclimber/huidige_trajectories.png')
  
    
    climber =  HillClimber(random_chosen_solution)
    result =climber.run(800)
    trajectories = result[0]
    
    # score na elke iteratie plotten 
    scores = result[1]
    plot_iterations_scores(scores,800, 'data/images/hillclimber/scores_na_wijziging.png')
    # de uiteindelijke traject plotten 
    trajectories_after_hillclimber = result[0]
    score_after_hillclimber = result[2]
    
    # hillclimber meerdere keren runnen en score na elke hilclimber printen 

    # de hilclimber met de beste score  plotten

        

