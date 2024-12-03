import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:

x = x.reshape(-1, 1)

# Create the model

model = LinearRegression().fit(x, y)

# labels axes and creates scatterplot

plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure vs. Age")

# Find the coefficient, bias, and r squared values.

coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)


# Each should be a float and rounded to two decimal places. 

# Print out the linear equation and r squared value

print(f"Model's Linear Equation: y = {coef}x + {intercept}")
print(f"R Squared value: {r_squared}")

plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

### Predict the the blood pressure of someone who is 43 years old.

prediction = model.predict([[43]])

print(f"Prediction when x is {43}: {prediction}")

### Print out the prediction

### Create the model in matplotlib and include the line of best fit

plt.scatter(x,y, c="blue")
plt.scatter(43, prediction, c="purple")

plt.legend()
plt.show()