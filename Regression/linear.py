import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import average_precision_score, accuracy_score, f1_score
import csv

# Minimum FPL points for regression analysis i.e. if 5 then any player that is predicted to score 5 and actually scores 5 is counted as an accuracy
REGRESS = 4

# Repeat the regression 10,000 times so I can take the average
for _ in range(10001):

    # Load the csv as a panda
    dataset = pd.read_csv("GK PerApp 6GWs.csv")

    # Drop the columns that are not going to be used in the regression
    dataset.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position"], axis=1, inplace=True)

    # Setting up the values of x and y
    x = dataset.drop(["Points_y"], axis=1, inplace=False)
    y = dataset["Points_y"]

    # Assign the data which is for test. Remove random_state so each run is 100% randomised
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # Assign model
    model = LinearRegression()

    # Fit to model
    model.fit(x_train, y_train)

    # Run prediction of x_test data using the result from the multi regression
    y_predict = model.predict(x_test)

    # Turn the prediction and the y_test into list of ints because of the accuracy tests to be run
    y_test = [int(x) for x in y_test]
    y_predict = [int(x) for x in y_predict]

    # If the value is equal or above REGRESS, then turn it to 1
    final_predict = [1 if num >= REGRESS else 0 for num in y_predict]

    final_test = [1 if num >= REGRESS else 0 for num in y_test]

    # Run accuracy score for 2 scenarios
    # Scenario 1 - If predicted score is exact same as actual score
    # Scenario 2 - If actual score is equal or more than predicted REGRESS. Else don't consider the player
    exact_score_accuracy = str(accuracy_score(y_test, y_predict))
    binary_accuracy = str(accuracy_score(final_test, final_predict))

    total_positive_labels = 0
    guessed_positive_labels = 0
    total_negative_labels = 0
    guessed_negative_labels = 0

    for i in range(len(final_test)):
        if final_test[i] == 1:
            total_positive_labels += 1
            if final_test[i] == final_predict[i]:
                guessed_positive_labels += 1
        elif final_test[i] == 0:
            total_negative_labels += 1
            if final_test[i] == final_predict[i]:
                guessed_negative_labels += 1

    true_positive_rate = guessed_positive_labels / total_positive_labels

    true_negative_rate = guessed_negative_labels / total_negative_labels

    f_score = f1_score(final_test, final_predict)

    # Write all the results to a CSV
    with open("results.csv", "a", newline="\n") as file:
        file.write(exact_score_accuracy)
        file.write(",")
        file.write(binary_accuracy)
        file.write(",")
        file.write(str(true_positive_rate))
        file.write(",")
        file.write(str(f_score))
        file.write("\n")

