# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

The R Squared coefficient was 0.86. This means that the model was pretty good at predicting the price.

2. Is your model accurate? Why or why not?

The R Squared value was fairly high. The model was pretty good at predicting the price. The predicted price was usually within 1,000 dollars of the actual price.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

For the 10-year-old car it predicted a price of around 13,000. For the 20-year-old car it predicted a price of around -600.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Because it follows the linear line, for something with large value it will follow the line downwards in the negatives.