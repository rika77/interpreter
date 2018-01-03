import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target

pca = decomposition.PCA(n_components = 2, whiten = "False", copy = "True")
pca.fit(X)
X_pca= pca.transform(X)
import pylab as pl
pl.scatter(X_pca[:,0],X_pca[:,1],c=Y)
plt.show()
