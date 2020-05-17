# predicting the salary.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import statsmodels.api as sm
from word2number import w2n

# data preprecess steps are complete.

ds = pd.read_csv("hiring.csv", header = 0, names = ["experience", "test_score", "interview_score","salary"])
ds.experience = ds.experience.fillna("Zero")

from math import floor
ds.test_score = ds.test_score.fillna(floor(ds.test_score.mean()))

# to apply w2n on a perticular colum use 
#d.experience = d.experience.apply(w2n.word_to_num)   # (I M P O R T A N T)


lst = list(set(ds.experience))
temp = []
for i in lst:
    temp.append(w2n.word_to_num(i))

ds.replace(lst,temp, inplace = True)

# multivariate regression

regress = LinearRegression()
regress.fit(ds[["experience","test_score","interview_score"]],ds["salary"])

regress.coef_    # b0 +b1x1+b2x2.......bnxn, b0 == intercept, b1,b2,...,bn is coefecients
regress.intercept_


# now predicting the values

regress.predict([[2,9,6]])     # predicted sal = 53713.86677124  
regress.predict([[12,10,10]])  # predicted sal = 93747.79628651
