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
        verbindingen= len(new_trajectories[getal]._stations)

        # als de traject leeg is 
        while verbindingen < 1:
            getal = random.randint(0, len(new_trajectories)-1)
            verbindingen= len(new_trajectories[getal]._stations)
        

        old_traject = new_trajectories[getal]
        start_station = new_trajectories[getal]._stations[0]
        station_object = make_connections()
        new_traject = Traject(station_object[start_station])
       
        for i in old_traject._stations[1:len(old_traject._stations)-1]:
            new_traject.add_trajectconnection(station_object[i])
        new_trajectories[getal] = new_traject
    
    def change_start_station(self,new_trajectories):

        getal = random.randint(0, len(new_trajectories)-1)

        while len(new_trajectories[getal]._stations) < 2:
            getal = random.randint(0, len(new_trajectories)-1)
            
        old_traject = new_trajectories[getal]
        start_station = new_trajectories[getal]._stations[1]
        station_object = make_connections()
        new_traject = Traject(station_object[start_station])

        for i in old_traject._stations[2:len(old_traject._stations)]:
            new_traject.add_trajectconnection(station_object[i])
        new_trajectories[getal] = new_traject

    def separate_traject(self, new_trajectories):
        number_routes = len(new_trajectories)
        if number_routes >= 9:
            return new_trajectories
        
        number = random.randint(0, len(new_trajectories)-1)
        old_traject = new_trajectories[number]
        separate_number= random.randint(0, len(old_traject._stations)-1)
        start_station_first_traject = old_traject._stations[0]
        start_station_second_traject = old_traject._stations[separate_number]

        station_object = make_connections()
        first_traject= Traject(station_object[start_station_first_traject])
        second_traject= Traject(station_object[start_station_second_traject])

        for i in old_traject._stations[1:separate_number]:
            first_traject.add_trajectconnection(station_object[i])

        for i in old_traject._stations[separate_number+1: len(old_traject._stations)]:
            second_traject.add_trajectconnection(station_object[i])

        while True:
            connection = first_traject._endstation._connection[random.choice(list(first_traject._endstation._connection.keys()))]
            if int(first_traject._traveltime) + int(connection[1]) > 120:
                break
            first_traject.add_trajectconnection(connection[0])

        while True:
            connection = second_traject._endstation._connection[random.choice(list(second_traject._endstation._connection.keys()))]
            if int(second_traject._traveltime) + int(connection[1]) > 120:
                break
            second_traject.add_trajectconnection(connection[0])

        new_trajectories.pop(number)
        new_trajectories.append(first_traject)
        new_trajectories.append(second_traject)
        #print(first_traject)

        #print(len(new_trajectories))
        
        #new_trajectories.pop(number_routes)
       


    def check_solution(self, new_trajectories):
        #print(new_trajectories)
        new_value = score_calc(new_trajectories)
        
        old_value = self.value 
        #print(new_value)
    
        if new_value >= old_value:
            self.trajectories= new_trajectories
            self.value = new_value
           

    def mutate_random_trajectories(self,new_trajectories):
        functions = []
        functions.append("self.delete_last_connection(new_trajectories)")
         #self.mutate_trajectories(new_trajectories)
            # self.delete_last_connection(new_trajectories)
            # self.change_start_station(new_trajectories)
        print(functions)

    
    def run(self, iterations, mutate_trajectories_number=1):

        # herhaal
        
       
        for iteration in range(iterations):
            #print(self.value)

            new_trajectories = copy.deepcopy(self.trajectories)
            # doe een kleine random aanpassing 
            # een traject minder rijden x
            # van een traject laatste verbinding verwijderen x
            # een traject bij een andere startpunt laten beginnen  x
            # een traject opsplitsten x

            # self.mutate_trajectories(new_trajectories)
            # self.delete_last_connection(new_trajectories)
            # self.change_start_station(new_trajectories)
            #print(new_trajectories)
            # self.separate_traject(new_trajectories)
            #als de state is verslechterd:
            self.mutate_random_trajectories(new_trajectories)
            self.check_solution(new_trajectories)
            
            
        
        #print(new_trajectories, len(new_trajectories))
                
                