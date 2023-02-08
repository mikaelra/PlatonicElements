import math
import Circles
from matplotlib.pyplot import *

x0, y0 = 0, 0

x1, y1 = Circles.GetNPointsFromCircle(6, r=1, x0=x0, y0=y0)
#x1,x1
#-------
#1,0
#0.5, 0.86
#-0.5, 0.86
#-1, 0
#-0.5, -0.86
#0.5, -0.86

#x2,y2
#-------
#0, 2
#0.86, 1.5
#1.72, 1
#1.72, 0
#1.72, -1
#0.86, -1.5
#0, -2
#-0.86, -1.5
#-1.72, -1
#-1.72, 0
#-1.72, 1
#-0.86, 1.5
print('x,y')
for i in range(6):
    print(str(x1[i])+','+str(y1[i]))

x2=[]
y2=[]

for i in range(6):
    x_new = x1[i-2] + x1[i-1]
    y_new = y1[i-2] + y1[i-1]

    x2.append(x_new)
    y2.append(y_new)

    x_new = x1[i]*2
    y_new = y1[i]*2

    x2.append(x_new)
    y2.append(y_new)

# for i in range(6):
#     x_new = x1[i]*2
#     y_new = y1[i]*2

#     x2.append(x_new)
#     y2.append(y_new)

x3 = []
y3 = []
for i in range(6):
    x_new = x2[i]*3/2
    y_new = y2[i]*3/2

    x3.append(x_new)
    y3.append(y_new)

for i in range(12):
    x_new = x2[i-2] + x2[i-1]
    y_new = y2[i-2] + y2[i-1]

    x3.append(x_new)
    y3.append(y_new)
    


print('x2,y2')
for i in range(len(x2)):
    print(str(x2[i])+','+str(y2[i]))

def PlotCirclesOfListOfPoints(x, y, r=1, n=100):
    for i in range(len(x)):
        c = Circles.Circle(x[i],y[i],1,100)
        plot(c[0], c[1])

#PlotCirclesOfListOfPoints(x1,y1)
#PlotCirclesOfListOfPoints(x2,y2)
PlotCirclesOfListOfPoints(x3,y3)
show()
