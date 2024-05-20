from nicegui import app, ui
from fastapi import HTTPException, Request

import pathlib

import website.main_page as main_page

from .pages import render_platter
from .pages import render_slice
from .pages import render_filament
from .pages import render_printer

app.add_static_files("/static", pathlib.Path(__file__).parent / "static")
app.add_static_files("/fonts", pathlib.Path(__file__).parent / "fonts")


@app.post("/dark_mode")
async def _post_dark_mode(request: Request) -> None:
    app.storage.browser["dark_mode"] = (await request.json()).get("value")


@ui.page("/platter")
def _page_platter() -> None:
    render_platter()


@ui.page("/slice")
def _page_slice() -> None:
    render_slice()


@ui.page("/filament")
def _page_filament() -> None:
    render_filament()


@ui.page("/printer")
def _page_printer() -> None:
    render_printer()


@ui.page("/")
def _page_index() -> None:
    main_page.render()


@app.get("/status")
def _status():
    return "Ok"
