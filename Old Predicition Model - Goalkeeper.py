import pandas as pd

# Read in the Defenders Excel scrapped file
dataset = pd.read_excel('fpl_goalkeeper.xlsx')

# Fill in any cells that might be blank or NaN
dataset.fillna(0, inplace=True)

# Predict Goalkeeper Points
dataset['Predict'] = (((dataset['Key Passes'])*54.770248) + ((dataset['Expected Assists'])*21.22336) + ((dataset['Saves'])*-1.792028) + ((dataset['Creativity'])*-5.722363) + ((dataset['BPS'])*0.118902) + ((dataset['Bonus Points'])*-1.565485) + ((dataset['Total Tackles'])*9.963446) + ((dataset['Tackles Won'])*-14.372568) + ((dataset['Recovery'])*0.37525) + ((dataset['Blocks'])*-70.887019) + ((dataset['Shots Conceded OT'])*0.814689) + ((dataset['Total Passes'])*0.196963) + ((dataset['Successful Passes'])*-0.341113) + ((dataset['%% Successful Passes'])*0.094488) + (5.059584))

# Export to an Excel file & A General file of only predicitions
selectList = ['Name', 'Team Name', 'Price', 'Predict']
dataToWrite = dataset[selectList]
dataToWrite.to_excel('fpl_goalkeeperOld.xlsx', index=False)