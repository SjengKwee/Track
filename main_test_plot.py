# Plot scores
from code.bouwblokjes.plot_trajectories import *


# Files
files_holland = {
    "1": ["data/output/progressive/holland/random/1scores", "data/output/progressive/holland/connections/1scores", "data/output/progressive/holland/stations/1scores", "data/output/progressive/holland/filler/1scores", "data/images/progressive/holland/1/plot.png"],
    "10": ["data/output/progressive/holland/random/10scores", "data/output/progressive/holland/connections/10scores", "data/output/progressive/holland/stations/10scores", "data/output/progressive/holland/filler/10scores", "data/images/progressive/holland/10/plot.png"],
    "100": ["data/output/progressive/holland/random/100scores", "data/output/progressive/holland/connections/100scores", "data/output/progressive/holland/stations/100scores", "data/output/progressive/holland/filler/100scores", "data/images/progressive/holland/100/plot.png"]
}

files_nederland = {
    "1": ["data/output/progressive/nederland/random/1scores", "data/output/progressive/nederland/connections/1scores", "data/output/progressive/nederland/stations/1scores", "data/output/progressive/nederland/filler/1scores", "data/images/progressive/nederland/1/plot.png"],
    "10": ["data/output/progressive/nederland/random/10scores", "data/output/progressive/nederland/connections/10scores", "data/output/progressive/nederland/stations/10scores", "data/output/progressive/nederland/filler/10scores", "data/images/progressive/nederland/10/plot.png"],
    "100": ["data/output/progressive/nederland/random/100scores", "data/output/progressive/nederland/connections/100scores", "data/output/progressive/nederland/stations/100scores", "data/output/progressive/nederland/filler/100scores", "data/images/progressive/nederland/100/plot.png"]
}

for iteratie in files_holland.keys():
    plot_meer_histogrammen(files_holland[iteratie][0], files_holland[iteratie][1], files_holland[iteratie][2], files_holland[iteratie][3], files_holland[iteratie][4])

for iteratie in files_holland.keys():
    plot_meer_histogrammen(files_nederland[iteratie][0], files_nederland[iteratie][1], files_nederland[iteratie][2],files_nederland[iteratie][3],files_nederland[iteratie][4],)


# Plot tracks
