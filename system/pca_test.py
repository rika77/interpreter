import numpy as np
import matplotlib.pyplot as plt

# average
ave_a = [1,3]  
cov = np.array([[3.0,-2.0],[-2.0,6.0]])
a = np.random.multivariate_normal(ave_a, cov, size=200) # 200samples

#y -> all 0
b = np.array([[0] for i in range(200)])
# np.set_printoptions(precision=3) # digit = 3
# print a[:10,:2]	#10rows 2colums
# print b[:10,:]
plt.figure (figsize=(4,4))
plt.scatter(a[:,0],b)
plt.axis('equal')
plt.show()

