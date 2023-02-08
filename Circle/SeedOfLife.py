from matplotlib.pyplot import *
from Circle import Circles
import math

c0 = Circles(0,0,1,100)
c1 = Circles(0,1,1,100)
c2 = Circles(0,-1,1,100)
c3 = Circles(math.sqrt(3)/2, 1/2,1,100)
c4 = Circles(-math.sqrt(3)/2, 1/2,1,100)
c5 = Circles(math.sqrt(3)/2, -1/2,1,100)
c6 = Circles(-math.sqrt(3)/2, -1/2,1,100)


plot(c0[0],c0[1])
plot(c1[0],c1[1])
plot(c2[0],c2[1])
plot(c3[0],c3[1])
plot(c4[0],c3[1])
plot(c5[0],c5[1])
plot(c6[0],c6[1])

show()