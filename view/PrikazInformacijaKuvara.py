from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from controller.osnovneFunkcije import *
from view.Tabela import *


class PrikazInformacijaKuvara(QDialog):
    def __init__(self, korisnik):
        super().__init__()
        self.korisnik = korisnik
        self.initUI()
        self.inicijalizujGrid()

        self.exec_()

    def initUI(self):
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.setFixedSize(800,800)
        image = QImage("..\slike\profil.jpg")
        sImage = image.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

    def inicijalizujGrid(self):
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = [ 'Ime:', '1', '',
                    'Prezime:', '2', '',
                  'Korisnicko ime:', '3', '',
                  'Mejl:', '4', '',
                  'Datum rodjenja:', '5', '',
                  'Adresa:', '6', '',
                  'Naziv mesta:', '7', '',
                  'Postanski broj:', '8', '',
                  'Pol:', '9', '',
                  'Dugotrajni sastojci:', '', '',
                  '', '10', '',
                  'Dugotrajna oprema:', '', '',
                  '', '11', '',
                 ]

        pozicije = [(i, j) for i in range(13) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "1":
                labela = QLabel(self.korisnik.ime)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "2":
                labela = QLabel(self.korisnik.prezime)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "3":
                labela = QLabel(self.korisnik.korisnickoIme)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "4":
                labela = QLabel(self.korisnik.mejl)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "5":
                labela = QLabel(self.korisnik.datumRodjenja)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "6":
                labela = QLabel(self.korisnik.adresa)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "7":
                labela = QLabel(self.korisnik.mesto.nazivMesta)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "8":
                labela = QLabel(self.korisnik.mesto.postanskiBroj)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "9":
                if self.korisnik.pol == 0:
                    pol = "Zenski"
                else:
                    pol = "Muski"
                labela = QLabel(pol)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "10":
                sastojci = self.korisnik.dugotrajniSastojci
                sviSastojci = nadjiSastojke(sastojci)
                self.postojeciSastojci = Tabela(len(sviSastojci) + 1, 3)
                self.postojeciSastojci.dodajZaglavlja(["Sifra", "Naziv sastojka", "Tip kolicine"])
                self.postojeciSastojci.setColumnWidth(0, 120)
                self.postojeciSastojci.setColumnWidth(1,219)
                self.postojeciSastojci.setColumnWidth(2, 140)
                brojac = 1
                for sastojak in sviSastojci:
                    self.postojeciSastojci.setItem(brojac, 0, QTableWidgetItem(str(sastojak.sifra)))
                    self.postojeciSastojci.setItem(brojac, 1, QTableWidgetItem(sastojak.naziv))
                    self.postojeciSastojci.setItem(brojac, 2, QTableWidgetItem(str(sastojak.tipKolicine)))
                    brojac += 1
                self.postojeciSastojci.setFixedSize(522, 165)
                grid.addWidget(self.postojeciSastojci, *pozicija)
            elif sadrzaj == "11":
                oprema = self.korisnik.oprema
                svaOprema = nadjiOpremu(oprema)
                tabela = Tabela(len(svaOprema) + 1,3)
                tabela.dodajZaglavlja(["Sifra", "Naziv", "Naziv marke"])
                tabela.setColumnWidth(0, 120)
                tabela.setColumnWidth(1,219)
                tabela.setColumnWidth(2, 140)

                brojac = 1
                for aparat in svaOprema:
                    tabela.setItem(brojac, 0, QTableWidgetItem(str(aparat.sifra)))
                    tabela.setItem(brojac, 1, QTableWidgetItem(aparat.naziv))
                    tabela.setItem(brojac, 2, QTableWidgetItem(aparat.marka))
                    brojac += 1

                tabela.setFixedSize(522, 165)
                grid.addWidget(tabela, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
