# Hyper parameter tuning! 
# now need for spliting into train and test data set

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import GridSearchCV  
from sklearn.datasets import load_iris

from sklearn.svm import SVC
# creating the dataset
iris = load_iris()
dir(iris)

ds = pd.DataFrame(iris.data, columns = iris.feature_names)
ds["Target"] = iris.target
ds["Target_Names"] = ds.Target.replace([0, 1, 2],['setosa', 'versicolor', 'virginica'])

X = ds.iloc[:,:-2].values
y = ds.iloc[:, -2].values

 # for Gridsearch: it works all possible tuning
 # takes long for bigger data set.
 
classifier2 = GridSearchCV(SVC(), {"C":[1,10,20],
                          "kernel":["linear","poly", "rbf"]},
                            cv = 5, return_train_score=False)
classifier2.fit(X,y)
dir(classifier2)

classifier2.best_score_
classifier2.best_params_
classifier2.cv_results_

res_df = pd.DataFrame(classifier2.cv_results_)
res_df[['param_C', 'param_kernel', 'mean_test_score']]

# for large datasets we can use(more than 100000 rows)
from sklearn.model_selection import RandomizedSearchCV
 
classifier1 = RandomizedSearchCV(SVC(), {"C":[1,10,20],
                          "kernel":["linear","poly", "rbf"]},
                            cv = 5, return_train_score=False,
                            n_iter = 3)   # n_iter will decide number of output rows
                                        # n_iter selects randoms permutation and combinations
classifier1.fit(X,y)
res_df_ran = pd.DataFrame(classifier1.cv_results_)
res_df_ran[['param_C', 'param_kernel', 'mean_test_score']]

# ------------------------------------God Model------------------------------------

# all Classification model,
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

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
        
