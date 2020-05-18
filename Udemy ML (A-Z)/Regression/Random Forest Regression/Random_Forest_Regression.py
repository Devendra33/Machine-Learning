# Random Forest: it is a version of Ensemble learning
# Ensemble learning: it is a learing in which many algoritms or a algorithm used many times and we put them 
# together to do much more powerfull than original one.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


ds = pd.read_csv("Position_Salaries.csv")
x = ds.iloc[:,1:2].values
y = ds.iloc[:,2].values
# training the model
regress = RandomForestRegressor(n_estimators = 10, random_state = 0)
regress.fit(x, y)

# predicting the values
regress.predict([[6.5]])

# visualization part
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid),1)

plt.scatter(x, y, color = "red")
plt.plot(x_grid, regress.predict(x_grid), color = "blue")
plt.title("position vs salaries")
plt.xlabel("position")
plt.ylabel("salaries")
plt.show()