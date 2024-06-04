import csv


class traject():
    def __init__(self, start_station):
        self.verbinding = []
        self.reistijd = 0 
        eind_station = start_station
        

    
    

class station():
    def __init__(self, naam):
    self.name = naam  
    # met welke stations de station verbinding heeft
    self.verbinding = []                                                                                                                                                                                                              



def functie(station):
    if station heeft verbinding met eind station
        voeg station aan lijst verbindingen 
        tel tijd bij 
        update eind station 

    



# Open bestand en print rij
with open('StationsHolland.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        
        maak station.naam aan 
        stop alle stations.namen in dictionary 
        #print(row[0])

with open('ConnectiesHolland.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    minuten = 0
    for row in csvreader:
        als station.naam  gelijk is aan row[0]
            add row[1] in lijst verbindingen 
        minuten += int(row[2])
        print(row[2])
    print(minuten)
    
    
