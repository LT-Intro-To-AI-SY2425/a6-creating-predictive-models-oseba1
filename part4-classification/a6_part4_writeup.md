# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

It was around 0.70. StandardScaler balances the data so that they are relative to eachother, so remoivng this would make the model weigh certain varibles more than others.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

It was 0.87 accurate. I think for this purpose it is pretty good and could be used for this use case because it is not that high stakes.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

There was not a super obvious pattern but some of the errors seemed to be around middle aged people.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

She would not buy an SUV.