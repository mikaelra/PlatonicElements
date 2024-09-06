import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# Define the vertices for a regular tetrahedron
regular_tetra_vertices = [
    [0, 0, 0],                     # Vertex 1
    [1, 0, 0],                     # Vertex 2
    [0.5, np.sqrt(3)/2, 0],        # Vertex 3
    [0.5, np.sqrt(3)/6, np.sqrt(2/3)]  # Vertex 4
]

# Calculate the centroid of the first tetrahedron
centroid = np.mean(regular_tetra_vertices, axis=0)

# Reflect each vertex across the centroid to get the vertices of the opposite tetrahedron
opposite_tetra_vertices = [
    2 * centroid - np.array(vertex) for vertex in regular_tetra_vertices
]

# Define the faces for both tetrahedrons
regular_tetra_faces = [
    [regular_tetra_vertices[0], regular_tetra_vertices[1], regular_tetra_vertices[2]],  # Face 1
    [regular_tetra_vertices[0], regular_tetra_vertices[1], regular_tetra_vertices[3]],  # Face 2
    [regular_tetra_vertices[0], regular_tetra_vertices[2], regular_tetra_vertices[3]],  # Face 3
    [regular_tetra_vertices[1], regular_tetra_vertices[2], regular_tetra_vertices[3]]   # Face 4
]

opposite_tetra_faces = [
    [opposite_tetra_vertices[0], opposite_tetra_vertices[1], opposite_tetra_vertices[2]],  # Face 1
    [opposite_tetra_vertices[0], opposite_tetra_vertices[1], opposite_tetra_vertices[3]],  # Face 2
    [opposite_tetra_vertices[0], opposite_tetra_vertices[2], opposite_tetra_vertices[3]],  # Face 3
    [opposite_tetra_vertices[1], opposite_tetra_vertices[2], opposite_tetra_vertices[3]]   # Face 4
]

# Create a new figure for the animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot for each frame
def update(frame):
    ax.clear()  # Clear previous frame

    # Plot the first tetrahedron with translucent faces
    ax.add_collection3d(Poly3DCollection(regular_tetra_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.3))

    # Plot the opposite tetrahedron with translucent faces
    ax.add_collection3d(Poly3DCollection(opposite_tetra_faces, facecolors='magenta', linewidths=1, edgecolors='b', alpha=.3))

    # Set the aspect ratio, labels, and dynamic view based on frame number
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Rotate the view around the z-axis
    angle = frame * 2  # Control the speed of rotation
    ax.view_init(elev=30, azim=angle)

# Create the animation
ani = FuncAnimation(fig, update, frames=180, interval=50)

plt.show()
