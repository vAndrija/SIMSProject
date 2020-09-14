import traceback

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from view.PredgovorDijalog import PredgovorDijalog
from view.PrikazRecepaVirtuelniKuvar import PrikazReceptaVirtuelniKuvar


class VirtuelniKuvar(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.menadzerVKuvara = QApplication.instance().actionManager.vKuvarMenadzer
        self.kuvarPocetnik = QApplication.instance().actionManager.prijavljeniKorisnik
        self.menadzerReceptima = QApplication.instance().actionManager.receptiMenadzer
        self.trenutni = 0
        self.recept = None
        self.pocetna = False
        self.azuriraniPredgovor = None
        self.initUi()
        self.show()
        self.exec_()

    def initUi(self):
        self.vKuvar = QApplication.instance().actionManager.vKuvarMenadzer.vratiVirtuelniKuvar(
            self.kuvarPocetnik.virtuelniKuvar
        )
        self.setWindowTitle("Virtuelni kuvar")
        self.setModal(True)
        image = QImage("..\slike\\virtuelni.jpg")
        sImage = image.scaled(QSize(1000, 900))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.setFixedSize(1000, 900)
        self.izgled = QGridLayout()
        self.setLayout(self.izgled)
        matrica = ['', '3', '',
                   '', '1', '',
                   '', '', '',
                   '', '4', '2']
        self.sastojci = []
        self.oprema = []
        pozicije = [(i, j) for i in range(4) for j in range(3)]
        for pozicija, sadrzaj in zip(pozicije, matrica):
            if sadrzaj == "3":
                labela = QLabel('<h1>Moj virtuelni kuvar</h1>')
                labela.setAlignment(Qt.AlignCenter)
                self.izgled.addWidget(labela, *pozicija)
            elif sadrzaj == "1":
                self.predgovor = QLabel('<i><b>{0}</i></b>'.format(self.vKuvar.predgovor))
                self.predgovor.setWordWrap(True)
                self.predgovor.setAlignment(Qt.AlignCenter)
                self.izgled.addWidget(self.predgovor, *pozicija)
            elif sadrzaj == "2":
                self.dugme = QPushButton("Azuriraj predogovor")
                self.izgled.addWidget(self.dugme, *pozicija)
                self.dugme.clicked.connect(self.azuriranjePredgovora)
            elif sadrzaj == "4":
                self.prikaziRecepte = QPushButton("Prikazi recepte")
                self.prikaziRecepte.clicked.connect(self.prikaziRecepteAkcija)
                self.izgled.addWidget(self.prikaziRecepte, *pozicija)

            else:
                self.labela = QLabel(sadrzaj)
                self.izgled.addWidget(self.labela, *pozicija)


    def azuriranjePredgovora(self):
        PredgovorDijalog(self)
        if(self.azuriraniPredgovor!= None):
            self.vKuvar.predgovor = self.azuriraniPredgovor
            self.predgovor.setText('<i><b>{0}</i></b>'.format(self.vKuvar.predgovor))
            QApplication.instance().actionManager.vKuvarMenadzer.upisiVirtuelneKuvare()




    def prikaziRecepteAkcija(self):
        if (len(self.vKuvar.recepti) == 0):
            return
        self.hide()
        self.recept = self.menadzerReceptima.vratiRecept(self.vKuvar.recepti[self.trenutni])
        PrikazReceptaVirtuelniKuvar(self, self.recept)
        self.close()
        if self.pocetna:
            self.pocetna = False

            VirtuelniKuvar(QApplication.instance().actionManager.glavniProzor)
