from nicegui import app, ui
import website.init

ui.run(
    port=8328,
    title="PySect",
    show=False,
    dark=True,
    show_welcome_message=False,
    storage_secret="1234",
    native=True,
)
print(f"Access PySect at http://127.0.0.1:8328")
