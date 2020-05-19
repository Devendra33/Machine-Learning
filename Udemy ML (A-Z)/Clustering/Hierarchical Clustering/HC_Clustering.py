# Hierarchical clustering:
# 2 approches, 1. algglomerative HC( bottom - up approch):
# in this approach every single point is treated as a different cluster and two closest clusters combine until
# they become a single cluster., the process memory is stored in dendrogram

# PROS: The optimal number of clusters can be
# obtained by the model itself, practical
# visualisation with the dendrogram

# CONS: Not appropriate for large datasets

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Importing the dataset
ds = pd.read_csv("Mall_Customers.csv")
x = ds.iloc[:,[-2,-1]].values

# creating the dendrogram
import scipy.cluster.hierarchy as sch
dg = sch.dendrogram(sch.linkage(x, method = "ward")) # ward means minimum variance method
plt.title("Dendrogram")
plt.xlabel("customers")
plt.ylabel("Euclidain Distance")
plt.show() 

# Now visualizing the clustering
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = "euclidean", linkage = "ward")
y_hc = hc.fit_predict(x)

plt.scatter(x[y_hc == 0, 0], x[y_hc == 0, 1], s = 100, c = "blue", label = "C1")
plt.scatter(x[y_hc == 1, 0], x[y_hc == 1, 1], s = 100, c = "green", label ="C2")
plt.scatter(x[y_hc == 2, 0], x[y_hc == 2, 1], s = 100, c = "red", label = "C3")
plt.scatter(x[y_hc == 3, 0], x[y_hc == 3, 1], s = 100, c = "cyan", label = "c4")
plt.scatter(x[y_hc == 4, 0], x[y_hc == 4, 1], s = 100, c = "magenta", label = "C5")
plt.title("Clustering")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.show()