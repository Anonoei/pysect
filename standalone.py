from nicegui import app, ui
import website.init

ui.run(port=8328, title="PySect", storage_secret="1234", native=True)
