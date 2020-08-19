from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from controller.actions.Odajava import *
from controller.actions.PrikazSvogProfila import *
class Toolbar(QToolBar):
    def __init__(self,parent):
        super().__init__(parent)
        self.show()
        self.dodajSadrzaj()
        self.roditelj = parent
    def dodajSadrzaj(self):
        vidzet = QWidget()

        vidzet.setFixedSize(1200,40)
        vidzet.show()
        self.addWidget(vidzet)
        self.addAction(SopstveniProfilAkcija(self))
        self.addAction(OdjavaAkcija(self))
