import copy
import random
from code.bouwblokjes.score import *
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.inladen import *
from .random_algoritme import *
import itertools
from itertools import combinations

random.seed(10)


class HillClimber():
    """De Hillclimber class kies willekeurig een verandering. 
    Elke verandering wordt bewaard voor de volgende iteratie 
    """
    def __init__(self,start_state, stations_file='StationsHolland.csv', connecties_file='ConnectiesHolland.csv'):

        self.trajectories = copy.deepcopy(start_state)
        self.value = score_calc(start_state)
        self.stations_file = stations_file
        self.connecties_file = connecties_file
        self.functions = [
            ('separate_traject', self.separate_traject),
            ('delete_last_connection', self.delete_last_connection),
            ('mutate_trajectories', self.mutate_trajectories),
            ('change_start_station', self.change_start_station)
        ]
        
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
        new_traject= duplicate_traject(old_traject,0,1,len(old_traject._stations)-1,self.stations_file, self.connecties_file)
        new_trajectories[getal] = new_traject
    
    def change_start_station(self,new_trajectories):
        """ Een random traject kiezen en start station wijzigen"""

        # Een random traject kiezen met minimaal 2 verbindingen
        getal = random.randint(0, len(new_trajectories)-1)
        while len(new_trajectories[getal]._stations) < 2:
            new_trajectories.pop(getal)
            
            getal = random.randint(0, len(new_trajectories)-1)
        
        # Gekozen traject opslaan en nieuwe traject zonder de begin station aanmaken
        old_traject = new_trajectories[getal]
        new_traject = duplicate_traject(old_traject, 1, 2, len(old_traject._stations),self.stations_file, self.connecties_file)
        new_trajectories[getal] = new_traject

    def separate_traject(self, new_trajectories):
        """ Een willekeurig traject kiezen, 
        het gekozen traject opsplitsen op een willekeurige plek en 
        vervolgens het traject aanvullen. """

        # Als er genoeg trajecten zijn traject niet opsplitsen 
        number_routes = len(new_trajectories)
        
        # Random traject kiezen een random scheiding plaats
        number = random.randint(0, len(new_trajectories)-1)
        old_traject = new_trajectories[number]
        separate_number= random.randint(0, len(old_traject._stations)-1)

        # gekozen traject opsplitsten in first en second
        first_traject = duplicate_traject(old_traject,0,1,separate_number, self.stations_file, self.connecties_file)
        second_traject = duplicate_traject(old_traject,separate_number,separate_number+1,len(old_traject._stations),self.stations_file, self.connecties_file)

        # traject aanvullen tot het max minuten bereikt 
        first_traject = add_connections_to_trajectory(first_traject, self.stations_file)
        second_traject = add_connections_to_trajectory(second_traject, self.stations_file)
        
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
           

    
    def run(self, functions_combination, iterations, output_file=None):
        """ Voert optimalisatie uit voor een bepaald aantal iteraties."""
        scores_na_iteratie = []
        chosen_functions = []
        for _ in range(iterations):

            # Maak een copy 
            new_trajectories = copy.deepcopy(self.trajectories)

            # Breng wijziging aan door een willekeurige functie uit de combinatie te kiezen
            func_name, func= random.choice(functions_combination)
            func(new_trajectories)
            

            # check wijziging 
            previous_value = self.value
            self.check_solution(new_trajectories)
            scores_na_iteratie.append(self.value)
            new_value = self.value

             # Bewaar de gekozen functie en eventueel de nieuwe score
            if new_value > previous_value:
                chosen_functions.append((func_name, new_value))
                
            else:
                chosen_functions.append((func_name, None))

            # Schrijf gekozen functies en scores naar een CSV-bestand
            if output_file is not None:
                save_used_functions(output_file,chosen_functions)
           

        return [new_trajectories, scores_na_iteratie, self.value]
                

def duplicate_traject(old_traject, start, start_index, end, stations_file, connecties_file):
    """ traject dupliceren van en tot en met gekozen verbinding"""
    
    start_station = old_traject._stations[start]
    station_object = make_connections(stations_file, connecties_file)
    traject= Traject(station_object[start_station])

    for i in old_traject._stations[start_index:end]:
        traject.add_trajectconnection(station_object[i])
    return traject 

def add_connections_to_trajectory(traject, stations_file):
    """ voeg verbindingen toe aan de traject"""
    if stations_file == 'StationsHolland.csv':
        minutes = 120
    else:
         minutes = 180

    
    while True:
        connection = traject._endstation._connection[random.choice(list(traject._endstation._connection.keys()))]
        if float(traject._traveltime) + float(connection[1]) > minutes:
            break
        traject.add_trajectconnection(connection[0])
    return traject 



def restart_hillclimber(iterations_hillclimber, mutation_iteration, stations_file,connecties_file, combination):
    """Hillclimber meerdere keren runnen met elke keer een andere start state"""
    
    hillclimber_results = []
    scores_iteration_hillclimber = []
    for i in range(iterations_hillclimber):
        random_chosen_solution = make_random_start_state( iterations_hillclimber*100, stations_file, connecties_file)
        climber =  HillClimber(random_chosen_solution, stations_file,connecties_file)
        result =climber.run(combination, mutation_iteration)
        hillclimber_results.append(result)
        scores_iteration_hillclimber.append(result[2])
        print("restart Hill Climber run: ", i, "score: ",result[2])
        

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

def make_random_start_state(number_of_starts,stations_file, connecties_file):
    """maakt random trajecten aan met random algoritme"""
    stations = make_connections(stations_file, connecties_file)
    possible_solutions = []
    for i in range(number_of_starts):
        solution = run_random_algoritme(stations,7)
        possible_solutions.append(solution)
    random_chosen_solution= random.choice(possible_solutions)
    return random_chosen_solution


def save_used_functions(output_file,chosen_functions):

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for func_name, score in chosen_functions:
            if score is not None:
                writer.writerow([f"Gekozen functie: {func_name}, {score}"])
                
            else:
                writer.writerow([f"Gekozen functie: {func_name}"])

def make_compinations(climber):
    function_names = [
        'separate_traject',
        'delete_last_connection',
        'mutate_trajectories',
        'change_start_station'
        ]
    combination_name = []
    function_combinations = []
    for i in range(1, len(function_names) + 1):  
            for combination in combinations(function_names, i):
                
                # Maak een lijst met tuples (function_name, climber.method)
                method_tuples = [(func_name, getattr(climber, func_name)) for func_name in combination]
                method_names = '__'.join(func_name for func_name, _ in method_tuples)
                combination_name.append(method_names)
                function_combinations.append(method_tuples)
    return combination_name, function_combinations

def test_combination( hillclimber_iteration,function_combinations, combination_name, random_chosen_solution, stations_file, connecties_file,regio):
    best_score = 0
    for index, combination in enumerate(function_combinations):
        climber =  HillClimber(random_chosen_solution,stations_file, connecties_file)
        output_filename = f"{combination_name[index]}.csv"
        #     print(combination_name)
        result = climber.run(combination, hillclimber_iteration, f'data/output/hillclimber/{regio}/{output_filename}.csv')
    
        if result[2] > best_score:
            best_score = result[2]
            best_trajectories = result[0]
            scores_after_iteration = result[1]
            best_combination = combination_name[index]
            chosen_combination = combination
    
    return best_score, best_trajectories, scores_after_iteration, best_combination, chosen_combination