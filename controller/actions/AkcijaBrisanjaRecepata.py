

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view.PraceniKuvari import *
from view.ProzorZaBrisanjeRecepta import *
class AkcijaBrisanjaRecepata(QAction):
    def __init__(self, parent):
        super().__init__("Brisanje recepta", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\gumica.png'))

    def actionCalled(self):
        prozor = ProzorZaBrisanjeRecepta(QApplication.instance().actionManager.glavniProzor)
