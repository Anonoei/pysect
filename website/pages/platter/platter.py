import pathlib
from nicegui import ui

from website.header import init as header_init

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import pyvista


def render():
    ui.context.client.content.classes("p-0 gap-0")
    header_init()
    with ui.header(wrap=True):
        ui.label("This is the header")

    with ui.left_drawer():
        ui.label("left drawer")
        with ui.column():
            ui.label("col1")

        with ui.column():
            ui.label("col2")

        with ui.column():
            ui.label("col3")

    with ui.right_drawer():
        ui.label("right drawer")

    with ui.footer():
        ui.label("This is the footer")

    with ui.matplotlib().figure as fig:
        mesh = pyvista.read(
            pathlib.Path(__file__).parent.parent.parent.parent
            / "files"
            / "PiPED 40x100mm.stl"
        )
        # mesh.plot()
