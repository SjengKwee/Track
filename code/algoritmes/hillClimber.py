import copy
import random
from code.bouwblokjes.score import *
from code.classes.station import *
from code.classes.traject import *





class HillClimber():
    def __init__(self,start_state):
        # start_state moet een lijst met trajecten zijn
        self.trajectories = copy.deepcopy(start_state)
        #self.connections = connections
        self.value = score_calc(start_state)
        
    

    def mutate_trajectories(self, new_trajectories, number_of_mutation=1):

        #print(len(new_trajectories), "voor ")
        getal = random.randint(0, len(new_trajectories)-1)
        new_trajectories.pop(getal)
        print(getal,len(new_trajectories))

        #print(len(new_trajectories), "na ")

    def check_solution(self, new_trajectories):
        new_value = score_calc(new_trajectories)
        old_value = self.value 
    
        if new_value >= old_value:
            self.trajectories= new_trajectories
            self.value = new_value


    
    def run(self, iterations, mutate_trajectories_number=1):

        # herhaal
       
        for iteration in range(iterations):
            print(self.value)


            new_trajectories = copy.deepcopy(self.trajectories)
            # doe een kleine random aanpassing 
            # een traject meer of minder rijden 
            # een verbinding verwijderen 
            # een verbinding toevoegen 
            # een traject bij een andere startpunt laten beginnen  
            self.mutate_trajectories(new_trajectories, number_of_mutation=mutate_trajectories_number)
            #als de state is verslechterd:
            self.check_solution(new_trajectories)
        print(new_trajectories)
                
                