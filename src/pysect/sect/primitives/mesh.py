from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


class Mesh:

    def __init__(self, vectors: np.ndarray, points: np.ndarray):
        self.vectors = vectors
        self.points = points
        self.align()

    def align(self):
        bottom = self.bottom()
        self.translate(0, 0, -bottom)

    def Z2D(self, z: float):
        polys = []
        for triangle in self.vectors:
            tri_min_z = min((triangle[0][2], triangle[1][2], triangle[2][2]))
            tri_max_z = max((triangle[0][2], triangle[1][2], triangle[2][2]))

            if tri_min_z < z and tri_max_z > z:
                continue

            pos_x = (triangle[0][0], triangle[1][0], triangle[2][0])
            pos_y = (triangle[0][1], triangle[1][1], triangle[2][1])

            pts = np.array(
                [[pos_x[0], pos_y[0]], [pos_x[1], pos_y[1]], [pos_x[2], pos_y[2]]]
            )
            polys.append(Polygon(pts, closed=False))

        return polys

    def top(self):
        return max(pos[2] for vector in self.vectors for pos in vector)

    def bottom(self):
        return min(pos[2] for vector in self.vectors for pos in vector)

    def left(self):
        return min(pos[0] for vector in self.vectors for pos in vector)

    def right(self):
        return max(pos[0] for vector in self.vectors for pos in vector)

    def front(self):
        return max(pos[1] for vector in self.vectors for pos in vector)

    def back(self):
        return min(pos[1] for vector in self.vectors for pos in vector)

    def width(self):
        return self.right() - self.left()

    def depth(self):
        return self.front() - self.back()

    def height(self):
        return self.top() - self.bottom()

    def translate(self, x, y, z):
        x = np.float32(x)
        y = np.float32(y)
        z = np.float32(z)
        print(f"Translating {x}, {y}, {z}")

        for idx in range(self.vectors.shape[0]):
            for i in range(self.vectors.shape[1]):
                self.vectors[idx, i, 0] += x
                self.vectors[idx, i, 1] += y
                self.vectors[idx, i, 2] += z

    def plot(self):
        plt.figure()
        ax = plt.axes(projection="3d")

        ax.add_collection3d(
            mplot3d.axes3d.art3d.Poly3DCollection(
                self.vectors,
                shade=True,
                facecolors="#AAAAAA",
                edgecolors="#222222",
            )
        )

        # Auto scale to the mesh size
        scale = self.points.flatten()
        ax.auto_scale_xyz(scale, scale, scale)

        plt.show()
