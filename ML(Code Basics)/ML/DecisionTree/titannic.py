# to classify whether the passenger survived or not.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

#importing the dataset
ds = pd.read_csv("titanic.csv")

ds = ds.drop(columns = ["PassengerId", "Name",'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked' ])
ds.Age = ds.Age.fillna(25)   # 25 is appropiate guessing age.

x = ds.iloc[:,1:].values
y = ds.iloc[:,0].values

# data preprocessing steps
le_gen = LabelEncoder()
x[:,1] =  le_gen.fit_transform(x[:,1]) 


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 50)

classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
classifier.score(x_test, y_test)     # 85 % accurate model

