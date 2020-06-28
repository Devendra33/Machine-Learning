# Spam detection Model by  Naive_bayes theorem

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB

# importing the dataset
ds = pd.read_csv("spam.csv")
ds["spam"] = ds.Category.apply(lambda x: 1 if x == "spam" else 0)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(ds.Message, ds.spam, test_size = 0.2)



from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# takes pandas series module to use vectorize method
classifier = Pipeline([("vectorizer", CountVectorizer()),("nb", MultinomialNB())])
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)   # 98% accuracy.

y_pred = classifier.predict(X_test)
