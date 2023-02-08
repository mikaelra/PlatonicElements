from matplotlib.pyplot import *
from Circles import CircleWithLimits, Circle
import math

cOuter = Circle(0,0,3,1000)
cOuter2 = Circle(0,0,3.2,1000)

c0 = Circle(0,0,1,100)
c1 = Circle(0,1,1,100)
c2 = Circle(0,-1,1,100)
c3 = Circle(math.sqrt(3)/2, 1/2,1,100)
c4 = Circle(-math.sqrt(3)/2, 1/2,1,100)
c5 = Circle(math.sqrt(3)/2, -1/2,1,100)
c6 = Circle(-math.sqrt(3)/2, -1/2,1,100)

c7 = Circle(-math.sqrt(3)/2 , 1/2 + 1,1,100)
c8 = Circle(math.sqrt(3)/2 , 1/2 + 1,1,100)
c9 = Circle(0 , 2,1,100)

c10 = Circle(-math.sqrt(3)/2 , -1/2 - 1,1,100)
c11 = Circle(math.sqrt(3)/2 , -1/2 - 1,1,100)
c12 = Circle(0 , -2,1,100)

c13 = Circle(2*math.sqrt(3)/2 , -1,1,100)
c14 = Circle(2*math.sqrt(3)/2 , 1,1,100)
c15 = Circle(-2*math.sqrt(3)/2 , -1,1,100)
c16 = Circle(-2*math.sqrt(3)/2 , 1,1,100)

c17 = Circle(2*math.sqrt(3)/2 , 0,1,100)
c18 = Circle(-2*math.sqrt(3)/2 , 0,1,100)

#18 half circles is needed of some sort


plot(cOuter[0],cOuter[1])
plot(cOuter2[0],cOuter2[1])

plot(c0[0],c0[1])
plot(c1[0],c1[1])
plot(c2[0],c2[1])
plot(c3[0],c3[1])
plot(c4[0],c3[1])
plot(c5[0],c5[1])
plot(c6[0],c6[1])

plot(c7[0], c7[1])
plot(c8[0], c8[1])
plot(c9[0], c9[1])

plot(c10[0], c10[1])
plot(c11[0], c11[1])
plot(c12[0], c12[1])

plot(c13[0], c13[1])
plot(c14[0], c14[1])
plot(c15[0], c15[1])
plot(c16[0], c16[1])

plot(c17[0], c17[1])
plot(c18[0], c18[1])

# 18 half Circle needs to be plotted


show()