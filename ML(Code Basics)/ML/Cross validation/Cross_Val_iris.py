# selction best model for iris data sets

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.datasets import load_iris

iris = load_iris()

# creating the dataframe
ds = pd.DataFrame(iris.data, columns = iris.feature_names)
ds["Target"] = iris.target
ds["Name"]  = ds.Target.apply(lambda x: iris.target_names[x])

X = ds.iloc[:,0:4].values
y = ds.iloc[:, 4].values

dic = {}

# for logistic regression
lst_lg = cross_val_score(LogisticRegression(),X, y, cv = 5)
lg_score = lst_lg.mean()
dic["logistic regression"] = lg_score

# for support vector machine
lst_svc = cross_val_score(SVC(),X, y, cv = 5)
svc_score = lst_svc.mean()
dic["support vector machine"] = svc_score

# for randomforest classificaction
lst_rf = cross_val_score(RandomForestClassifier(n_estimators = 10),X, y, cv = 5)
rf_score = lst_rf.mean()
dic["randomforest classificaction"] = rf_score

# for decsion tree.
lst_dt = cross_val_score(DecisionTreeClassifier(criterion = "entropy"),X, y, cv = 5)
dt_score = lst_dt.mean()
dic["Decision Tree Classifier"] = dt_score

max_score = max(dic.values())
print("_________________________________________________________________________")
print("\n")

for k, v in dic.items():
    if v == max_score:
        print(f"The Best Model is:\n\t{k} ")
