# Polynomial Regression.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# importing the data set
ds = pd.read_csv("Position_Salaries.csv")

x = ds.iloc[:,1:2].values
y = ds.iloc[:,2].values

# Polynomial linear regression model
# converting into b0+b1x1^1+b2x2^2+b3x3^3......bnxn^n.
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)

#fitting into linear model.
regress = LinearRegression()
regress.fit(x_poly, y)

# visualisation of polynomial  regression.
x_grid = np.arange(min(x), max(x), 0.1)    # for smoothing of line.
x_grid = x_grid.reshape(len(x_grid), 1)    # now it is converted into matrix form.
plt.scatter(x,y, color = "red")
plt.plot(x_grid, regress.predict(poly_reg.fit_transform(x_grid)), color  = "blue" )
plt.title("polynomial regression")
plt.xlabel("Postion")
plt.ylabel("Salary")
plt.show()
 
# prediction of new result using polynomial regression.
regress.predict(poly_reg.fit_transform(np.array([6.5]).reshape(1, 1)))