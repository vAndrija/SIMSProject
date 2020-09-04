import os
import traceback

from PyQt5.QtWebEngineWidgets import *

from view.ProzorZaPretragu import *
from view.Toolbar import *


class KuvarPocetna(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.show()
        self.sledecaStranicaBrojac = 0
        self.sledecaPostoji = None
        self.setFixedSize(1360, 700)
        self.postaviPoziciju()
        self.inicijalizujDesnuReklamu()
        self.inicijalizujLijevuReklamu()
        self.inicijalizacijaToolbar()
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

        self.recepti = []
        self.inicijalizujPocetnu()

    def postaviPoziciju(self):
        dHeight = QApplication.desktop().height()
        dWidth = QApplication.desktop().width()
        wHeight = self.size().height()
        wWidth = self.size().width()
        y = (dHeight - wHeight) / 2
        x = (dWidth - wWidth) / 2
        y = y - 50
        self.move(x, y)

    def inicijalizacijaToolbar(self):
        self.toolbar = Toolbar(self)
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

    def inicijalizujPocetnu(self):
        """
       
        :return: 
        """""
        self.lista = QWidget()
        self.setCentralWidget(self.lista)
        self.izgled = QGridLayout()
        self.lista.setLayout(self.izgled)
        self.lista.show()

    def sortiraj(self, elem):
        for element in self.mapiranje:
            if element[1] is elem:
                return element[0]

    def refresujPocetnu(self, recepti, oprema, sastojci, napredno):

        self.zbirno = []
        dio = os.getcwd()[:-4]
        dio = dio.split("\\")
        dio = "/".join(dio)
        putanja = 'file:///' + dio + 'dizajn/pocetnaRecepti'
        pozicije = [(i, j) for i in range(4) for j in range(2)]
        self.dugmad = []
        self.sledecaStranicaBrojac = 0
        if (recepti == None):
            self.recepti = QApplication.instance().actionManager.receptiMenadzer.receptiZaPrikaz()
        else:

            self.recepti = recepti

        trenutni = []
        if napredno:
            self.zbirno = []
            for prvi, drugi in zip(oprema, sastojci):
                self.zbirno.append(0)
                self.zbirno[-1] = prvi + drugi
            self.mapiranje = []
            for kljuc, vrijednost in zip(self.zbirno, self.recepti):
                self.mapiranje.append([kljuc, vrijednost])
            self.mapiranje1=[]
            for prvi,drugi,recept in zip(oprema,sastojci,self.recepti):
                self.mapiranje1.append([prvi,drugi,recept])


            self.recepti.sort(key=self.sortiraj)


        if (len(self.recepti) >= ((self.sledecaStranicaBrojac + 1) * 4)):
            if ((len(self.recepti) == ((self.sledecaStranicaBrojac + 1) * 4))):
                self.sledecaPostoji = False
            else:
                self.sledecaPostoji = True
            for i in range(self.sledecaStranicaBrojac * 4, self.sledecaStranicaBrojac + 4):
                trenutni.append(self.recepti[i])
        else:
            self.sledecaPostoji = False
            for i in range(self.sledecaStranicaBrojac * 4, len(self.recepti)):
                trenutni.append(self.recepti[i])
            for i in range(self.sledecaStranicaBrojac * 4, len(self.recepti),
                           (self.sledecaStranicaBrojac + 1) * 4):
                trenutni.append("*")

        for pozicija, recept in zip(pozicije, trenutni):
            if (pozicija[0] != 3):
                if (recept != "*"):
                    privrem = QWidget()
                    izgled1 = QVBoxLayout()
                    privrem.setLayout(izgled1)
                    privremeni = QWebEngineView()
                    privremeni.setUrl(QUrl(putanja + "/" + str(recept.id) + ".html"))
                    izgled1.addWidget(privremeni)

                    dugme = QPushButton(">>")
                    horizontalno = QHBoxLayout()
                    horizontalno.addWidget(dugme)
                    if napredno:
                        for clan in self.mapiranje1:
                            if(clan[2] is recept):
                                if (clan[1] == 0 and clan[0] == 0):
                                    tekst = "Imate sve potrebne sastojke i opremu"

                                else:
                                    tekst = "Nedostaje {0} sastojaka i {1} opreme".format(
                                        clan[1], clan[0])

                                labela = QLabel(tekst)
                                toolTip = QApplication.instance().actionManager.receptiMenadzer.vracanjeToolTipSadrzaja(
                                    recept)
                                labela.setToolTip(toolTip)

                                horizontalno.addWidget(labela)
                    drugi = QWidget()
                    drugi.setLayout(horizontalno)
                    self.dugmad.append(dugme)
                    dugme.setFixedSize(30, 30)
                    izgled1.addWidget(drugi)
                    self.izgled.addWidget(privrem, *pozicija)
                else:
                    privrem = QWidget()
                    izgled1 = QVBoxLayout()
                    privrem.setLayout(izgled1)
                    self.izgled.addWidget(privrem, *pozicija)
        if (len(self.recepti) == 0):
            for pozicija in pozicije:
                if (pozicija[0] != 3):
                    privrem = QWidget()
                    izgled1 = QVBoxLayout()
                    privrem.setLayout(izgled1)
                    self.izgled.addWidget(privrem, *pozicija)

        self.trenutniRecepti = 4
        self.sledecaStranica = QPushButton("Sledeca stranica")
        self.sledecaStranica.clicked.connect(lambda x:self.sledecaStranicaAkcija(oprema,sastojci,napredno))
        self.izgled.addWidget(self.sledecaStranica, 3, 0)

    def sledecaStranicaAkcija(self, oprema, sastojci, napredno):
        if (self.sledecaPostoji):
            self.inicijalizujPocetnu()
            self.sledecaStranicaBrojac = +1
            dio = os.getcwd()[:-4]
            dio = dio.split("\\")
            dio = "/".join(dio)
            putanja = 'file:///' + dio + 'dizajn/pocetnaRecepti'
            pozicije = [(i, j) for i in range(4) for j in range(2)]
            trenutni = []
            if napredno:
                print("Usao")
                self.zbirno = []
                for prvi, drugi in zip(oprema, sastojci):
                    self.zbirno.append(0)
                    self.zbirno[-1] = prvi + drugi
                self.mapiranje = []
                for kljuc, vrijednost in zip(self.zbirno, self.recepti):
                    self.mapiranje.append([kljuc, vrijednost])
                self.mapiranje1=[]
                for prvi,drugi,recept in zip(oprema,sastojci,self.recepti):
                    self.mapiranje1.append([prvi,drugi,recept])
                    print(prvi,drugi,recept.naziv)

                self.recepti.sort(key=self.sortiraj)
            if (len(self.recepti) >= ((self.sledecaStranicaBrojac + 1) * 4)):
                if ((len(self.recepti) == ((self.sledecaStranicaBrojac + 1) * 4))):
                    self.sledecaPostoji = False
                else:
                    self.sledecaPostoji = True
                for i in range(self.sledecaStranicaBrojac * 4, self.sledecaStranicaBrojac + 4):
                    trenutni.append(self.recepti[i])
            else:
                self.sledecaPostoji = False
                for i in range(self.sledecaStranicaBrojac * 4, len(self.recepti)):
                    trenutni.append(self.recepti[i])
                for i in range(len(self.recepti), (self.sledecaStranicaBrojac + 1) * 4):
                    trenutni.append("*")
            for pozicija, recept in zip(pozicije, trenutni):
                if (pozicija[0] != 3):
                    if (recept != "*"):
                        privrem = QWidget()
                        izgled1 = QVBoxLayout()
                        privrem.setLayout(izgled1)
                        privremeni = QWebEngineView()
                        privremeni.setUrl(QUrl(putanja + "/" + str(recept.id) + ".html"))
                        izgled1.addWidget(privremeni)
                        dugme = QPushButton(">>")
                        horizontalno = QHBoxLayout()
                        horizontalno.addWidget(dugme)
                        if napredno:
                            for clan in self.mapiranje1:
                                if (clan[2] is recept):
                                    if (clan[1] == 0 and clan[0] == 0):
                                        tekst = "Imate sve potrebne sastojke i opremu"

                                    else:
                                        tekst = "Nedostaje {0} sastojaka i {1} opreme".format(
                                            clan[1], clan[0])

                                    labela = QLabel(tekst)
                                    toolTip = QApplication.instance().actionManager.receptiMenadzer.vracanjeToolTipSadrzaja(recept)
                                    labela.setToolTip(toolTip)
                                    horizontalno.addWidget(labela)
                        drugi = QWidget()
                        drugi.setLayout(horizontalno)
                        self.dugmad.append(dugme)
                        dugme.setFixedSize(30, 30)
                        izgled1.addWidget(drugi)
                        self.izgled.addWidget(privrem, *pozicija)
                    else:
                        privrem = QWidget()
                        izgled1 = QVBoxLayout()
                        privrem.setLayout(izgled1)
                        self.izgled.addWidget(privrem, *pozicija)
            self.izgled.addWidget(self.sledecaStranica, 3, 0)
    def inicijalizujLijevuReklamu(self):
        """
        Funkcija izvrsava inicijalizovanje i postavljanje pocetnog sadrzaja lijeve reklame u prozoru
        :return:
        """
        reklama = QWebEngineView()
        self.lijevaReklama = QDockWidget()
        self.lijevaReklama.setWidget(reklama)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.lijevaReklama)
        self.lijevaReklama.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.lijevaReklama.setFixedSize(300, 700)
        reklama.showFullScreen()
        reklama.setUrl(QUrl("https://online.idea.rs/#!/categories/60008342/idea-organic"))

    def inicijalizujDesnuReklamu(self):
        """
               Funkcija izvrsava inicijalizovanje i postavljanje pocetnog sadrzaja desne reklame u prozoru
               :return:
               """
        reklama = QWebEngineView()
        self.desnaReklama = QDockWidget()
        self.desnaReklama.setWidget(reklama)
        self.addDockWidget(Qt.RightDockWidgetArea, self.desnaReklama)
        self.desnaReklama.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.desnaReklama.setFixedSize(300, 700)
        reklama.showFullScreen()
        reklama.setUrl(QUrl("https://online.idea.rs/#!/offers"))
