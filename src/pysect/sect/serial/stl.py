import struct
from typing import IO
import numpy as np

from ..primitives.stl import STL as prim_STL

FIELD_BUFFER_SIZE = 4096
FIELD_HEADER_SIZE = 80
FIELD_COUNT_SIZE = 4


def detect(filepath):
    try:
        with open(filepath, "r") as f:
            line = f.readline()
        return "r"
    except UnicodeDecodeError:
        return "rb"


def loadf(filepath):
    mode = detect(filepath)
    with open(filepath, mode) as f:
        return load(f, mode)


def load(fh: IO, mode):
    if "b" in mode:
        return prim_STL(_load_binary(fh))
    else:
        return prim_STL(_load_ascii(fh))


def _load_binary(fh: IO):
    fh.read(FIELD_HEADER_SIZE)  # Skip the header
    count_data = fh.read(FIELD_COUNT_SIZE)
    if len(count_data) != FIELD_COUNT_SIZE:
        count = 0
    else:
        (count,) = struct.unpack("<i", count_data)
    print(f"Loading {count} triangles")
    dtype = np.dtype(
        [
            ("normals", np.float32, (3,)),
            ("vectors", np.float32, (3, 3)),
            ("attr", np.uint16, (1,)),
        ]
    )
    dtype = dtype.newbyteorder("<")
    return np.fromfile(fh, dtype=prim_STL.dtype(), count=count)


def _load_ascii(fh: IO):
    fh.readline()  # Skip the header

    def get_facet(fh: IO):
        normals = ()
        v1 = ()
        v2 = ()
        v3 = ()
        attr = 0

        line = fh.readline().strip()
        line = line.split(" ")
        if not line[0] == "facet":
            return None
        normals = (float(line[-3]), float(line[-2]), float(line[-1]))
        fh.readline()  # throw away outer loop line

        def get_vertices(line):
            line = line.split(" ")
            if not line[0] == "vertex":
                raise Exception("Failed to read vertex")
            return float(line[-3]), float(line[-2]), float(line[-1])

        v1 = get_vertices(fh.readline())
        v2 = get_vertices(fh.readline())
        v3 = get_vertices(fh.readline())
        fh.readline()
        fh.readline()
        return (normals, (v1, v2, v3), attr)

    def itter_facet(fh):
        while True:
            facet = get_facet(fh)
            if facet is None:
                break
            yield facet

    return np.fromiter(itter_facet(fh), dtype=prim_STL.dtype())
