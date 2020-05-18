# Decision tree Regression: Feature scaling is not required.
# it is used when there are many independent variable not suited for only 1 independent varaible ds.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

ds = pd.read_csv("Position_Salaries.csv")

x = ds.iloc[:,1:2].values
y = ds.iloc[:,2].values

# training the Decision tree model
degress = DecisionTreeRegressor(random_state = 0)   # for predicting a numeric value
degress.fit(x, y)

# predicting the value 
degress.predict([[6.5]]) 

#visualizing the DecisionTreeRegression
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x, y, color = "red")
plt.plot(x_grid, degress.predict(x_grid), color = "blue")
plt.title("position vs salaries (Decision tree regression)")
plt.xlabel("position")
plt.ylabel("salaries")
plt.show()

