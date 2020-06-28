# Naive bayes theoram
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# importing the dataset

ds = pd.read_csv("titanic.csv")
ds = ds.drop(columns = ['PassengerId', 'Name', 'SibSp', 'Parch',
       'Ticket', 'Fare', 'Cabin', 'Embarked'])

# now data  preprcessiing
lab = LabelEncoder()
ds["Sex"][:] = lab.fit_transform(ds["Sex"][:])
ds.Age = ds.fillna(ds.Age.mean())

X = ds.iloc[:,:-1].values
y = ds.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Now fitting into the Gausian model

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)

y_pred  = classifier.predict(X_test) # predicted values

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)
