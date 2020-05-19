# PROS: Simple to understand, easily adaptable,
# works well on small or large datasets,
# fast, efficient and performant

# CONS: Need to choose the number of clusters
 
# K-means Algorrithm
import pandas as pd
import matplotlib.pyplot as plt

# file imported
ds = pd.read_csv("Mall_Customers.csv")

# now select 2 good related fields for plotting at x and y axis.
x = ds.iloc[:,[-2,-1]].values

# in k-means we try to make depend variable and make clusters of levels of dependent variables
# now Elbow method.
from sklearn.cluster import KMeans
# we gonna make 10 clusters and select the best K values

wcss = []  # Within clusters sum of squares
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = "k-means++", random_state = 42)
    km.fit(x)    # fitting the data into cluster model
    wcss.append(km.inertia_)
plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method Graph")
plt.xlabel("Clusters")
plt.ylabel("WCSS")       # now k value should be 5 after looking the graph


# Now predicting the dependent variable
km = KMeans(n_clusters = 5, init = "k-means++", random_state = 42)
y_kmeans = km.fit_predict(x)    # fitting the data into cluster model

# visiualization of kmeans clustering
plt.scatter(x[y_kmeans == 0,0],x[y_kmeans == 0,1], s = 100, c = "blue", label = "C1" )
plt.scatter(x[y_kmeans == 1,0],x[y_kmeans == 1,1], s = 100, c = "green", label = "C2" )
plt.scatter(x[y_kmeans == 2,0],x[y_kmeans == 2,1], s = 100, c = "red", label = "C3" )
plt.scatter(x[y_kmeans == 3,0],x[y_kmeans == 3,1], s = 100, c = "cyan", label = "C4" )
plt.scatter(x[y_kmeans == 4,0],x[y_kmeans == 4,1], s = 100, c = "magenta", label = "C5" )
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], s = 400, c = "yellow", label = "centeriods")

plt.title("clusters of customers")
plt.xlabel("Annual Income")
plt.ylabel("Salary")
plt.legend()
plt.show()
