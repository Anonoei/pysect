class coord:

    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{type(self).__name__} ({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"<{str(self)}>"
