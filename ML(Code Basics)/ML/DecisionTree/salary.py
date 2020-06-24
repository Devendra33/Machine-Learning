# To predict the employees salary is greater than 100k or not.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

ds = pd.read_csv("salaries.csv") 
x = ds.iloc[:, 0:3].values
y = ds.iloc[:, 3].values
 
# Now data preprocessing step
le_comp = LabelEncoder()
le_pos = LabelEncoder()
le_deg = LabelEncoder()

x[:,0] = le_comp.fit_transform(x[:,0])
x[:,1] = le_comp.fit_transform(x[:,1])
x[:,2] = le_comp.fit_transform(x[:,2])

# now fitting into the model
classifier = DecisionTreeClassifier()
classifier.fit(x,y)
classifier.score(x,y)
classifier.predict([[2,0,0]])   # gives Output: 1.