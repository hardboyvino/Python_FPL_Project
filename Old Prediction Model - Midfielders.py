import pandas as pd

# Read in the Midfielders Excel scrapped file
dataset = pd.read_excel('fpl_midfielders.xlsx')

# Fill in any cells that might be blank or NaN
dataset.fillna(0, inplace=True)

# Predict Midfielders Points
dataset['Predict'] = (((dataset['Minutes'])*-0.022662) + ((dataset['%%xGI'])*1.607351) + ((dataset['%%GI'])*-0.908959) + ((dataset['Shots'])*-4.816212) + ((dataset['Shots in Box'])*4.942442) + ((dataset['Shots Outside Box'])*5.10057) + ((dataset['Headed Shots'])*0.703654) + ((dataset['NPxG'])*29.063232) + ((dataset['Expected Goals'])*-20.368701) + ((dataset['Goals'])*-1.682331) + ((dataset['Goals In Box'])*0.804892) + ((dataset['Headed Goals'])*-5.235949) + ((dataset['Successful Crosses'])*0.595737) + ((dataset['%% Successful Crosses'])*-0.00654) + ((dataset['Total Indirect FK'])*-0.327395) + ((dataset['Key Passes'])*0.816344) + ((dataset['Big Chances Created'])*7.469412) + ((dataset['Expected Assists'])*-18.392258) + ((dataset['Yellow Card'])*-1.177047) + ((dataset['Cleansheet'])*0.521796) + ((dataset['Threat'])*0.058777) + ((dataset['Influence'])*-0.070222) + ((dataset['xAtt'])*-1.686843) + ((dataset['%%xGI'])*1.607351) + ((dataset['bBPS'])*-0.176561) + ((dataset['BPS'])*0.236976) + ((dataset['Blocks'])*0.651944) + ((dataset['Interceptions'])*0.124314) + ((dataset['Shots Conceded'])*0.052201) + ((dataset['Shots Conceded In Box'])*-0.170595) + ((dataset['Shots Conceded OT'])*-0.273396) + ((dataset['Headed Shots Conceded'])*0.263572) + ((dataset['BC Conceded'])*-0.34444) + ((dataset['xGC'])*1.381935) + ((dataset['Total Passes'])*0.275501) + ((dataset['Successful Passes'])*-0.291669) + ((dataset['%% Successful Passes'])*0.040983) + ((dataset['Opposition Half Passes'])*-0.157571) + ((dataset['Successful Opposition Half Passes'])*0.18155) + ((dataset['%% Successful Opposition Half Passes'])*-0.025455) + ((dataset['Accurate Throughballs'])*1.083609) + ((dataset['Touches in Box'])*0.249869) + ((dataset['Entries into Box'])*0.068721) + ((dataset['Total Penalties'])*30.444519) + ((dataset['Penalty Goals'])*-8.136125) + (0.325339))

# Export to an Excel file & A General file of only predicitions
selectList = ['Name', 'Team Name', 'Price', 'Predict']
dataToWrite = dataset[selectList]
dataToWrite.to_excel('fpl_midfieldersOld.xlsx', index=False)