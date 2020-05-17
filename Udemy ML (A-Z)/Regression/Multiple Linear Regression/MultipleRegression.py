# Multiple Linear Regression
# important methods
# backward elimination  
# forward selection 
# bi-direction elimination
# we do not need to perform feature scaling.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# importing the dataset
ds = pd.read_csv("50_Startups.csv")

x = ds.iloc[:,0:4].values
y = ds.iloc[:,4].values
 
lab_x = LabelEncoder()
x[:,3] = lab_x.fit_transform(x[:,3])
ohe = OneHotEncoder(categorical_features = [3])
x = ohe.fit_transform(x).toarray()

# taking care of dummy variable trap
x = x[:,1:]        # for some softwares it is nesscary to do this but librabry takes care of it in this course

# spliting the data into train and test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/5, random_state = 0)

# Fitting the training data into regressor.
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicting the value
y_pred = regressor.predict(x_test)

#  now to perform backward elimination we add 1 in front of dataset(x), bcoz, y = b0 + b1x1 + b2x2+...+bnxn.
x = np.append(arr = np.ones((50,1)).astype(int), values = x, axis = 1)

# performing the backword elimination method.
import statsmodels.api as sm
 # SL = 0.5   (Significance Level)
x_opt = x[:,[0,1,2,3,4,5]]
regress_OLS = sm.OLS(endog = y, exog = x_opt).fit()   #endog = dependent , exog = optimal matrix.
regress_OLS.summary()      # remove 1 bcoz of highest significance value
x_opt = x[:,[0,2,3,4,5]]
regress_OLS = sm.OLS(endog = y, exog =x_opt).fit()
regress_OLS.summary()  # remove 2 
x_opt = x[:,[0,3,4,5]]
regress_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regress_OLS.summary()  # remove 4
x_opt = x[:,[0,3,5]]
regress_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regress_OLS.summary()  # remove 5
x_opt = x[:,[0,3]]
regress_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regress_OLS.summary()

