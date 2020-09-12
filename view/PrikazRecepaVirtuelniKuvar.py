from view.PrikazRecepta import *
from view.VirtuelniKuvar import *


class PrikazReceptaVirtuelniKuvar(PrikazRecepta):
    def __init__(self, parent, recept):
        super().__init__(parent, recept)

    def definisanjeDugmica(self, matrica, pozicije):

        self.naprijed = QPushButton("Sledeci recept")
        self.nazad = QPushButton("Prethodni recept")
        self.naprijed.clicked.connect(self.sledeci)
        self.nazad.clicked.connect(self.prethodni)
        if self.parent.trenutni == 0:
            self.nazad.setText("Predgovor")
        if self.parent.trenutni == len(self.parent.vKuvar.recepti) - 1:
            self.naprijed.hide()

        self.izgled.addWidget(self.naprijed, 4, 2)
        self.izgled.addWidget(self.nazad, 4, 0)

    def sledeci(self):
        self.close()
        self.parent.trenutni += 1
        self.parent.prikaziRecepteAkcija()

    def prethodni(self):
        if (self.parent.trenutni == 0):

            self.close()
            self.parent.pocetna = True
        else:
            self.close()
            self.parent.trenutni -= 1
            self.parent.prikaziRecepteAkcija()
