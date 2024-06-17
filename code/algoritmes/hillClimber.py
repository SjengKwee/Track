import copy
import random
from code.bouwblokjes.score import *
from code.classes.station import *
from code.classes.traject import *
from code.bouwblokjes.inladen import *



random.seed(10)


class HillClimber():
    def __init__(self,start_state):
        # start_state moet een lijst met trajecten zijn
        self.trajectories = copy.deepcopy(start_state)
        #self.connections = connections
        self.value = score_calc(start_state)
        
    

    def mutate_trajectories(self, new_trajectories):

        #print(len(new_trajectories), "voor ")
        # kies een getal en verwijder die traject 
        getal = random.randint(0, len(new_trajectories)-1)
        new_trajectories.pop(getal)
        print(getal,len(new_trajectories))

        #print(len(new_trajectories), "na ")
    def delete_last_connection(self, new_trajectories):
        
        getal = random.randint(0, len(new_trajectories)-1)
        old_traject = new_trajectories[getal]
        start_station = new_trajectories[getal]._stations[0]
        station_object = make_connections()
        new_traject = Traject(station_object[start_station])
       
        for i in old_traject._stations[1:len(old_traject._stations)-1]:
            new_traject.add_trajectconnection(station_object[i])

        new_trajectories[getal] = new_traject
        

    
      






        verbindingen= len(new_trajectories[getal]._stations)
        # print(len(new_trajectories))

        # while verbindingen < 1:
        #     getal = random.randint(0, len(new_trajectories)-1)
        #     verbindingen= len(new_trajectories[getal]._stations)
        
        # station_verwijderen = new_trajectories[getal]._stations.pop()
        # station_verwijderen = new_trajectories[getal]._trajectconnection.pop()
        # print(new_trajectories[getal]._stations)
        #return new_trajectories
        #print(len(new_trajectories[getal]._stations),getal)



    def check_solution(self, new_trajectories):
        #print(new_trajectories)
        new_value = score_calc(new_trajectories)
        
        old_value = self.value 
        #print(new_value, old_value)
    
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
            # van een traject laatste verbinding verwijderen 
            # van een traject een verbinding toevoegen 
            # een traject bij een andere startpunt laten beginnen  
            # een traject opsplitsten
            self.mutate_trajectories(new_trajectories)
            self.delete_last_connection(new_trajectories)
            #print(new_trajectories)

            #als de state is verslechterd:
            self.check_solution(new_trajectories)
        
        print(new_trajectories, len(new_trajectories))
                
                