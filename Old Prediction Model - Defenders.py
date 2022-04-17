import pandas as pd

# Read in the Defenders Excel scrapped file
dataset = pd.read_excel('fpl_defenders.xlsx')

# Fill in any cells that might be blank or NaN
dataset.fillna(0, inplace=True)

# Predict Defenders Points
dataset['Predict'] = (((dataset['Minutes'])*-0.009034) + ((dataset['%%xGI'])*-1.802019) + ((dataset['%%GI'])*1.02112) + ((dataset['xGI'])*1.762121) + ((dataset['On Target'])*-3.031996) + ((dataset['Big Chances'])*-6.456009) + ((dataset['NPxG'])*24.043236) + ((dataset['Headed Goals'])*-1.033312) + ((dataset['Total Corners'])*0.066494) + ((dataset['Total Indirect FK'])*-0.22258) + ((dataset['Key Passes'])*-0.191123) + ((dataset['Red Card'])*-1.297444) + ((dataset['Threat'])*-0.050047) + ((dataset['Influence'])*-0.042478) + ((dataset['BPS'])*0.045861) + ((dataset['Points'])*-0.114879) + ((dataset['Goals Conceded'])*-0.11276) + ((dataset['Total Tackles'])*0.156991) + ((dataset['Tackles Won'])*-0.222984) + ((dataset['Clearances'])*0.03936) + ((dataset['Shots Conceded OT'])*0.032499) + ((dataset['SP'])*0.1917) + ((dataset['Headed Shots Conceded'])*-0.123623) + ((dataset['BC Conceded'])*0.065461) + ((dataset['Successful Passes'])*0.015142) + ((dataset['%% Successful Passes'])*-0.018628) + ((dataset['Successful Opposition Half Passes'])*-0.023796) + ((dataset['Total Throughballs'])*0.619998) + ((dataset['Total Touches'])*0.019132) + ((dataset['Touches in Box'])*0.096691) + ((dataset['Entries into Final 3rd'])*-0.020132) + ((dataset['Entries into Box'])*0.100053) + ((dataset['Fouled in Box'])*-1.303454) + ((dataset['Accurate Indirect FK'])*-0.545811) + ((dataset['Total Direct FK'])*-1.093949) + ((dataset['Goals Direct FK'])*4.460507) + ((dataset['Penalty Goals'])*7.9751) + (4.183594))

# Export to an Excel file & A General file of only predicitions
selectList = ['Name', 'Team Name', 'Price', 'Predict']
dataToWrite = dataset[selectList]
dataToWrite.to_excel('fpl_defendersOld.xlsx', index=False)