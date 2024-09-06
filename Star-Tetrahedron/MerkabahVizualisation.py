import math
from matplotlib.pyplot import *

def createOuterPointsToTetrahedron(x0=0,y0=0,r=1,deg=math.pi/2):
    x = [x0]
    y = [y0]

    one_step = 2*math.pi/3

    for i in range(3):
        tempx = math.cos(i*one_step+deg)*r + x0
        tempy = math.sin(i*one_step+deg)*r + y0

        x.append(tempx)
        y.append(tempy)
    
    return [x, y]

def createStarTetrahedron(x0=0,y0=0,r=1,deg=math.pi/2):
    x = []
    y = []

    one_step = 2*math.pi/3

    for i in range(3):
        x.append(x0)
        y.append(y0)
        tempx = math.cos(i*one_step+deg)*r + x0
        tempy = math.sin(i*one_step+deg)*r + y0

        x.append(tempx)
        y.append(tempy)
    for i in range(3):
        tempx = math.cos(i*one_step+deg)*r + x0
        tempy = math.sin(i*one_step+deg)*r + y0

        x.append(tempx)
        y.append(tempy)
    
    for i in range(3):
        x.append(x0)
        y.append(y0)
        tempx = math.cos(i*one_step+deg+math.pi)*r + x0
        tempy = math.sin(i*one_step+deg+math.pi)*r + y0

        x.append(tempx)
        y.append(tempy)
    for i in range(3):
        tempx = math.cos(i*one_step+deg+math.pi)*r + x0
        tempy = math.sin(i*one_step+deg+math.pi)*r + y0

        x.append(tempx)
        y.append(tempy)
    
    return [x, y]

# x, y = createOuterPointsToTetrahedron()
# plot(x,y,marker='o')
# x, y = createOuterPointsToTetrahedron(deg=3*math.pi/2)
# plot(x,y,marker='o')
# show()

# x, y = createStarTetrahedron(deg=3*math.pi/2)
# plot(x,y,marker='o')
# show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    x, y = createStarTetrahedron(x0 = 2 - 0.025*i, y0 = 0)
    x0, y0 = createStarTetrahedron(x0 = 0, y0 = 0)
    x2, y2 = createStarTetrahedron(x0 = -2 + 0.025*i, y0 = 0)
    x += x0
    y += y0
    x += x2
    y += y2
    line.set_ydata(y)  # update the data.
    line.set_xdata(x)
    return line,

if __name__ == "__main__":

    fig, ax = plt.subplots()
    ax.set_xlim([-4,4])
    ax.set_ylim([-4,4])

    x, y = createStarTetrahedron()
    x2, y2 = createStarTetrahedron()
    x += x2
    y += y2

    line, = ax.plot(x, y)
    
    ani = animation.FuncAnimation(
        fig, animate, interval=20, blit=True, save_count=50)

    # To save the animation, use e.g.
    #
    # ani.save("movie.mp4")
    #
    # or
    #
    # writer = animation.FFMpegWriter(
    #     fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # ani.save("movie.mp4", writer=writer)

    # MIKAELS NOTES:
    # DIS MOVIE STUFF ABOVE DON'T WORK
    plt.show()

    # Create one merkaba seen from above
    # x, y = createStarTetrahedron()
    # plt.plot(x, y)
    # plt.show()

    # # Create 72 merkabas between 0 and 60 degrees (aka pi/3)

    # m = 12
    # for i in range(m):
    #     x, y = createStarTetrahedron(deg=math.pi / 2 + i*math.pi/(3*m))
    #     plt.plot(x, y)

    # plt.show()

    # # Create seventy-two merkabas between 0 and 60 degrees (aka pi/3)

    # m = 72
    # for i in range(m):
    #     x, y = createStarTetrahedron(deg=math.pi / 2 + i*math.pi/(3*m))
    #     plt.plot(x, y)

    # plt.show()

