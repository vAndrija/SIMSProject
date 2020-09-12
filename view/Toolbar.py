from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from controller.actions.AkcijaBrisanjaRecepata import AkcijaBrisanjaRecepata
from controller.actions.KreiranjeReceptaAkcija import KreiranjeReceptaAkcija
from controller.actions.Odjava import *
from controller.actions.PrikazSvogProfila import *
from controller.actions.Pretraga import *
from controller.actions.PocetnaStranaAkcija import *
from controller.actions.SpisakZaKupovinuAkcija import SpisakZaKupovinuAkcija
from controller.actions.UrednjivanjeKategorija import *
from controller.actions.UredjivanjePratilaca import *
from controller.actions.SopstveniReceptiAkcija import *
from controller.actions.VirtuelniAkcija import *
from controller.actions.PromenaLozinkeAkcija import *
class Toolbar(QToolBar):
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
        self.addAction(VirtuelniAkcija(self))
        self.addAction(SpisakZaKupovinuAkcija(self))
        self.addAction(AkcijaBrisanjaRecepata(self))
        self.addAction(SopstveniReceptiAkcija(self))
        self.addAction(KreiranjeReceptaAkcija(self))
        self.addAction(UredjivanjePratilaca(self))
        self.addAction(UredjivanjeKategorija(self))
        self.addAction(PocetnaStranaAkcija(self))
        self.addAction(PretragaAkcija(self))
        self.addAction(SopstveniProfilAkcija(self))
        self.addAction(PromenaLozinkeAkcija(self))
        self.addAction(OdjavaAkcija(self))


