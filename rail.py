import csv


class trein():
    def __init__(self, naam):
        self.name = naam
        self.bezocht_stations = []

class station():
    def __init__(self, naam):
        self.name = naam

class tijd():
    def __init__(self, start,eind):
        self.start = start
        self.eind = eind 






# Open bestand en print rij
with open('StationsHolland.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        print(row[0])
    
    
