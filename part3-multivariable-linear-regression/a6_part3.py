import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values


xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2)

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 

coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y),2)

#Loop through the data and print out the predicted prices and the 
#actual prices

predict = model.predict(xtest)
predit = np.around(predict, 2)

for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]


plt.scatter(xtrain, ytrain, c="blue", label="Training Data")
plt.scatter(xtest, ytest, c="purple", label="Testing Data")

plt.scatter(xtest, predict, c="red", label="Predictions")

plt.xlabel("Car")
plt.ylabel("Price")
plt.title("Price by Car")
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()

print("***************")
print("Testing Results")