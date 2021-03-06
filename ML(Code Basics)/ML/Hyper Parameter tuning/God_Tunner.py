# Hyper parameter tuning! 
# No need for spliting into train and test data set

# for classification

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split  
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# reading the data set
ds = pd.read_csv("iris_data.csv")

X = ds.iloc[:, :-1].values
y = ds.iloc[:, -1].values

model_params = {
        "svm":{"model":SVC(),
                "params":{"C":[1, 10, 20],
                          "kernel":["rbf","poly","linear"]},
                          
            },
        "Random_Forest":{"model":RandomForestClassifier(),
                        "params":{"n_estimators":[10,20,30],
                                  "criterion":["gini","entropy"]}
                        },
        "Logistic_Regression":{"model":LogisticRegression(),
                               "params":{"C":[1,5,10]}
                               },
        "Gaussian_NB":{"model":GaussianNB(priors=None),
                        "params":{}
                        },
         "Multinomial_NB":{"model":MultinomialNB(),
                        "params":{}
                        },
         "Bernoulli_NB":{"model":BernoulliNB(),
                        "params":{}
                        },
         "K_NN":{"model":KNeighborsClassifier(),
                        "params":{"n_neighbors":[5,9,7,9]}
                        },
         "DecisionTree_Classifier":{"model":DecisionTreeClassifier(),
                        "params":{"criterion":["gini", "entropy"]}
                        }
                } 
               
# To run model_params we need for loop.
score = []
for model_name, mp in model_params.items():
    classifier = GridSearchCV(mp["model"], mp["params"],
                              cv = 5, return_train_score=False)
    classifier.fit(X, y)
    score.append({"model":model_name,
                  "best_score":classifier.best_score_,
                  "best_params" : classifier.best_params_})
    
df = pd.DataFrame(score, columns = ["model", "best_score", "best_params"])
df[["model", "best_params","best_score"]][df.best_score == df.best_score.max()]
        
