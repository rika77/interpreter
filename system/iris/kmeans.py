import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
#random_state -> seed fix

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(131)
data,cluster=make_blobs(n_samples=1000,centers=3,cluster_std=3.0,random_state=4)
ax.scatter(data[:,0],data[:,1],c=cluster)
ax.set_title("basic")

from sklearn.cluster import KMeans

ay = fig.add_subplot(132)
km=KMeans(n_clusters=3,max_iter=1)
cluster = km.fit_predict(data)
ay.scatter(data[:,0],data[:,1],c=cluster)
ay.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],marker='X')
ay.axis('equal')
ay.set_title("kmeans-1")

az = fig.add_subplot(133)
km=KMeans(n_clusters=3,max_iter=10)
cluster = km.fit_predict(data)
az.scatter(data[:,0],data[:,1],c=cluster)
az.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],marker='X')
az.axis('equal')
az.set_title("kmeans-10")

plt.show()
