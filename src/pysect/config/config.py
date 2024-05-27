from ..printer.printer import Printer
from ..filament.filament import Filament
from ..slice.slice import Slice

import pyboiler.generic as generic


class Config(generic.slot_storage):

    __slots__ = ("printers", "filaments", "slices", "selected")

    def __init__(self):
        self.printers: dict[str, Printer] = {}
        self.filaments: dict[str, Filament] = {}
        self.slices: dict[str, Slice] = {}
        self.selected: dict[str, str] = {"printer": "", "filament": "", "slice": ""}

    def printer(self) -> Printer:
        return self.printers[self.selected["printer"]]

    def filament(self) -> Filament:
        return self.filaments[self.selected["filament"]]

    def slice(self) -> Slice:
        return self.slices[self.selected["slice"]]

    def add_printer(self, printer: Printer):
        self.printers[printer.name] = printer
        self.selected["printer"] = printer.name

    def add_filament(self, filament: Filament):
        self.filaments[filament.name] = filament
        self.selected["filament"] = filament.name

    def add_slice(self, slice: Slice):
        self.slices[slice.name] = slice
        self.selected["slice"] = slice.name
