from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SopstveniReceptiAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Prikazi sopstvene recepte", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\slike\sopstveniRecepti.jpg'))

    def actionCalled(self):
        try:
            QApplication.instance().actionManager.receptiMenadzer.pronadjiReceptePrijavljenog()
            receptiPrijavljenog = QApplication.instance().actionManager.receptiMenadzer.receptiPrijavljenog
            QApplication.instance().actionManager.glavniProzor.inicijalizujPocetnu()
            QApplication.instance().actionManager.glavniProzor.sledecaPostoji = True
            QApplication.instance().actionManager.glavniProzor.sledecaStranicaBrojac = 0
            QApplication.instance().actionManager.glavniProzor.refresujPocetnu(receptiPrijavljenog, [], [], False)
        except Exception as e:
            print(e)
