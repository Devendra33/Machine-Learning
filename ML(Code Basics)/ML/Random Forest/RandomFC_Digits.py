import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix

digit = load_digits()
dir(digit)

# for showing some images in the dataset
for i in range(4):
    plt.matshow(digit.images[i])
    
# Creating the pandas datasets
ds = pd.DataFrame(digit.data)
ds["Target"] = digit.target
X = ds.iloc[:,:-1].values
y = ds.iloc[:, -1].values
ds.to_csv("Num_Img_Data.csv", index = False)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)

# fitting into the random forest algorithm
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10)
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)

y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# visualizing confusion matrix
import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot = True)
plt.title("Digit Dataset.")
plt.xlabel("predicted")
plt.ylabel("Truth")