from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view.PrikazKategorija import *
class UredjivanjeKategorija(QAction):
    def __init__(self, parent):
        super().__init__("Pregled i uredjivanje pracenih kategorija", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\pracenjeKategorije.png'))

    def actionCalled(self):
        prozor = PrikazKategorija(QApplication.instance().actionManager.glavniProzor)