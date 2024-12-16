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


print("***************")
print("Testing Results")

predict = model.predict(xtest)
predit = np.around(predict, 2)
print(f"R Squared value: {r_squared}")

for index in range(len(xtest)):
    miles = xtest[index]
    actual = ytest[index]
    predicted = predict[index]
    print(f"Age: {float(miles[1])}, Mileage: {float(miles[0])}, Predicted price:{ predicted}, Actual price:{actual}")



