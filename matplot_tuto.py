import matplotlib.pyplot as plt
circle= plt.Circle((0,0), radius= 0.5, fill=False)
ax=plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.show()