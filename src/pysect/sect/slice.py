import numpy as np

from .config import config as dflt_conf
from .primitives.mesh import Mesh


def generate_layers(mesh: Mesh, config=dflt_conf):
    layer_heights = [mesh.bottom()]
    top = mesh.top()
    while layer_heights[-1] < top:
        layer_heights.append(layer_heights[-1] + config.LAYER_HEIGHT)
    print(f"Found {len(layer_heights)} layers!")

    for height in layer_heights:
        polys = mesh.Z2D(height)
        yield (height, polys)
    yield
