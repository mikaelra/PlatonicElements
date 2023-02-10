import math
import Circles

from matplotlib.pyplot import *

def makePointsFromCore6(n, r=1, x0=0, y0=0):
    x1, y1 = Circles.GetNPointsFromCircle(n=6, r=r*n, x0=x0, y0=y0)
    x = []
    y = []

    xncore = []
    yncore = []
    for i in range(6):
        xncore.append(x1[i])
        yncore.append(y1[i])

    for i in range(6):
        x.append(xncore[i-2])
        y.append(yncore[i-2])
        for j in range(1,n):
            x.append(xncore[i-2] + j/n*(xncore[i-1]-xncore[i-2]))
            y.append(yncore[i-2] + j/n*(yncore[i-1]-yncore[i-2]))
    
    return [x, y]

def CreateFlowerPointsOfLifeForNLayers(n, r=1, x0=0, y0=0):
    # n must be greater or equal 2
    x = [x0]
    y = [y0]
    
    x1, y1 = Circles.GetNPointsFromCircle(x0=x0, y0=y0, r=r, n=6)
    x += x1
    y += y1

    for i in range(2,n+1):
        xi, yi = makePointsFromCore6(i, r=r, x0=x0, y0=y0)
        x+=xi
        y+=yi
    
    return [x, y]

def plotCircleForEachPoint(x, y, r=1, n=100):
    for i in range(len(x)):
        cxi, cyi = Circles.Circle(x0=x[i],y0=y[i],r=r,n=n)
        plot(cxi, cyi, color='black')

def plotFlowerOfLifeForNLayers(n=6, x0=0, y0=0, r=1,np=100):
    x, y = CreateFlowerPointsOfLifeForNLayers(n, r, x0=x0, y0=y0)
    plotCircleForEachPoint(x, y, r=r, n=np)

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

plotFlowerOfLifeForNLayers(n=2,x0=0,y0=0, r=2)
plotFlowerOfLifeForNLayers(n=2,x0=0,y0=0, r=1)
plotFlowerOfLifeForNLayers(n=2,x0=0,y0=0, r=0.5)
show()

