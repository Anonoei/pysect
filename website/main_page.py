from nicegui import ui
from website.header import init as header_init

import website.style as style


def render():
    ui.context.client.content.classes("p-0 gap-0")
    header_init()
