import os
from functools import partial

from PyQt5.QtWebEngineWidgets import *

from view.PrikazInformacijaKuvara import *
from view.PrikazInformacijaUrednika import *
from view.ProzorZaRegistracijuUrednika import *
from view.ToolbarAdmin import *


class AdministratorPocetna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sledecaPostojiTab1 = None
        self.sledecaStranicaBrTab1 = 0
        self.sledecaPostojiTab2 = None
        self.sledecaStranicaBrTab2 = 0
        self.showMinimized()
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.show()
        self.setFixedSize(1000, 950)
        self.inicijalizacijaToolbar()
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

        self.informacije = QApplication.instance().actionManager.informacije

        self.inicijalizujTabove()

        self.hide()

    def inicijalizacijaToolbar(self):
        self.toolbar = ToolbarAdmin(self)

        self.addToolBar(self.toolbar)

    def inicijalizujTabove(self):
        self.tabovi = QTabWidget()
        # self.tab1 = QWidget()

        # self.inicijalizujTab1()
        self.inicijalizujTabKuvari()
        self.inicijalizujTabUrednici()
        self.tabovi.addTab(self.tab1, "Kuvari pocetnici")
        self.tabovi.addTab(self.tab2, "Urednici")
        self.setCentralWidget(self.tabovi)

    def inicijalizujTabKuvari(self):
        self.tab1 = QWidget()
        self.grid = QGridLayout()
        self.tab1.setLayout(self.grid)

        dio = os.getcwd()[:-4]
        dio = dio.split("\\")
        dio = "/".join(dio)
        putanja = 'file:///' + dio + 'dizajn/profilKorisnika'

        pozicije = [(i, j) for i in range(4) for j in range(2)]

        sviKuvari = self.informacije.sviKuvari

        self.dugmad = []
        trenutni = []

        if len(sviKuvari) >= (self.sledecaStranicaBrTab1 + 1) * 4:
            if len(sviKuvari) == (self.sledecaStranicaBrTab1 + 1) * 4:
                self.sledecaPostojiTab1 = False
            else:
                self.sledecaPostojiTab1 = True
            for i in range(self.sledecaStranicaBrTab1 * 4, self.sledecaStranicaBrTab1 * 4 + 4):
                trenutni.append(sviKuvari[i])
        else:
            self.sledecaPostojiTab1 = False
            for i in range(self.sledecaStranicaBrTab1 * 4, len(sviKuvari)):
                trenutni.append(sviKuvari[i])
            for i in range(len(sviKuvari), (self.sledecaStranicaBrTab1 + 1) * 4):
                trenutni.append("*")

        for pozicija, kuvar in zip(pozicije, trenutni):
            # if (pozicija[0] != 3):
            if (kuvar != "*"):
                privrem = QWidget()
                izgled1 = QVBoxLayout()
                privrem.setLayout(izgled1)
                privremeni = QWebEngineView()
                privremeni.setUrl(QUrl(putanja + "/" + kuvar.korisnickoIme + ".html"))
                izgled1.addWidget(privremeni)
                dugme = QPushButton(">>")
                self.dugmad.append(dugme)
                dugme.clicked.connect(partial(self.prikazDetaljnihInformacija, kuvar))
                dugme.setFixedSize(30, 30)
                izgled1.addWidget(dugme)

                self.grid.addWidget(privrem, *pozicija)

            else:
                privrem = QWidget()
                izgled1 = QVBoxLayout()
                privrem.setLayout(izgled1)
                self.grid.addWidget(privrem, *pozicija)

        pozicije = [(i, j) for i in range(4, 6) for j in range(2)]

        dugmeSledecaStrana = QPushButton("Sledeca strana")
        dugmePrethodnaStrana = QPushButton("Prethodna strana")
        dugmeDodajNovi = QPushButton("Dodajte novi nalog")
        dugmeDodajNovi.clicked.connect(self.dodajNoviNalog)

        dugmici = []
        if self.sledecaStranicaBrTab1 != 0:
            dugmici.append(dugmePrethodnaStrana)
            dugmePrethodnaStrana.clicked.connect(self.refresujPrethodnuTab1)
        else:
            dugmici.append(QLabel(""))
        if self.sledecaPostojiTab1:
            dugmici.append(dugmeSledecaStrana)
            dugmeSledecaStrana.clicked.connect(self.refresujSledecuTab1)
        else:
            dugmici.append(QLabel(""))
        dugmici.append(dugmeDodajNovi)

        for pozicija, dugme in zip(pozicije, dugmici):
            self.grid.addWidget(dugme, *pozicija)

    def refresujSledecuTab1(self):
        self.sledecaStranicaBrTab1 += 1
        self.inicijalizujTabove()

    def refresujPrethodnuTab1(self):
        self.sledecaStranicaBrTab1 -= 1
        self.inicijalizujTabove()

    def prikazDetaljnihInformacija(self, kuvar):
        PrikazInformacijaKuvara(kuvar, self)

    def refresujStranu(self):
        self.inicijalizujTabove()

    def dodajNoviNalog(self):
        ProzorZaRegistraciju()
        self.setWindowModality(Qt.WindowModal)
        self.refresujStranu()

    def postaviPoziciju(self):
        dHeight = QApplication.desktop().height()
        dWidth = QApplication.desktop().width()
        wHeight = self.size().height()
        wWidth = self.size().width()
        y = (dHeight - wHeight) / 2
        x = (dWidth - wWidth) / 2
        y = y - 50
        self.move(x, y)

    def inicijalizujTabUrednici(self):
        self.tab2 = QWidget()
        grid = QGridLayout()
        self.tab2.setLayout(grid)

        dio = os.getcwd()[:-4]
        dio = dio.split("\\")
        dio = "/".join(dio)
        putanja = 'file:///' + dio + 'dizajn/profilKorisnika'

        pozicije = [(i, j) for i in range(4) for j in range(2)]

        sviUrednici = self.informacije.sviUrednici

        self.dugmad = []
        trenutni = []

        if len(sviUrednici) >= (self.sledecaStranicaBrTab2 + 1) * 4:
            if len(sviUrednici) == (self.sledecaStranicaBrTab2 + 1) * 4:
                self.sledecaPostojiTab2 = False
            else:
                self.sledecaPostojiTab2 = True
            for i in range(self.sledecaStranicaBrTab2 * 4, self.sledecaStranicaBrTab2 * 4 + 4):
                trenutni.append(sviUrednici[i])
        else:
            self.sledecaPostojiTab2 = False
            for i in range(self.sledecaStranicaBrTab2 * 4, len(sviUrednici)):
                trenutni.append(sviUrednici[i])
            for i in range(len(sviUrednici), (self.sledecaStranicaBrTab2 + 1) * 4):
                trenutni.append("*")

        for pozicija, urednik in zip(pozicije, trenutni):
            # if (pozicija[0] != 3):
            if (urednik != "*"):
                privrem = QWidget()
                izgled1 = QVBoxLayout()
                privrem.setLayout(izgled1)
                privremeni = QWebEngineView()
                privremeni.setUrl(QUrl(putanja + "/" + urednik.korisnickoIme + ".html"))
                izgled1.addWidget(privremeni)
                dugme = QPushButton(">>")
                self.dugmad.append(dugme)
                dugme.clicked.connect(partial(self.prikazDetaljnihInformacijaUrednika, urednik))
                dugme.setFixedSize(30, 30)
                izgled1.addWidget(dugme)

                grid.addWidget(privrem, *pozicija)

            else:
                privrem = QWidget()
                izgled1 = QVBoxLayout()
                privrem.setLayout(izgled1)
                grid.addWidget(privrem, *pozicija)

        pozicije = [(i, j) for i in range(4, 6) for j in range(2)]

        dugmeSledecaStrana = QPushButton("Sledeca strana")
        dugmePrethodnaStrana = QPushButton("Prethodna strana")
        dugmeDodajNovi = QPushButton("Dodajte novi nalog")
        dugmeDodajNovi.clicked.connect(self.dodajNovogUrednika)

        dugmici = []
        if self.sledecaStranicaBrTab2 != 0:
            dugmici.append(dugmePrethodnaStrana)
            dugmePrethodnaStrana.clicked.connect(self.refresujPrethodnuTab2)
        else:
            dugmici.append(QLabel(""))
        if self.sledecaPostojiTab2:
            dugmici.append(dugmeSledecaStrana)
            dugmeSledecaStrana.clicked.connect(self.refresujSledecuTab2)
        else:
            dugmici.append(QLabel(""))
        dugmici.append(dugmeDodajNovi)

        for pozicija, dugme in zip(pozicije, dugmici):
            grid.addWidget(dugme, *pozicija)

    def refresujSledecuTab2(self):
        self.sledecaStranicaBrTab2 += 1
        self.inicijalizujTabove()
        self.refresujTab2()

    def refresujPrethodnuTab2(self):
        self.sledecaStranicaBrTab2 -= 1
        self.inicijalizujTabove()
        self.refresujTab2()

    def prikazDetaljnihInformacijaUrednika(self, urednik):
        PrikazInformacijaUrednika(urednik, self)

    def dodajNovogUrednika(self):
        ProzorZaRegistracijuUrednika()
        self.setWindowModality(Qt.WindowModal)
        self.refresujStranu()
        self.refresujTab2()

    def refresujTab2(self):
        self.tabovi.setCurrentWidget(self.tab2)
