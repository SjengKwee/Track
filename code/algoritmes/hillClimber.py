import copy
import random
from code.bouwblokjes.score import *
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.inladen import *
from .random_algoritme import *


random.seed(10)

class HillClimber():
    """De Hillclimber class kies willekeurig een verandering. 
    Elke verandering wordt bewaard voor de volgende iteratie 
    """
    def __init__(self,start_state):

        self.trajectories = copy.deepcopy(start_state)
        self.value = score_calc(start_state)
        
    def mutate_trajectories(self, new_trajectories):
        """ verwijder een willekeurig traject """

        getal = random.randint(0, len(new_trajectories)-1)
        new_trajectories.pop(getal)

      
    def delete_last_connection(self, new_trajectories):
        """Kies een willekeurig traject en verwijder de laatste verbinding"""

        getal = random.randint(0, len(new_trajectories)-1)
        verbindingen= len(new_trajectories[getal]._stations)

        # als de gekozen traject leeg is kies willekeurig een andere traject 
        while verbindingen < 1:
            getal = random.randint(0, len(new_trajectories)-1)
            verbindingen= len(new_trajectories[getal]._stations)
        
        # maak nieuwe traject aan zonder laatste verbindingen 
        old_traject = new_trajectories[getal]
        new_traject= duplicate_traject(old_traject,0,1,len(old_traject._stations)-1)
        new_trajectories[getal] = new_traject
    
    def change_start_station(self,new_trajectories):
        """ Een random traject kiezen en start station wijzigen"""

        # Een random traject kiezen met minimaal 2 verbindingen
        getal = random.randint(0, len(new_trajectories)-1)
        while len(new_trajectories[getal]._stations) < 2:
            getal = random.randint(0, len(new_trajectories)-1)
        
        # Gekozen traject opslaan en nieuwe traject zonder de begin station aanmaken
        old_traject = new_trajectories[getal]
        new_traject = duplicate_traject(old_traject, 1, 2, len(old_traject._stations))
        new_trajectories[getal] = new_traject

    def separate_traject(self, new_trajectories):
        """ Een willekeurig traject kiezen, 
        het gekozen traject opsplitsen op een willekeurige plek en 
        vervolgens het traject aanvullen tot het maximale aantal minuten is bereikt. """

        # Als er genoeg trajecten zijn traject niet opsplitsen 
        number_routes = len(new_trajectories)
        if number_routes >= 7:
            return new_trajectories
        
        # Random traject kiezen een random scheiding plaats
        number = random.randint(0, len(new_trajectories)-1)
        old_traject = new_trajectories[number]
        separate_number= random.randint(0, len(old_traject._stations)-1)

        # gekozen traject opsplitsten in first en second
        first_traject = duplicate_traject(old_traject,0,1,separate_number)
        second_traject = duplicate_traject(old_traject,separate_number,separate_number+1,len(old_traject._stations))

        # traject aanvullen tot het max minuten bereikt 
        first_traject = add_connections_to_trajectory(first_traject)
        second_traject = add_connections_to_trajectory(second_traject)
        
        # gekozen traject verwijderen opgesplitste traject toevoegen
        new_trajectories.pop(number)
        new_trajectories.append(first_traject)
        new_trajectories.append(second_traject)
       
    def check_solution(self, new_trajectories):
        """ check en accepter wijzigingen die de score verhogen"""
        new_value = score_calc(new_trajectories)
        old_value = self.value 

        if new_value >= old_value:
            self.trajectories= new_trajectories
            self.value = new_value
           
    def mutate_random_trajectories(self):
    
        """ maak een lijst aan met methodes die wijzigingen mogelijk maken."""
        functions = []
        functions.append(self.separate_traject)
        functions.append(self.delete_last_connection)
        functions.append(self.mutate_trajectories)
        functions.append(self.change_start_station)
        
        return functions
    
    def run(self, iterations):
        """ Voert optimalisatie uit voor een bepaald aantal iteraties."""
        scores_na_iteratie = []
        for iteration in range(iterations):

            # maak een copy 
            new_trajectories = copy.deepcopy(self.trajectories)

            # breng wijzig aan 
            functions = self.mutate_random_trajectories()
            func = random.choice(functions)
            func(new_trajectories)
            
            # check wijziging 
            self.check_solution(new_trajectories)
            scores_na_iteratie.append(self.value)
            
        return [new_trajectories, scores_na_iteratie, self.value]
                

def duplicate_traject(old_traject, start, start_index, end):
    """ traject dupliceren van en tot en met gekozen verbinding"""
    
    start_station = old_traject._stations[start]
    station_object = make_connections()
    traject= Traject(station_object[start_station])

    for i in old_traject._stations[start_index:end]:
        traject.add_trajectconnection(station_object[i])
    return traject 

def add_connections_to_trajectory(traject):
    """ voeg verbindingen toe aan de traject"""
    while True:
        connection = traject._endstation._connection[random.choice(list(traject._endstation._connection.keys()))]
        if int(traject._traveltime) + int(connection[1]) > 120:
            break
        traject.add_trajectconnection(connection[0])
    return traject 

    




def restart_hillclimber(iterations_hillclimber, mutation_iteration, random_chosen_solution):
    """Hillclimber meerdere keren runnen met elke keer een andere start state"""
    
    hillclimber_results = []
    scores_iteration_hillclimber = []
    for i in range(iterations_hillclimber):

        climber =  HillClimber(random_chosen_solution)
        result =climber.run(mutation_iteration)
        hillclimber_results.append(result)
        scores_iteration_hillclimber.append(result[2])

    return [hillclimber_results, scores_iteration_hillclimber]

def calculate_best_trajectory(hc_restart, iteration_restart):
    max_result = 0
    hillclimber_results = hc_restart
    
    for i in range(iteration_restart):
        if float(hillclimber_results[i][2]) > max_result:
            max_result = float(hillclimber_results[i][2])
            best_trajectories = hillclimber_results[i][0]

    print(max_result)
    return [max_result, best_trajectories]

def make_random_start_state(number_of_starts):
    """maakt random trajecten aan met random algoritme"""
    stations = make_connections()
    possible_solutions = []
    for i in range(number_of_starts):
        solution = run_random_algoritme(stations,7)
        possible_solutions.append(solution)
    random_chosen_solution= random.choice(possible_solutions)
    return random_chosen_solution