from code.algoritmes.random_algoritme import *
from code.algoritmes.hillClimber import *
from code.bouwblokjes.plot_trajectories import *
from code.bouwblokjes.score import *
from code.bouwblokjes.inladen import *



if __name__ == "__main__":
    
    # --------------------------- Hill Climber ---------------------------------


    print("Setting up Hill Climber...")
    stations = make_connections()

    # start state 1 oplossing = lijst[traject([stations)])]
    # een lijst met oplossing 1 oplossing kiezen 
    possible_solutions = []
    for i in range(100):
        solution = run_random_algoritme(stations,7)
        possible_solutions.append(solution)

    random_chosen_solution= random.choice(possible_solutions)
    
    climber =  HillClimber(random_chosen_solution)

    #print("Running Hill Climber...")
    climber.run(10,1)


    

