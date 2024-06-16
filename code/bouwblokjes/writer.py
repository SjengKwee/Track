# Aangemaakt door Sjeng
# writer.py
# Deze functie schrijft de output behorende bij een enkele oplossing uit om geplot te kunnen worden

import csv

def tracks_writer(tracks: list, score, filename):
    """
    Print de resultaten, met name een lijst trajecten en de score, in een csv
    """

    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file,quoting=csv.QUOTE_MINIMAL, delimiter = ",")
        writer.writerow(["Tracks", "Stations"])
        counter = 1
        for track in tracks:
            writer.writerow([counter, track._stations])
            counter += 1
        writer.writerow(["Score:", score])
    
