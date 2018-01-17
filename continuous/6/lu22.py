# lu of 2,2 array

import numpy as np
a = np.array([[1,4],[2,3]])
l = np.zeros((2,2))
u = np.zeros((2,2))

# l[i,i] = 1
l[0,0] = 1
l[1,1] = 1

u[0,0] = a[0,0]
u[0,1] = a[0,1]
l[1,0] = a[1,0]/u[0,0]
u[1,1] = (a[1,1]-l[1,0]*u[0,1])/l[1,1]

print l
print u


