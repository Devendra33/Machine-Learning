import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

ds = pd.read_csv("income.csv")

# performed feature scaling
sc = StandardScaler()
ds[["Age","Income($)"]] = sc.fit_transform(ds[["Age","Income($)"]])

# elbow method

wcss = []
for i in range(1,11):
    k = KMeans(n_clusters = i, init = "k-means++")
    k.fit(ds[["Age","Income($)"]])
    wcss.append(k.inertia_)
plt.plot(range(1,11), wcss)
plt.xlabel("frequency")
plt.ylabel("clusters")    # now we get 3 clusters by elbow method

# now fitting into kmeans model

km = KMeans(n_clusters = 3, init = "k-means++")
y_means = km.fit_predict(ds[["Age","Income($)"]])

# visualizing the graph
ds["cluster"] = y_means

ds0 = ds[ds.cluster == 0]
ds1 = ds[ds.cluster == 1]
ds2 = ds[ds.cluster == 2]

plt.scatter(ds0["Age"],ds0["Income($)"], color = "red", s = 100, label = "c1") # cluster 1
plt.scatter(ds1["Age"],ds1["Income($)"], color = "blue", s = 100, label = "c2")# cluster 2
plt.scatter(ds2["Age"],ds2["Income($)"], color = "green", s = 100, label = "c3")# cluster 3
# to represent the centers
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1], s = 400, color = "yellow", label = "centers")
plt.xlabel("clusters")
plt.ylabel("frequency")
plt.legend()
