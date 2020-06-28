# Naive bayes model for wine data set of sklearn library.
# classifier1 by GaussianNB 
# classifier2 by MultinomialNB

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.metrics import r2_score

# importing the dataset
wine = load_wine() 
dir(wine)

# creating the dataset
ds = pd.DataFrame(wine.data, columns = wine.feature_names)
ds["Target"] = wine.target
ds["Target_names"] = ds.Target.replace([0, 1, 2], ['class_0', 'class_1', 'class_2'])
ds.to_csv("Wine_Data.csv", index = False)

X = ds.iloc[:, :-2].values
y = ds.iloc[:, -2].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

classifier1 = GaussianNB()
classifier2 = MultinomialNB()

classifier1.fit(X_train, y_train)
classifier1.score(X_test, y_test)   # 100 % accuracy  aquired.
y1_pred = classifier1.predict(X_test)
r2_score(y_test, y1_pred)

classifier2.fit(X_train, y_train)
classifier2.score(X_test, y_test) # 91.6 % accuracy aquired.
y2_pred = classifier2.predict(X_test)
r2_score(y_test, y2_pred)


