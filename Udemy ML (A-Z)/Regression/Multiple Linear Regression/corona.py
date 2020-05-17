import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

ds = pd.read_csv("corona.txt", sep = " ")
ds.Day = ds.Day + 1
ds = ds[["months","Day","new_cases"]]
x = ds.iloc[:,1:2].values
y = ds.iloc[:, 2].values

# polynomial regression
x_poly = PolynomialFeatures(degree = 4)
x_in = x_poly.fit_transform(x)
regress = LinearRegression()
regress.fit(x_in,y)

#visualization

plt.scatter(x,y, color = "red")
plt.plot(x, regress.predict(x_poly.fit_transform(x)), color = "blue")
plt.title("Corona cases in India")
plt.xlabel("Per Day")
plt.ylabel("Frequency")
plt.show()