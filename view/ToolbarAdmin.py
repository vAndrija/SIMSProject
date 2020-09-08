from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from controller.actions.Odjava import *
from controller.actions.PrikazSvogProfila import *
from controller.actions.Pretraga import *
class ToolbarAdmin(QToolBar):
    def __init__(self,parent):
        super().__init__(parent)
        self.show()
        self.dodajSadrzaj()
        self.roditelj = parent
    def dodajSadrzaj(self):
        vidzet = QWidget()

        vidzet.setFixedSize(900,40)
        vidzet.show()
        self.addWidget(vidzet)
        # napraviti prozor za prikazivanje informacija admina i urednika
        self.addAction(SopstveniProfilAkcija(self))
        self.addAction(OdjavaAkcija(self))


