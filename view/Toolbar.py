from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from controller.actions.Odajava import *
from controller.actions.PrikazSvogProfila import *
from controller.actions.Pretraga import *
from controller.actions.PocetnaStranaAkcija import *
class Toolbar(QToolBar):
    def __init__(self,parent):
        super().__init__(parent)
        self.show()
        self.dodajSadrzaj()
        self.roditelj = parent
    def dodajSadrzaj(self):
        vidzet = QWidget()

        vidzet.setFixedSize(1150,40)
        vidzet.show()
        self.addWidget(vidzet)
        self.addAction(PocetnaStranaAkcija(self))
        self.addAction(PretragaAkcija(self))
        self.addAction(SopstveniProfilAkcija(self))
        self.addAction(OdjavaAkcija(self))


