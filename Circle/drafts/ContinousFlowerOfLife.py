import math

n_points = 6

r = 1

p_x = []
p_y = []

one_step = 2*math.pi/n_points

for i in range(n_points):
    x = math.cos(i*one_step)*r
    y = math.sin(i*one_step)*r

    p_x.append(x)
    p_y.append(y)

print('sqrt(3)/2 = ' + str(math.sqrt(3)/2))
print('sqrt(3) = ' + str(math.sqrt(3)))
print('x,y,'+str(n_points) + ' points')
for i in range(n_points):
    print(str(p_x[i])+','+str(p_y[i]))

def GetNPointsFromCircle(n, r, x0, y0):
    p_x = []
    p_y = []

    one_step = 2*math.pi/n

    for i in range(n):
        x = math.cos(i*one_step)*r + x0
        y = math.sin(i*one_step)*r + y0

        p_x.append(x)
        p_y.append(y)
    
    return [p_x, p_y]

from matplotlib.pyplot import *
from Circles import Circle

def PlotCircleFromPoint(x0, y0, r=1, n=100):
    x, y = Circle(x0, y0, r, n)
    plot(x, y)

n = 6
x, y = GetNPointsFromCircle(n, 1, 0, 0)

for i in range(n):
    PlotCircleFromPoint(x[i],y[i])

n = 12
x, y = GetNPointsFromCircle(n,2,0,0)

for i in range(n):
    PlotCircleFromPoint(x[i],y[i])

n = 18
x, y = GetNPointsFromCircle(n,3,0,0)

for i in range(n):
    PlotCircleFromPoint(x[i],y[i])

show()