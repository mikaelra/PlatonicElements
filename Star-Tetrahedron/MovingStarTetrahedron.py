import math
from matplotlib.pyplot import *
from StarTetrahedron import createStarTetrahedron
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])

x, y = createStarTetrahedron()
line, = ax.plot(x, y)

def animate(i):
    x0, y0 = createStarTetrahedron()
    x, y = createStarTetrahedron(deg=i)
    x2, y2 = createStarTetrahedron(deg=3*math.pi / 2 - i)
    x += x2
    y += y2
    x += x0
    y += y0
    line.set_ydata(y)  # update the data.
    line.set_xdata(x)
    return line,

if __name__ == "__main__":

    ani = animation.FuncAnimation(
        fig, animate, interval=20, blit=True, save_count=50)
    
    plt.show()

    # NEXT STEP: Create animation with 12-merkabas