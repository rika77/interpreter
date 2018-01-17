# lu of n,n array
n = 3
import numpy as np
a = np.array([[1,2,4],[2,3,5],[1,2,3]])
l = np.zeros((n,n))
u = np.zeros((n,n))

lu = np.zeros((2,2))

# l[i,i] = 1
for i in range(n):
	l[i,i] = 1

# def lu
u[0,0] = a[0,0]
for i in range(1,3):
	u[0,i] = a[0,i]
	l[i,0] = a[i,0]/u[0,0]
l_sub = l[1:3,0]
u_sub = u[0,1:3]
lu = np.dot(l_sub[:,np.newaxis], u_sub[np.newaxis,:])
a_sec = a[1:3,1:3] - lu

# sec
u[1,1] = a_sec[0,0]
u[1,2] = a_sec[0,1]
l[2,1] = a_sec[1,0]/u[1,1]
u[2,2] = a_sec[1,1] - l[2,1]*u[2,1]


print l
print u

print np.dot(l,u)
 
