import random,math
from matplotlib import pyplot as plt

totalThrows=900
throwsInsideCircle = 0 
for throw in range(totalThrows): 
  x = random.random()-0.5
  print(x) 
  y = random.random()-0.5
  print(y)
  
  if(x*x + y*y < 0.25): 
    throwsInsideCircle += 1
    plt.scatter(x, y, s=2, c='green')
  else :
  	plt.scatter(x, y, s=2, c='red')

pi = (4.0*throwsInsideCircle)/totalThrows
print(totalThrows)
print(pi) 
circle= plt.Circle((0,0), radius= 0.5, fill=False)
ax=plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.show()