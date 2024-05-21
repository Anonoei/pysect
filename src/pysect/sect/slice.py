import numpy as np

from .config import config as dflt_conf
from .primitives.mesh import Mesh


class slice:
    @staticmethod
    def generate_layers(mesh: Mesh, config=dflt_conf):
        layer_heights = [(0.0, config.LAYER_HEIGHT)]
        top = mesh.top()
        while layer_heights[-1][1] < top:
            height = layer_heights[-1][1]
            layer_heights.append((height, height + config.LAYER_HEIGHT))
        print(f"Found {len(layer_heights)} layers!")
