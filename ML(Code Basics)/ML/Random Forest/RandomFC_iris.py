import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

# creating the dataset ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
#                                 'petal width (cm)'],
ds = pd.DataFrame(iris.data, columns = iris.feature_names)
ds["Target"] = iris.target
ds["Names"] = ds.Target.apply(lambda x: iris.target_names[x])
ds.to_csv("fower_data.csv", index = False)

X = ds.iloc[:, 0:4].values
y = ds.iloc[:, 4].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)

# fitiing into the model
classifier = RandomForestClassifier(n_estimators = 10, criterion = "entropy", random_state = 0)
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
