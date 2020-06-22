import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
dir(iris)

ds = pd.DataFrame(iris.data, columns = iris.feature_names)
ds = ds.drop(columns = ["sepal length (cm)","sepal width (cm)"])

# performing features scaling
sc = StandardScaler()
ds = sc.fit_transform(ds)
ds = pd.DataFrame(ds, columns = ["pl","pw"])
# now elbow method
wcss = []
for i in range(1,11):
    k = KMeans(n_clusters = i, init = "k-means++")
    k.fit(ds)
    wcss.append(k.inertia_)
plt.plot(range(1,11), wcss)   # 3 clusters are optimum

# making cluster model
km = KMeans(n_clusters = 3, init = "k-means++")
y_means = km.fit_predict(ds)
ds["cluster"] = y_means

ds0 = ds[ds.cluster == 0]
ds1 = ds[ds.cluster == 1]
ds2 = ds[ds.cluster == 2]

# visualization of clusters
plt.scatter(ds0["pl"], ds0["pw"], color = "red", s=100, label = "c1" )
plt.scatter(ds1["pl"], ds1["pw"], color = "green", s=100, label = "c2" )
plt.scatter(ds2["pl"], ds2["pw"], color = "blue", s=100, label = "c3" )
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], color = "yellow", s = 400, label = "centers")
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.legend()
plt.show()



