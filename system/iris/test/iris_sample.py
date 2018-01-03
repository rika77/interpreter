
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
targets = iris.target


pca = PCA(n_components = 2)
pca.fit(X)
transformed = pca.fit_transform(X)

for label in np.unique(targets):
        plt.scatter(transformed[targets == label, 0],
                    transformed[targets == label, 1])
# plt.scatter(pca_x[:,0],pca_x[:,1])
plt.show()
