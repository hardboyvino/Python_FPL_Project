import pandas as pd

# Read in the Forwards Excel scrapped file
dataset = pd.read_excel('fpl_forward.xlsx')

# Fill in any cells that might be blank or NaN
dataset.fillna(0, inplace=True)

# Predict Forwards Points
dataset['Predict'] = (((dataset['%%GI'])*-1.019903) + ((dataset['On Target'])*-1.069947) + ((dataset['Shots Outside Box'])*0.353106) + ((dataset['Big Chances'])*-1.805292) + ((dataset['Headed Shots'])*-0.454502) + ((dataset['NPxG'])*1.872558) + ((dataset['Goals'])*0.972139) + ((dataset['Goals from Outside Box'])*-2.522883) + ((dataset['Headed Goals'])*1.273953) + ((dataset['Successful Crosses'])*-0.987266) + ((dataset['Total Corners'])*-1.777532) + ((dataset['Total Indirect FK'])*-1.318969) + ((dataset['Key Passes'])*-2.608201) + ((dataset['Assists'])*0.805826) + ((dataset['Yellow Card'])*0.743667) + ((dataset['Creativity'])*0.164501) + ((dataset['xAtt'])*-0.822763) + ((dataset['Expected Points'])*1.549264) + ((dataset['Bonus Points'])*-0.319878) + ((dataset['Goals Conceded'])*-0.372822) + ((dataset['Total Tackles'])*-0.317474) + ((dataset['Interceptions'])*-0.632818) + ((dataset['Shots Conceded In Box'])*0.134319) + ((dataset['Shots Conceded OT'])*-0.885171) + ((dataset['SP'])*0.379245) + ((dataset['Headed Shots Conceded'])*-0.40258) + ((dataset['BC Conceded'])*-1.060432) + ((dataset['xGC'])*3.272983) + ((dataset['Opposition Half Passes'])*-0.046839) + ((dataset['Accurate Throughballs'])*-1.829806) + ((dataset['Total Touches'])*-0.056358) + ((dataset['Touches in Box'])*0.160959) + ((dataset['Entries into Final 3rd'])*0.291885) + ((dataset['Entries into Box'])*0.417056) + ((dataset['Fouled in Final 3rd'])*0.25925) + ((dataset['Corners into Box'])*2.189437) + (1.876184))

# Export to an Excel file & A General file of only predicitions
selectList = ['Name', 'Team Name', 'Price', 'Predict']
dataToWrite = dataset[selectList]
dataToWrite.to_excel('fpl_forwardOld.xlsx', index=False)