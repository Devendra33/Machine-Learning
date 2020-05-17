# ML practice
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# importing the dataset  
dataset = pd.read_csv("data.csv")

# splitting into dependent and independ variable.
ind = dataset.iloc[:,0:3].values
dep = dataset.iloc[:,3:4].values

# handling missing values

imp = SimpleImputer(missing_values = np.nan, strategy ="median" )
ind[:,1:3] = imp.fit_transform(ind[:,1:3])

# handling categorical (for independent dataset)
label_ind = LabelEncoder()
ind[:,0] = label_ind.fit_transform(ind[:,0]) 
ohe = OneHotEncoder(categorical_features = [0])
ind = ohe.fit_transform(ind).toarray()

# handling categorical (for dependent dataset)
label_dep = LabelEncoder()
dep = label_dep.fit_transform(dep)

# testing and training

from sklearn.model_selection import train_test_split
ind_train, ind_test, dep_train, dep_test = train_test_split(ind, dep, test_size = 0.2, random_state = 0)

# feature scaling  (only apply on independent data)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
ind_train = sc.fit_transform(ind_train)
ind_test = sc.transform(ind_test)     # already fitted.q