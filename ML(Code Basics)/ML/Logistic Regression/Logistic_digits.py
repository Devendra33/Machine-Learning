# logistic Regression model for digit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import load_digits

digit = load_digits()
# for showing the images
for i in range(4):
    plt.matshow(digit.images[i])

ds = pd.DataFrame(digit.data)
ds["Target"] = digit.target
ds.to_csv("Digits_Data.csv", index = False)

X = ds.iloc[:,:-1].values
y = ds.iloc[:,-1].values

# traning and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size  = 0.2)

# fittingg into the model
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)
y_pred = classifier.predict(X_test)

# now creating the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# creating the confusion matrix for better visualization using seborn
import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot = True)
plt.xlabel("predicted")
plt.ylabel("Truth")