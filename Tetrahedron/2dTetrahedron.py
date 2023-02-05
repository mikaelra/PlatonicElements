from matplotlib.pyplot import *
import math as m
import numpy as np

# steps when making ranges
steps = 100

# if length of one line in triangle is one, then the height is the sqrt of 0.75, by pythagoras theorem
top = m.sqrt(0.75)

# define all points
leftCorner = (0,0)
rightCorner = (1,0)
topPoint = (0.5, top)
middlePoint = (0.5, m.sqrt(3)/6)

# Outer lines

c = np.linspace(leftCorner[0], rightCorner[0], steps)
c2 = np.linspace(leftCorner[1], rightCorner[1], steps)

b = np.linspace(leftCorner[0], topPoint[0], steps)
b2 = np.linspace(leftCorner[1], topPoint[1], steps)

a = np.linspace(rightCorner[0], topPoint[0], steps)
a2 = np.linspace(rightCorner[1], topPoint[1], steps)

# Inside lines

d = np.linspace(leftCorner[0], middlePoint[0], steps)
d2 = np.linspace(leftCorner[1], middlePoint[1], steps)

e = np.linspace(rightCorner[0], middlePoint[0], steps)
e2 = np.linspace(rightCorner[1], middlePoint[1], steps)

f = np.linspace(topPoint[0], middlePoint[0], steps)
f2 = np.linspace(topPoint[1], middlePoint[1], steps)

plot(c, c2, 'r')
plot(b, b2, 'r')
plot(a, a2, 'r')

plot(d, d2, 'r')
plot(e, e2, 'r')
plot(f, f2, 'r')

show()
