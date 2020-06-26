# Logistic Regression for iris flower dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# now loading the data set
from sklearn.datasets import load_iris
iris = load_iris()

# creating a pandas dataframe
ds = pd.DataFrame(iris.data, columns = iris.feature_names)
ds["Target"] = iris.target

ds["Name"] = ds.Target.replace([0, 1, 2],['setosa', 'versicolor', 'virginica'])
ds.to_csv("Iris_Data.csv", index = False)

X = ds.iloc[:, 0:4].values
y = ds.iloc[:,4].values

# spliting into training and test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)

# fitting the model

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)
y_pred = classifier.predict(X_test)

# now creating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# creating the confusion matrix for better visualization using seborn

import seaborn as sn
plt.figure(figsize = (6,5))
sn.heatmap(cm, annot = True)
plt.title("Iris Dataset")
plt.xlabel("predicted")
plt.ylabel("Truth")