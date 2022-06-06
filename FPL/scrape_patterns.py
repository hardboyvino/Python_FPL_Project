import numpy as np
import pandas as pd
from itertools import combinations, product

# Read in the fill to combine
df = pd.read_excel("Diff Scrape.xlsx")
print(df)

# Find the product of every column with each other
combo = list(product(df["STAT TYPE"], df["DATA TYPE"], df["SEASONS"], df["FIXTURE FILTER"], df["PLAYER FILTER"], df["GW DIFFERENCE"]))

# Turn the list into a dataFrame
new_df = pd.DataFrame(combo)

# Fill empty cells with NaN
new_df.replace("", np.nan, inplace=True)

for i in range(6):
    new_df.dropna(subset=[i], inplace=True)


# Turn the dataFrame into an excel
new_df.to_excel("Possible Combos.xlsx", index=False)