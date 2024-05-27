import pathlib
from nicegui import ui, events

from website.header import init as header_init

from pysect.config.config import Config, Printer, Filament, Slice
import json

config = Config()
config.add_printer(Printer())
config.add_filament(Filament())
config.add_slice(Slice())
loaded_files = []
uploaded_files = []
scene = None
file_list = None

print(json.dumps(config.json(), indent=4))


def handle_upload(e: events.UploadEventArguments):
    uploaded_files.append(str(pathlib.Path("files") / e.name))
    update_scene()


def update_scene():
    global scene
    for idx, fname in enumerate(uploaded_files):
        try:
            loaded_files[idx]
        except IndexError:
            scene.stl(fname)
            loaded_files.append(True)


def _select_printer(e):
    config.selected["printer"] = e.value


def _select_filament(e):
    config.selected["filament"] = e.value


def _select_slice(e):
    config.selected["slice"] = e.value


def render():
    global file_list
    global scene
    ui.context.client.content.classes("p-0 gap-0")
    header_init()

    with ui.left_drawer():
        ui.label("left drawer")
        with ui.column():
            ui.label("col1")

        with ui.column():
            ui.label("col2")

        with ui.column():
            ui.label("col3")

    with ui.right_drawer():
        ui.upload(on_upload=handle_upload).props("accept=.stl").classes("max-w-full")
        ui.separator()
        _printers = list(config.printers.keys())
        select_printer = ui.select(
            _printers, value=_printers[0], label="Printer", on_change=_select_printer
        )
        _filaments = list(config.filaments.keys())
        select_filament = ui.select(
            _filaments,
            value=_filaments[0],
            label="Filament",
            on_change=_select_filament,
        )
        _slices = list(config.slices.keys())
        select_slice = ui.select(
            _slices, value=_slices[0], label="Slice", on_change=_select_slice
        )

    ui.query(".nicegui-content").classes("h-screen no-wrap")

    scene = ui.scene(grid=False, background_color="#111111").classes("w-full h-full")
    scene.move_camera(
        x=config.printer().bed.x * 0.75,
        y=config.printer().bed.y * 0.75,
        z=config.printer().bed.z // 3,
        look_at_x=0,
        look_at_y=0,
        duration=1.0,
    )
    init_bed()


def init_bed():
    global scene
    scene.box(config.printer().bed.x, config.printer().bed.x, 2)
    for val in scene.objects.values():  # Set the build plate color darker
        val.color = "#444444"
