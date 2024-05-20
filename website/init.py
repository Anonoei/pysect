from nicegui import app, ui
from fastapi import HTTPException, Request

import pathlib

import website.main_page as main_page

app.add_static_files("/static", pathlib.Path(__file__).parent / "static")
app.add_static_files("/fonts", pathlib.Path(__file__).parent / "fonts")


@app.post("/dark_mode")
async def _post_dark_mode(request: Request) -> None:
    app.storage.browser["dark_mode"] = (await request.json()).get("value")


@ui.page("/")
def _main_page() -> None:
    main_page.create()


@app.get("/status")
def _status():
    return "Ok"
