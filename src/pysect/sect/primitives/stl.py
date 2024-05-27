import numpy as np

from .mesh import Mesh


class STL:
    def __init__(self, data):
        self.data = data

    def to_mesh(self):
        return Mesh(self.vectors, self.points)

    @property
    def normals(self):
        return self.data["normals"]

    @property
    def vectors(self) -> np.ndarray:
        return self.data["vectors"]

    @property
    def points(self):
        return self.vectors.reshape(self.data.size, 9)

    @classmethod
    def dtype(cls):
        dtype = np.dtype(
            [
                ("normals", np.float32, (3,)),
                ("vectors", np.float32, (3, 3)),
                ("attr", np.uint16, (1,)),
            ]
        )
        dtype = dtype.newbyteorder("<")
        return dtype
