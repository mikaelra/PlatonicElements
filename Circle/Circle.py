import math
from matplotlib.pyplot import *


def Circle(x0, y0, r, n):
    x = []
    y = []

    for i in range(n+1):
        tempx = math.sin(i/n * 2*math.pi)*r + x0
        tempy = math.cos(i/n * 2*math.pi)*r + y0
        
        x.append(tempx)
        y.append(tempy)
    
    
    return [x, y]

c0 = Circle(0,0,1,100)
c1 = Circle(0,1,1,100)
c2 = Circle(0,-1,1,100)
c3 = Circle(math.sqrt(3)/2, 1/2,1,100)
c4 = Circle(-math.sqrt(3)/2, 1/2,1,100)
c5 = Circle(math.sqrt(3)/2, -1/2,1,100)
c6 = Circle(-math.sqrt(3)/2, -1/2,1,100)


plot(c0[0],c0[1])
plot(c1[0],c1[1])
plot(c2[0],c2[1])
plot(c3[0],c3[1])
plot(c4[0],c3[1])
plot(c5[0],c5[1])
plot(c6[0],c6[1])

show()