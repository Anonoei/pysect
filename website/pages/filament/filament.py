from nicegui import ui

from website.header import init as header_init


def render():
    ui.context.client.content.classes("p-0 gap-0")
    header_init()
