# simple linear regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

ds = pd.read_csv("canada_per_capita_income.csv",header = 1, names = ["year", "income"])
x = ds.iloc[:,0:1].values
y = ds.iloc[:,1].values

# making the model with whole data set 
regress = LinearRegression()
regress.fit(x,y)

# now predicting the per capita income of year 2020
regress.predict([[2016]])