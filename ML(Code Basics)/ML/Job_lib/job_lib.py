# Joblib : used to save the object of the model to a external file so,
# we dont have to train the model every time we use it just load the external file and use it.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

# importing the data set
ds = pd.read_csv("Salary_Data.csv")
x = ds.iloc[:, 0:1].values
y = ds.iloc[:, 1].values

# fitting the model LinearRegresison
reg = LinearRegression()
reg.fit(x, y)
reg.predict([[2]])


joblib.dump(reg, "sal_reg")   # dumping the model

obj = joblib.load("sal_reg")   # loading the model back in the memory

obj.predict([[2]])   # prediction using joblib.

