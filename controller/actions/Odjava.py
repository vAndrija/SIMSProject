from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class OdjavaAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Odjavi se", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\slike\odjava.jpg'))

    def actionCalled(self):
        QApplication.instance().actionManager.glavniProzor.close()
        QApplication.instance().actionManager.prijava.show()
