from ctypes import sizeof
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

dataset = pd.read_excel('fpl_midfielders.xlsx')

dataset.fillna(0, inplace=True)

Price_Range = (((dataset['On Target'])*3.904) + ((dataset['Shots in Box'])*0.849) + ((dataset['Shots Outside Box'])*0.558) + ((dataset['Big Chances'])*7.787) + ((dataset['Goals In Box'])*5.429) + ((dataset['Final 3rd Passes'])*0.305) + ((dataset['Final 3rd Successesful Passes'])*-0.413) + ((dataset['%% Final 3rd Successful'])*0.042) + ((dataset['Successful Crosses'])*-0.968) + ((dataset['%% Successful Crosses'])*-0.025) + ((dataset['Total Indirect FK'])*-0.859) + ((dataset['Key Passes'])*-1.958) + ((dataset['Expected Assists'])*13.346) + ((dataset['Assists'])*4.365) + ((dataset['Cleansheet'])*5.706) + ((dataset['Creativity'])*0.157) + ((dataset['Influence'])*0.120) + ((dataset['xAtt'])*-5.573) + ((dataset['Expected Points'])*0.996) + ((dataset['Bonus Points'])*0.672) + ((dataset['Points'])*-1.688) + ((dataset['Goals Conceded'])*-1.890) + ((dataset['%% Accurate Tackles'])*0.005) + ((dataset['Recovery'])*0.078) + ((dataset['Blocks'])*-0.683) + ((dataset['Shots Conceded'])*0.273) + ((dataset['Shots Conceded In Box'])*-0.324) + ((dataset['Shots Conceded OT'])*-0.800) + ((dataset['SP'])*0.913) + ((dataset['Headed Shots Conceded'])*-0.464) + ((dataset['xGC'])*4.149) + ((dataset['Total Throughballs'])*1.017) + ((dataset['Touches in Box'])*0.313) + ((dataset['Entries into Final 3rd'])*-.077) + ((dataset['Corners into Box'])*0.555) + ((dataset['Total Direct FK'])*-1.304) - 1.154)

dataset['Predict1'] = 50 # else statement
dataset.loc[dataset['Price'] >= 5, 'Predict1'] = Price_Range # first if statement

dataset.loc[dataset['Price'] < 4.5, 'Predict1'] = 1000 #then the elif equivalent
print(dataset[['Name', 'Price', 'Predict1']])

# dependent_variable = '3GW'
# unneeded_variables1 = 'Name'
# unneeded_variables2 = '£M'
# unneeded_variables3 = 'App'
# unneeded_variables4 = 'Mins'
# unneeded_variables5 = 'Starts'
# unneeded_variables6 = 'Sub on'
# unneeded_variables7 = 'Sub off'

# independent_variables = dataset.columns.tolist()
# independent_variables.remove(dependent_variable)
# independent_variables.remove(unneeded_variables1)
# independent_variables.remove(unneeded_variables2)
# independent_variables.remove(unneeded_variables3)
# independent_variables.remove(unneeded_variables4)
# independent_variables.remove(unneeded_variables5)
# independent_variables.remove(unneeded_variables6)
# independent_variables.remove(unneeded_variables7)

# x = dataset[independent_variables]
# y = dataset[dependent_variable]

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.00000000001, random_state=0, shuffle=True)

# mlr = LinearRegression()
# mlr.fit(x_train, y_train)

# print("Intercept: ", mlr.intercept_)
# print("Coefficients:")
# print(list(zip(x, mlr.coef_)))

# y_pred_mlr = mlr.predict(x_test)
# mlr_diff = pd.DataFrame({'Actual Value': y_test, 'Predicted': y_pred_mlr})

# # mlr_diff.to_excel('mid_budget_prediction.xlsx', index=False)

# ajusted_r2 = 1 - (1-mlr.score(x_train, y_train))*(len(y_train)-1)/(len(y_train)-x.shape[1]-1)

# # print(mlr.score(x_train, y_train)) # Prints out the R2
# # print(ajusted_r2)