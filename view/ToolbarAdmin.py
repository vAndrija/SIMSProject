from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from controller.actions.Odjava import *
from controller.actions.AdminUrednikProfil import *
from controller.actions.PromenaLozinkeAkcija import *

class ToolbarAdmin(QToolBar):
    def __init__(self,parent):
        super().__init__(parent)
        self.show()
        self.dodajSadrzaj()
        self.roditelj = parent
    def dodajSadrzaj(self):
        vidzet = QWidget()

        vidzet.setFixedSize(850,40)
        vidzet.show()
        self.addWidget(vidzet)
        self.addAction(AdminUrednikProfil(self))
        self.addAction(PromenaLozinkeAkcija(self))
        self.addAction(OdjavaAkcija(self))


