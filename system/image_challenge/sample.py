# 2 -> 1 succeeded!

import numpy as np
import matplotlib.pyplot as plt

Cov = np.array([[2.9,-2.2],[-2.2,6.5]])
X = np.random.multivariate_normal([1,2], Cov, size=200) #200 samples

# np.set_printoptions(4,suppress=True)
# print X[:10,:]

plt.figure(figsize=(12,4))
# plt.scatter(X[:,0],X[:,1])
# plt.axis('equal')	#x-axis,y-axis same scale

from sklearn.decomposition import PCA
pca = PCA()
X_pca = pca.fit_transform(X)
print pca.components_	#axis
print pca.mean_	#average
print pca.explained_variance_ratio_	#importanc

Y = np.dot((X - pca.mean_), pca.components_.T)

plt.subplot(1,3,1)	#1line, 2row, 1st
plt.scatter(X[:,0],X[:,1])
plt.axis('equal')

zero = np.array([[0] for i in range(200)])
plt.subplot(1,3,2)
plt.scatter(Y[:,0], Y[:,1])
plt.axis('equal')

plt.subplot(1,3,3)
plt.scatter(Y[:,0], zero)
plt.axis('equal')

plt.show()
