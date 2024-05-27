from dataclasses import dataclass
from enum import Enum, auto

import pyboiler.generic as generic


class Extruder(generic.slot_storage):
    __slots__ = ("nozzle", "layer_min", "layer_max")

    def __init__(self):
        self.nozzle = 0.4
        self.layer_min = 0.0375
        self.layer_max = 0.3


class Bed(generic.slot_storage):
    __slots__ = ("x", "y", "z", "shape")

    def __init__(self, x: int, y: int, z: int, shape=None):
        self.x = x
        self.y = y
        self.z = z
        self.shape = shape


class Limits(generic.slot_storage):
    __slots__ = ("x", "y", "z", "e", "unit")

    def __init__(self, x: int, y: int, z: int, e: int, unit: str):
        self.x = x
        self.y = y
        self.z = z
        self.e = e
        self.unit = unit


class Printer(generic.slot_storage):
    __slots__ = ("name", "bed", "veloc", "accel")

    def __init__(self):
        self.name = "Printer"
        self.bed = Bed(300, 300, 270)

        self.veloc = Limits(500, 500, 12, 120, "mm/s")
        self.accel = Limits(3000, 3000, 300, 3000, "mm/s^2")
