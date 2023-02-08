import math
import Circles

x0, y0 = 0, 0

n = 2

x1, y1 = Circles.GetNPointsFromCircle(n=6, r=1, x0=x0, y0=y0)

x2core = []
y2core = []
for i in range(6):
    x2core_temp = x1[i]*2
    y2core_temp = y1[i]*2

    x2core.append(x2core_temp)
    y2core.append(y2core_temp)

x2between = []
y2between = []
for i in range(6):
    for j in range(n-1):
        xavg = (j+1)*(x2core[i-2] + x2core[i-1]) / n
        x2between_temp = (j+1)*(x2core[i-2] + x2core[i-1]) / n
        y2between_temp = (j+1)*(y2core[i-2] + y2core[i-1]) / n

        x2between.append(x2between_temp)
        y2between.append(y2between_temp)

n=3
x3core = []
y3core = []
for i in range(6):
    x3core_temp = x1[i]*n
    y3core_temp = y1[i]*n

    x3core.append(x3core_temp)
    y3core.append(y3core_temp)

x3between = []
y3between = []
for i in range(6):
    for j in range(1,n):
        x3between.append(x3core[i-2] + j/n*(x3core[i-1]-x3core[i-2]))
        y3between.append(y3core[i-2] + j/n*(y3core[i-1]-y3core[i-2]))

from matplotlib.pyplot import *

def makePointsFromCore6(n, r=1, x0=0, y0=0):
    # There are bugs here when r!= 0, x0!=0 and y0!=0
    x1, y1 = Circles.GetNPointsFromCircle(n=6, r=r*n, x0=x0, y0=y0)
    x = []
    y = []
    print('x1,y1')
    for i in range(6):
        print(str(x1[i]) + ',' + str(y1[i]))

    xncore = []
    yncore = []
    for i in range(6):
        xncore.append(x1[i])
        yncore.append(y1[i])

    print('xcore,ycore')
    for i in range(6):
        print(str(xncore[i]) + ',' + str(yncore[i]))

    for i in range(6):
        x.append(xncore[i-2])
        y.append(yncore[i-2])
        for j in range(1,n):
            x.append(xncore[i-2] + j/n*(xncore[i-1]-xncore[i-2]))
            y.append(yncore[i-2] + j/n*(yncore[i-1]-yncore[i-2]))

    print('y - line 73')
    print(y)
    
    return [x, y]

def CreateFlowerPointsOfLifeForNLayers(n, r=1, x0=0, y0=0):
    # n must be greater or equal 2
    x = [x0]
    y = [y0]
    
    x1, y1 = Circles.GetNPointsFromCircle(x0=x0, y0=y0, r=1, n=6)
    x += x1
    y += y1

    print('x')
    print(x)
    print('y')
    print(y)

    for i in range(2,n+1):
        xi, yi = makePointsFromCore6(i, r=r, x0=x0, y0=y0)
        x+=xi
        y+=yi

    print('x')
    print('y')
    
    return [x, y]

def plotCircleForEachPoint(x, y, r=1, n=100):
    for i in range(len(x)):
        cxi, cyi = Circles.Circle(x0=x[i],y0=y[i],r=r,n=n)
        plot(cxi, cyi, color='black')

def plotFlowerOfLifeForNLayers(n=6, x0=0, y0=0, r=1,np=100):
    x, y = CreateFlowerPointsOfLifeForNLayers(n, r, x0=x0, y0=y0)
    plotCircleForEachPoint(x, y, r=r, n=np)


# plot(x1, y1, marker="o")
# plot(x2core, y2core, marker="o")
# plot(x2between, y2between, marker="o")
# plot(x3core, y3core, marker="o")
# plot(x3between, y3between, marker='o')
#show()

# x, y = Circles.GetNPointsFromCircle(x0=5, y0=5, r=3, n=6)
# plot(x, y)
# show()

# x, y = makePointsFromCore6(1, 1,10,10)
# plot(x,y)
# x, y = makePointsFromCore6(3, 1, 0, 0)
# plot(x,y)
# show()

# x, y = CreateFlowerPointsOfLifeForNLayers(n=3,r=1,x0=10,y0=5)
# print(y)
# plot(x, y)
# show()

# plotCircleForEachPoint(x, y)
# show()

# plotFlowerOfLifeForNLayers(6, 0, 1)
# show()

plotFlowerOfLifeForNLayers(n=2,x0=0,y0=3, r=2)
# show()
show()

