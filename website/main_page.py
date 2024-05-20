from nicegui import ui
from .header import add_head_html, add_header

import website.style as style


def create():
    ui.context.client.content.classes("p-0 gap-0")
    add_head_html()
    add_header()
    with ui.row().classes(
        "w-full h-screen items-center gap-8 pr-4 no-wrap into-section"
    ):
        with ui.column().classes("gap-4 md:gap-8 pt-32"):
            style.title("Meet *PySect*.")
            style.subtitle("And let your browser slice your STLs")
            ui.link(target="#about").classes("scroll-indicator")
