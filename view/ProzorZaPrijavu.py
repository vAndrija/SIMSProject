#Kreiran prozor koji se prikazuje prilikom prijavljivanja

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
from PyQt5.QtCore import QSize
from view.ProzorZaRegistraciju import *
from view.KuvarPocetna import *
from controller.osnovneFunkcije import *
from view.ProzorZaPretragu import *
from model.Administrator import *
from model.KuvarPocetnik import *
from model.Urednik import *


class ProzorZaPrijavu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Funkcija koja definise izgled prozora za prijavu korisnika na aplikaciju.
        :return:
        """
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.setFixedSize(800,600)
        image = QImage("..\slike\prijava.jpg")
        sImage = image.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = [ '', '', '',
                    '', '', '',
                    '', '', '',
                    '', '', '',
                    '', '', '',
                 '', 'Unesite korisniko ime:', '',
                 '', '*', '',
                 '', 'Unesite lozinku:', '',
                 '', '^', '',
                 '', '+', '',
                 '', '/', '',
                    '', '', '',
                    '', '', '',
                    '', '', '',
                    '', '', '',
                 ]

        pozicije = [(i, j) for i in range(14) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "*":
                self.korisnickoIme = QLineEdit()
                grid.addWidget(self.korisnickoIme, *pozicija)
            elif sadrzaj =="^":
                self.lozinka = QLineEdit()
                grid.addWidget(self.lozinka,*pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Prijavite se")
                dugme.clicked.connect(self.prijava)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                dugme = QPushButton("Registrujte se")
                dugme.clicked.connect(self.registracija)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(240, 20)
                grid.addWidget(labela, *pozicija)

        self.show()


    def registracija(self):
        """
        Funkcija koja se poziva kada korisnik pritisne na dugme "Registruj se'. Prikazuje se prozor za registraciju
        korisnika.
        :return:
        """
        prozor = ProzorZaRegistraciju()

    def prijava(self):
        """
        Funkcija koja se poziva kada korisnik pritisne dugme 'Prijavi se'. Unutar funkcije poziva se funkcija koja
        proverava tacnost korisnickog imena i lozinke. U zavisnosti od uloge korisnika u sistemu objekat se kastuje.
        :return:
        """
        #ovde je potrebno obaviti poziv za funkciju koja provjerava ad li je korisnik prijavljen
        # i vraca objekat sa svim njegovim informacijama
        korisnik = provjeraPostojanjaKorisnika(self.korisnickoIme.text(),self.lozinka.text())
        if(korisnik!=None):
            self.hide()
            if(isinstance(korisnik,Administrator)):
                pass
            elif(isinstance(korisnik,Urednik)):
                pass
            else:
                QApplication.instance().actionManager.prijavljeniKorisnik=korisnik
                QApplication.instance().actionManager.glavniProzor.showMaximized()
                QApplication.instance().actionManager.glavniProzor.postaviPoziciju()
                QApplication.instance().actionManager.glavniProzor.show()
                QApplication.instance().actionManager.glavniProzor.refresujPocetnu()
        else:
            self.lozinka.setText("Pogresna lozinka ili korisnicko ime")





