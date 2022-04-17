import pandas as pd
from cs50 import get_int
import csv


# Open the file and get the column headers as a list
data = pd.read_csv(r'fpl_forward.csv').to_dict()

G = 2
D = 5
M = 5
F = 3
BUDGET = 101
team = []
counter = 0
positions = {'Goalkeeper': G, 'Defender': D, 'Midfielders': M, 'Forwards': F}


for item in data.items():
    print(item)