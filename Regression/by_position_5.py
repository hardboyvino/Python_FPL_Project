from csv import writer
import pandas as pd

price_range = pd.read_csv("GK PerApp 6GWs.csv")

# print(price_range.loc[price_range["Cost (£M)"] > 6])

# If price is lower than 4 OR higher than 6
price_range = price_range.loc[(price_range["Cost (£M)"] < 5) | (price_range["Cost (£M)"] > 4)]

price_range.to_csv("temp.csv", index=False)
