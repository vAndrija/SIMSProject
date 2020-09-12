from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PocetnaStranaAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Vracanje na pocetnu", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\slike\\vracanjePocetna.png'))

    def actionCalled(self):
        QApplication.instance().actionManager.glavniProzor.inicijalizujPocetnu()
        QApplication.instance().actionManager.glavniProzor.sledecaPostoji = True
        QApplication.instance().actionManager.glavniProzor.sledecaStranicaBrojac = 0
        QApplication.instance().actionManager.glavniProzor.refresujPocetnu(None, None, None, None)
