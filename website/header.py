from nicegui import ui, app
from typing import Optional

import pathlib

HEADER_HTML = (pathlib.Path(__file__).parent / "static" / "header.html").read_text()
STYLE_CSS = (pathlib.Path(__file__).parent / "static" / "style.css").read_text()


def add_head_html() -> None:
    """Add the code from header.html and reference style.css."""
    ui.add_head_html(HEADER_HTML + f"<style>{STYLE_CSS}</style>")


def add_header(menu: Optional[ui.left_drawer] = None) -> None:
    """Create the page header."""
    menu_items = {"PySect": "/"}
    dark_mode = ui.dark_mode(
        value=app.storage.browser.get("dark_mode"),
        on_change=lambda e: ui.run_javascript(
            f"""
        fetch('/dark_mode', {{
            method: 'POST',
            headers: {{'Content-Type': 'application/json'}},
            body: JSON.stringify({{value: {e.value}}}),
        }});
    """
        ),
    )
    with ui.header().classes("items-center duration-200 p-0 px-4 no-wrap").style(
        "box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)"
    ):
        if menu:
            ui.button(on_click=menu.toggle, icon="menu").props(
                "flat color=white round"
            ).classes("lg:hidden")

        with ui.row().classes("max-[1050px]:hidden"):
            for title_, target in menu_items.items():
                ui.link(title_, target).classes(replace="text-lg text-white")

        with ui.element().classes("max-[420px]:hidden").tooltip(
            "Cycle theme mode through dark, light, and system/auto."
        ):
            ui.button(
                icon="dark_mode", on_click=lambda: dark_mode.set_value(None)
            ).props("flat fab-mini color=white").bind_visibility_from(
                dark_mode, "value", value=True
            )
            ui.button(
                icon="light_mode", on_click=lambda: dark_mode.set_value(True)
            ).props("flat fab-mini color=white").bind_visibility_from(
                dark_mode, "value", value=False
            )
            ui.button(
                icon="brightness_auto", on_click=lambda: dark_mode.set_value(False)
            ).props("flat fab-mini color=white").bind_visibility_from(
                dark_mode, "value", lambda mode: mode is None
            )

        with ui.row().classes("min-[1051px]:hidden"):
            with ui.button(icon="more_vert").props("flat color=white round"):
                with ui.menu().classes("bg-primary text-white text-lg"):
                    for title_, target in menu_items.items():
                        ui.menu_item(
                            title_,
                            on_click=lambda target=target: ui.navigate.to(target),
                        )
