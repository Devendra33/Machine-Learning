# Creating a support vector model using Support Vector Mchine
from sklearn.datasets import load_iris

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()
dir(iris)

ds = pd.DataFrame(iris.data, columns = iris.feature_names)

# Adding the target variables 
ds["Target"] = iris.target

# Adding the target names to variables

ds["flowers"] = ds.Target.apply(lambda x : iris.target_names[x])

# dependent and indepenf variables
X = ds.iloc[:,0:4].values
y = ds.iloc[:, 4].values

# creating a csv file to access it easily
ds.to_csv("iris_data.csv", index = False)

# train & test split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.1, random_state = 0)

# Training the Model
classifier = SVC(kernel = "rbf") # radial basis function
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)  # 100 % accuracy


# now visualizing the data set
df0 =  ds[ds.Target == 0] # setosa
df1 =  ds[ds.Target == 1] # versicolor
df2 =  ds[ds.Target == 2] # virginica

# for sepal
plt.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], color = "red" ,label = "setosa")
plt.scatter(df1["sepal length (cm)"], df1["sepal width (cm)"], color = "blue", label = "versicolor")
plt.scatter(df2["sepal length (cm)"], df2["sepal width (cm)"], color = "cyan", label = "virginica")
plt.title("visualization for sepals")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.legend()
plt.show()


# for petal
plt.scatter(df0["petal length (cm)"], df0["petal width (cm)"], color = "red" ,label = "setosa")
plt.scatter(df1["petal length (cm)"], df1["petal width (cm)"], color = "blue", label = "versicolor")
plt.scatter(df2["petal length (cm)"], df2["petal width (cm)"], color = "cyan", label = "virginica")
plt.title("visualization for petals")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.legend()
plt.show()
