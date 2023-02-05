import math
from matplotlib.pyplot import *


def Circle(x0, y0, r, n):
    # x0 and y0 are center coordinates of circle
    # r is radius
    # n is the amount of points plotted
    x = []
    y = []

    for i in range(n+1):
        tempx = math.sin(i/n * 2*math.pi)*r + x0
        tempy = math.cos(i/n * 2*math.pi)*r + y0
        
        x.append(tempx)
        y.append(tempy)
    
    
    return [x, y]