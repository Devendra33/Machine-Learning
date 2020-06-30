# One Hot encoding without using sklearn library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing the dataset
ds = pd.read_csv("carprices.csv")

dum = pd.get_dummies(ds["Car Model"])
ds = pd.concat([ds, dum], axis = "columns")

ds.drop(["Car Model", "Audi A5"], axis = "columns", inplace = True)

x = ds.iloc[:,[0, 2, 3, 4]].values
y = ds.iloc[:, 1].values

# training the dataset by multiple linear regressioln
from sklearn.linear_model import LinearRegression

regress = LinearRegression()
regress.fit(x,y)
regress.score(x,y)   


# 1. predict the price of mercedes benz that is 4 yr old with mileage 45000
regress.predict([[45000, 4, 0, 1]])  # 36991.31721061

# 2. predict the price of a BMW X5 that is  7yr old with milege 86000
regress.predict([[86000, 7, 1, 0]])  # 11080.74313219

# 3. Tell me the score(accuracy) of your model
regress.score(x,y)   # 0.9417050937281082