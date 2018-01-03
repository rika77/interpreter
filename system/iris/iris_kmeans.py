#no change..

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D	# for 3D plot
from sklearn.datasets import load_iris

from sklearn import datasets
iris = load_iris()
data = iris.data
target = iris.target

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_x = pca.fit(data).transform(data)
from sklearn.cluster import KMeans
def t(n):
	km=KMeans(n_clusters=3,max_iter=n)
	cluster = km.fit_predict(pca_x)
	plt.scatter(pca_x[:,0],pca_x[:,1],c=cluster)
	plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],marker='X',c='blue')
	plt.show()

t(1)
