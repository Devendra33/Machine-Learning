# Used to select the best model for given set of data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

from sklearn.datasets import load_digits

digit = load_digits()

# creating the pandas dataframe
ds = pd.DataFrame(digit.data)
ds["Target"] = digit.target

X = ds.iloc[:, :-1].values
y = ds.iloc[:, -1].values
dic = {}
# for logistic regression

lst_lg = cross_val_score(LogisticRegression(), X, y, cv = 5)
lg_score = lst_lg.mean()
dic["logistic regression"] = lg_score

# for support vector machine
lst_svc = cross_val_score(SVC(), X, y, cv = 5)
svc_score = lst_svc.mean()
dic["support vector machine"] = svc_score

# for Random forest classifier
lst_rf = cross_val_score(RandomForestClassifier(n_estimators = 25), X, y, cv = 5)
rf_score = lst_rf.mean()
dic["Random forest classifier"] = rf_score

max_score = max(dic.values())
print("_________________________________________________________________________")
print("\n")

for k, v in dic.items():
    if v == max_score:
        print(f"The Best Model is:\n\t{k} ")

