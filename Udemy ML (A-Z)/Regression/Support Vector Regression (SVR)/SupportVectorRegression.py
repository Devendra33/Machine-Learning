# Support vector regression: It is a part in SVM, works mostly like linear regression but the only difference is
# linear regression just tries to minimize the error and in SVR it tries to reduce error with in boundaries.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
 
ds = pd.read_csv("Position_Salaries.csv")

x = ds.iloc[:,1:2].values
y = ds.iloc[:,2].values
y = y.reshape(len(y),1) # (for performing standard scaling we must pass 2D array or else it give error)

# Always perform feature scaling in SVR
# performing feature scaling.

sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)

# troin the model for svr set 
svr = SVR(kernel = 'rbf')
svr.fit(x,y)

# Now predicting the value. 
sc_y.inverse_transform(svr.predict(sc_x.transform([[6.5]])))

# visualizing the svr
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = "red")
plt.plot(sc_x.inverse_transform(x), sc_y.inverse_transform(svr.predict(x)))
plt.title("Positon Vs Salary")
plt.xlabel("Position")
plt.ylabel("Salary")
plt.show()

# in higher resolution
x_grid = np.arange(min(sc_x.inverse_transform(x)), max(sc_x.inverse_transform(x)), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = "red")
plt.plot(x_grid, sc_y.inverse_transform(svr.predict(sc_x.transform(x_grid))))
plt.title("Positon Vs Salary")
plt.xlabel("Position")
plt.ylabel("Salary")
plt.show()
