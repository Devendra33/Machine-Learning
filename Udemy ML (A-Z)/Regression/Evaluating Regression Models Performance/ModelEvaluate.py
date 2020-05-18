# projects that gives the best linear model suitable for data set.
# works only when the data set is preprocessed.
# the dependent variable must be at the end.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import statsmodels.api as sm

# preprcess dataset here.

# preprocess ends here....

# Read preprocessed file here.
 
ds = pd.read_csv("pre_beaver.csv")

x = ds.iloc[:,:-1].values
y = ds.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state = 0)

def bestlinearmodel(x_train, x_test, y_train, y_test):
    # Linear Regression ::   lin_reg.predict() (Model)
    dic = {}
    if len(x_train[0:1].ravel()) == 1:
        
        lin_reg = LinearRegression()
        lin_reg.fit(x_train, y_train)
        lin_pred = lin_reg.predict(x_test)
        dic["Simple_Linear_Regression: "] = r2_score(y_test, lin_pred)
    
    # Multiple Linear Regression :: mul_reg.predict()     (Model)
    
    mul_reg = LinearRegression()
    mul_reg.fit(x_train, y_train)
    mul_pred = mul_reg.predict(x_test)
    dic["Multiple_Linear_Regression: "] = r2_score(y_test, mul_pred)
    
    # Polynomial linear regression :: pol_reg.predict()    (Model)
    poly_reg = PolynomialFeatures(degree = 3)
    x_poly = poly_reg.fit_transform(x_train)
    pol_reg = LinearRegression()
    pol_reg.fit(x_poly, y_train)
    pol_pred = pol_reg.predict(poly_reg.fit_transform(x_test))
    dic["Polynomial_Linear_Regression: "] = r2_score(y_test, pol_pred)
    
    # Decision tree Regression::dec_reg                            (Model)
    
    dec_reg = DecisionTreeRegressor(random_state = 0)
    dec_reg.fit(x_train, y_train)
    dec_pred = dec_reg.predict(x_test)
    dic["Decision_Tree_Regression: "] = r2_score(y_test, dec_pred)
    
    # Random forest Regression                             (Model)
    ran_reg = RandomForestRegressor(n_estimators = 10, random_state = 0)
    ran_reg.fit(x_train, y_train)
    ran_pred = ran_reg.predict(x_test)    
    dic["Random_Forest_Regression: "] = r2_score(y_test, ran_pred)
    
    # Support Vector Regression :: svr_reg.predict()          (Model)
    # performing feature scaling.    
    dec = 0
    if min(y_train) >= 0 and max(y) <= 3:
        sc_x = StandardScaler()
        x_train = sc_x.fit_transform(x_train)
        x_test = sc_x.transform(x_test)
        dec = 1
    else:
        y_test = y_test.reshape(len(y_test),1)
        y_train = y_train.reshape(len(y_train),1)
        sc_x = StandardScaler()
        sc_y = StandardScaler()
        x_train = sc_x.fit_transform(x_train)
        x_test = sc_x.transform(x_test)
        y_train = sc_y.fit_transform(y_train)
        y_test = sc_y.transform(y_test)
        
    svr_reg = SVR(kernel = "rbf")
    svr_reg.fit(x_train, y_train)
    
    if dec == 1:
        y_pred = svr_reg.predict(x_test)
        dic["Support_Vector_Regression: "] = r2_score(y_test, y_pred)   # yeh y me values normal hai
    else:
        y_pred = sc_y.inverse_transform(svr_reg.predict(x_test))
        dic["Support_Vector_Regression: "] = r2_score(sc_y.inverse_transform(y_test), y_pred)  # isme values inverse krna padega
    
    return dic
    
d = bestlinearmodel(x_train, x_test, y_train, y_test)
m = max(d.values())
for k, v in d.items():
    print(k, v)
    if m == v:
        model = k
        mv = v
print(end = "\n\n\n")
if len(x_train[0:1].ravel()) == 1:
    plt.scatter(x_train, y_train, color = "red")
    #plt.plot(x_train, lin_reg.predict(x_train), color = "blue") # to see only scattering
    plt.title("Graph")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()
        
print("The best Model is:\n      ", model, mv)
print(end = "\n\n\n\n")