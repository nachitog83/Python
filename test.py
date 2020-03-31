import numpy as np
from matplotlib import pyplot as plt

N = 10000
coor = np.random.rand(N,2)
print(coor.shape)
x = coor[:,0] - 0.5
y = coor[:,1] - 0.5

adentro = np.add(x**2 , y**2) < 0.25

for i in range(N):
	if adentro[i] == True:
		plt.scatter(x[i], y[i], s=5, c='green')
	else:
  		plt.scatter(x[i], y[i], s=5, c='red')

#print(adentro)
print(4*adentro.sum()/N)

circle= plt.Circle((0,0), radius= 0.5, fill=False)
ax=plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.show()