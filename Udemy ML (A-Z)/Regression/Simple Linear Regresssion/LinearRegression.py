# Simple Linear Regression Model
# use when only there is one column in independent variable
# use for prediction the salaries, profits, etc..

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
# reading the dataset.
ds = pd.read_csv("Salary_Data.csv")

# independent and dependent dataset
ind = ds.iloc[:, :-1].values      # must be in form of (30,1)
dep = ds.iloc[:, -1].values      # must be in form of (30,)

# for training and testing.
ind_train, ind_test, dep_train, dep_test = train_test_split(ind, dep, test_size = 1/3, random_state = 0) 

# feature scaling is not required in Simple Linear Regression.(most imp. point)

# fitting the Linear Regression model to training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(ind_train, dep_train)

# y = mx + b,  m == coeficient, b == intercept.

m = regressor.coef_
b = regressor.intercept_

# predicting the test set results
y_pred = regressor.predict(ind_test)

# visualizing the train set
plt.scatter(ind_train, dep_train, color = "red")
plt.plot(ind_train, regressor.predict(ind_train), color = "blue")
plt.title("salary vs experience(Train set)")
plt.xlabel("years of experience")
plt.ylabel("salary")
plt.show()

# visualizing the test set
plt.scatter(ind_test, dep_test, color = "red")
plt.plot(ind_train, regressor.predict(ind_train), color = "blue")
plt.title("salary vs experience(Test set)")
plt.xlabel("years of experience")
plt.ylabel("salary")
plt.show()

# model evaulation
r2_score(dep_test, y_pred)
