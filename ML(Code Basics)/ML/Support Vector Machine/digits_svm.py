# Creating a support vector model using Support Vector Mchine
from sklearn.datasets import load_digits

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digit = load_digits()
# to show the image
dir(digit)
for i in range(5):
    plt.matshow(digit.images[i])


ds = pd.DataFrame(digit.data)

ds["Target"] = digit.target

ds.to_csv("digit_data.csv", index = False)
X = ds.iloc[:,:-1].values
y = ds.iloc[:,-1].values

# train & test split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

# Training the Model
classifier = SVC(C=15.0, kernel='rbf', degree=3, gamma='scale', random_state = 0) # radial basis function
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)  # 99.61% accuracy

y_pred = classifier.predict(X_test)
# creating the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# visualizing confusion matrix
import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot = True)
plt.title("Digit Dataset.")
plt.xlabel("predicted")
plt.ylabel("Truth")