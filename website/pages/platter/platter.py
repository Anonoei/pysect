from nicegui import ui

from website.header import init as header_init


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
