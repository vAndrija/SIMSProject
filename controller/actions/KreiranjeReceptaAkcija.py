from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from view.ProzorZaKreiranjeRecepta import ProzorZaKreiranjeRecepta
import traceback

class KreiranjeReceptaAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Dodaj novi recept", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\slike\plusic.png'))

    def actionCalled(self):
        try:
            ProzorZaKreiranjeRecepta()
        except:
            traceback.print_exc()
