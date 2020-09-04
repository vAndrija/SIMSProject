from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class PocetnaStranaAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Vracanje na pocetnu", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\slike\\vracanjePocetna.png'))

    def actionCalled(self):
        QApplication.instance().actionManager.glavniProzor.refresujPocetnu(None,None,None,None)