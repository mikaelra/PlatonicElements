import math
import matplotlib.pyplot as plt

point1 = (0,0,0)
point2 = (1,0,0)
point3 = (0.5,math.sqrt(3)/2,0)
point4 = (0.5,math.sqrt(3)/6,0)
point5 = (0.5,math.sqrt(3)/6,math.sqrt(3)/2)
#point6 = (0.5,math.sqrt(3)/6,0.5)

## Create 3d lines: ##

# Outer lines
# 1-2
# 1-3
# 2-3
# 1-5
# 2-5
# 3-5


# Inner lines
# 1-6
# 2-6
# 3-6
# 5-6

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(point1[0], point1[1], point1[2])
ax.scatter(point2[0], point2[1], point2[2])
ax.scatter(point3[0], point3[1], point3[2])
ax.scatter(point4[0], point4[1], point4[2])
ax.scatter(point5[0], point5[1], point5[2])
#ax.scatter(point6[0], point6[1], point6[2])

plt.show()