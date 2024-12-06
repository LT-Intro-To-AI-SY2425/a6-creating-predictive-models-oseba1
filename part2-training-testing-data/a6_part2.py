import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

x = x.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
rSquared = model.score(x_train, x_train)

print("Model's Linear Equation: y=",coef, "x+", intercept)
print("R Squared value:", rSquared)

predict = model.predict(x_test)

predict = np.around(predict, 2)

for index in range(len(x_test)):
    actual = y_test[index]
    predicted_y = predict[index]
    x_coord = x_test[index]

plt.figure(figsize=(5,4))

plt.scatter(x_train,y_train, c="blue", label="Training Data")
plt.scatter(x_test, y_test, c="purple", label="Testing Data")

plt.scatter(x_test, predict, c="red", label="Predictions")

plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure by Age")
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()

# Create your training and testing datasets:

# Use reshape to turn the x values into 2D arrays:
# xtrain = xtrain.reshape(-1,1)

# Create the model

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 


# Print out the linear equation and r squared value:

'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array

# get the predicted y values for the xtest values - returns an array of the results

# round the value in the np array to 2 decimal places


# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''