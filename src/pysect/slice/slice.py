import pyboiler.generic as generic


class VerticalShells(generic.slot_storage):
    __slots__ = ("perimeters", "other")

    def __init__(self, perimeters: int):
        self.perimeters = perimeters
        self.other = None


class HorizontalShells(generic.slot_storage):
    __slots__ = ("bottom", "top")

    def __init__(self, bottom: int, top: int):
        self.bottom = bottom
        self.top = top


class Slice(generic.slot_storage):
    __slots__ = ("name", "verti", "horiz")

    def __init__(self):
        self.name = "Slice"
        self.verti = VerticalShells(3)
        self.horiz = HorizontalShells(6, 5)
