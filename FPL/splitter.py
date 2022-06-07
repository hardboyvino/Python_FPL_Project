import pandas as pd
import os

# Filename
filename = "201819 PerApp GK2.csv"

# Read the file
dataset = pd.read_csv(filename)

# Turn this particular column into a float
dataset["Cost (M)"] = dataset["Cost (M)"].astype(float)

# If the column matches the criteria, extract it. Else, leave it alone
dataset = dataset.loc[dataset["Cost (M)"] > 5]

# Export the extract to another csv that can be used later
dataset.to_csv(f"{filename} - splitter.csv", mode="a",index=False)
