import pyvista
import matplotlib.pyplot as plt

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from pyboiler.config import config

import pysect.sect.serial.stl as stl
import pysect.sect.slice as slice


Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing


def main():

    # filepath = askopenfilename()
    # filepath = config().PATH_ROOT / "files" / "20mm_cube.stl"
    filepath = config().PATH_ROOT / "files" / "PiPED 40x100mm.stl"
    if not filepath:
        exit()
    # mesh = pyvista.read(filepath)
    # mesh.plot()
    mesh = stl.loadf(filepath).to_mesh()

    ax = plt.gca()
    x_min, x_max = mesh.left() * 1.5, mesh.right() * 1.5
    y_min, y_max = mesh.back() * 1.5, mesh.front() * 1.5
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    for idx, (height, polys) in enumerate(slice.generate_layers(mesh)):
        for poly in polys:
            ax.add_patch(poly)
        plt.title(f"Layer {idx}: {height:.2f}")
        plt.show()
        plt.close()
    plt.show()
    # slice.generate_layers(mesh=obj)
    # obj.plot()


if __name__ == "__main__":
    main()
