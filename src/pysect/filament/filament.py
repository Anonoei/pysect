import pyboiler.generic as generic


class Meta(generic.slot_storage):
    __slots__ = ("diameter", "multiplier")

    def __init__(self, diameter, multiplier):
        self.diameter = diameter
        self.multiplier = multiplier


class Filament(generic.slot_storage):
    __slots__ = ("name", "meta", "other")

    def __init__(self):
        self.name = "Filament"
        self.meta = Meta(1.75, 1.0)
        self.other = None
