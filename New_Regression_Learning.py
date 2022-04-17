import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn import metrics
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR


df = pd.read_excel('Prediction Analysis - Copy\FWD3GW-Premium.xlsx', sheet_name='3GWs')

df.isnull().sum() # Checks if the dataype of every Stat is as per our expectation
# df.info() # Checks if all the datatypes are as expected i.e. floats in this case


# # Plot scatter plot of every variable against 3GW except Appearances, Name and 3GW itself
# sns.pairplot(df, x_vars = df.drop(['App', 'Name', '3GW'], axis = 1, inplace=False).columns, y_vars=['3GW'])
# plt.show() 

# Create a list of continuous variables
linear_vars = df.select_dtypes(include=[np.number]).columns

# this removes dataframe’s outliers inplace
def removeoutliers(df, listvars, z):
    for var in listvars:
        df1 = df[np.abs(stats.zscore(df[var])) < z]
    return df1

# remove outliers where z score > 3
df = removeoutliers(df, linear_vars,3)

# Setup dataFrames for both X and y
X = df.drop(['3GW', 'Name', '£M', 'App', 'Starts', 'Sub on', 'Sub off'], axis=1, inplace=False)
y = df[['3GW']]

# #Convert variables to log
# def convertfeatures2log(df, listvars):
#    for var in listvars:
#     df[var] = np.log(df[var])
# convertfeatures2log(X, X.columns)
# convertfeatures2log(y, y.columns)
# y.hist(bins=20)

#Test Train Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.00000000001, random_state=0)

#Use Random Forrest ML Method
rf = RandomForestRegressor(n_estimators = 300)
model = rf.fit(X_train,y_train.values.ravel())
y_pred = rf.predict(X_test)

print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
print('MSE:', metrics.mean_squared_error(y_test, y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# models=[]
# models.append(('LR', LinearRegression()))
# models.append(('RF', RandomForestRegressor(n_estimators=100)))
# models.append(('KNN', KNeighborsRegressor()))
# models.append(('CART', DecisionTreeRegressor()))
# models.append(('SVR',SVR(gamma='auto')))

# # now evaluate each model 
# results = []
# names = []
# print("model: mean of score across 10 folds (std dev of score)")

# for name, model in models:
#     # --> split training dataset into 10 parts; train on 9 and test on 1; repeat for all combinations.
#     kfold = KFold(n_splits=10)
#     cv_results = cross_val_score(model, X_train, y_train, cv=kfold)
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)