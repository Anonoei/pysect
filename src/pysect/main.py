import pyvista

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from pyboiler.config import config

import pysect.sect.serial.stl as stl
import pysect.sect.slice


Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing


def main():

    # filepath = askopenfilename()
    # filepath = config().PATH_ROOT / "files" / "20mm_cube.stl"
    filepath = config().PATH_ROOT / "files" / "PiPED 40x100mm.stl"
    if not filepath:
        exit()
    mesh = pyvista.read(filepath)
    mesh.plot()
    # obj = stl.loadf(filepath).to_mesh()
    # slice.generate_layers(mesh=obj)
    # obj.plot()


if __name__ == "__main__":
    main()
