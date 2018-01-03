import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D	# for 3D plot
from sklearn.datasets import load_iris

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(121,projection = '3d')
from sklearn import datasets
iris = load_iris()
data = iris.data
target = iris.target
name = iris.target_names

ax.scatter(data[:,0],data[:,1],data[:,2], c=target)

ax.set_xlabel('sepal length(cm)')
ax.set_ylabel('sepal width(cm)')
ax.set_zlabel('petal length(cm)')

ay = fig.add_subplot(122)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)

pca_x = pca.fit(data).transform(data)


ay.scatter(pca_x[:,0],pca_x[:,1],c=target)

plt.show()


