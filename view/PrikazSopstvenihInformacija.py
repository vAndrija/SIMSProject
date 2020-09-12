from copy import deepcopy

from controller.osnovneFunkcije import *
from view.ProzorZaDodavanjeOpreme import *
from view.ProzorZaDodavanjeSastojaka import *


class PrikazSopstvenihInformacija(QDialog):
    def __init__(self, korisnik):
        super().__init__()

        self.korisnik = korisnik
        self.privremenaOprema = deepcopy(self.korisnik.oprema)
        self.privremenaSastojci = deepcopy(self.korisnik.dugotrajniSastojci)
        self.initUI()
        self.inicijalizujGrid()
        self.dugotrajnaOprema = []
        self.noviSastojci = []
        self.exec_()

    def initUI(self):
        self.setWindowTitle("Prikaz profila")
        self.setFixedSize(800, 900)
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
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        matrica = ['Ime:', '1', '',
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
                   '', '12', '',
                   '', '16', '',
                   'Dugotrajna oprema:', '', '',
                   '', '11', '',
                   '', '13', '',
                   '', '17', '',
                   '', '14', '',
                   ]

        pozicije = [(i, j) for i in range(18) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "1":
                self.labelaIme = QLineEdit(self.korisnik.ime)
                self.labelaIme.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaIme, *pozicija)
            elif sadrzaj == "2":
                self.labelaPrezime = QLineEdit(self.korisnik.prezime)
                self.labelaPrezime.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaPrezime, *pozicija)
            elif sadrzaj == "3":
                self.labelaKorisnicko = QLineEdit(self.korisnik.korisnickoIme)
                self.labelaKorisnicko.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaKorisnicko, *pozicija)
            elif sadrzaj == "4":
                self.labelaMejl = QLineEdit(self.korisnik.mejl)
                self.labelaMejl.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaMejl, *pozicija)

            elif sadrzaj == "5":
                self.labelaDatum = QDateEdit(calendarPopup=True)
                self.labelaDatum.setDateTime(QDateTime.fromString(self.korisnik.datumRodjenja, "yyyy-MM-dd"))

                self.labelaDatum.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaDatum, *pozicija)
            elif sadrzaj == "6":
                self.labelaAdresa = QLineEdit(self.korisnik.adresa)
                self.labelaAdresa.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaAdresa, *pozicija)
            elif sadrzaj == "7":
                self.labelaMesto = QLineEdit(self.korisnik.mesto.nazivMesta)
                self.labelaMesto.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaMesto, *pozicija)
            elif sadrzaj == "8":
                self.labelaPostanski = QLineEdit(self.korisnik.mesto.postanskiBroj)
                self.labelaPostanski.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaPostanski, *pozicija)
            elif sadrzaj == "9":
                self.comboBox = QComboBox()
                self.comboBox.addItem("Zenski")
                self.comboBox.addItem("Muski")
                if self.korisnik.pol == 0:
                    self.comboBox.setCurrentIndex(0)
                else:
                    self.comboBox.setCurrentIndex(1)
                # labela = QLineEdit(pol)
                self.comboBox.setFixedSize(130, 20)
                self.grid.addWidget(self.comboBox, *pozicija)
            elif sadrzaj == "10":
                sastojci = self.korisnik.dugotrajniSastojci
                sviSastojci = nadjiSastojke(sastojci)
                self.postojeciSastojci = Tabela(len(sviSastojci) + 1, 3)
                self.postojeciSastojci.dodajZaglavlja(["Sifra", "Naziv sastojka", "Tip kolicine"])
                self.postojeciSastojci.setColumnWidth(0, 120)
                self.postojeciSastojci.setColumnWidth(1, 219)
                self.postojeciSastojci.setColumnWidth(2, 140)
                brojac = 1
                for sastojak in sviSastojci:
                    self.postojeciSastojci.setItem(brojac, 0, QTableWidgetItem(str(sastojak.sifra)))
                    self.postojeciSastojci.setItem(brojac, 1, QTableWidgetItem(sastojak.naziv))
                    self.postojeciSastojci.setItem(brojac, 2, QTableWidgetItem(str(sastojak.tipKolicine)))
                    brojac += 1
                self.postojeciSastojci.setFixedSize(522, 165)
                self.grid.addWidget(self.postojeciSastojci, *pozicija)
            elif sadrzaj == "11":
                oprema = self.korisnik.oprema
                svaOprema = nadjiOpremu(oprema)
                self.tabela = Tabela(len(svaOprema) + 1, 3)
                self.tabela.dodajZaglavlja(["Sifra", "Naziv", "Naziv marke"])
                self.tabela.setColumnWidth(0, 120)
                self.tabela.setColumnWidth(1, 219)
                self.tabela.setColumnWidth(2, 140)

                brojac = 1
                for aparat in svaOprema:
                    self.tabela.setItem(brojac, 0, QTableWidgetItem(str(aparat.sifra)))
                    self.tabela.setItem(brojac, 1, QTableWidgetItem(aparat.naziv))
                    self.tabela.setItem(brojac, 2, QTableWidgetItem(aparat.marka))
                    brojac += 1

                self.tabela.setFixedSize(522, 165)
                self.grid.addWidget(self.tabela, *pozicija)
            elif sadrzaj == "12":
                self.dodavanjeSastojaka = QPushButton("Dodavanje novih sastojaka")
                self.dodavanjeSastojaka.clicked.connect(self.dodavanjeNovihSastojaka)
                self.dodavanjeSastojaka.setFixedSize(230, 20)
                self.grid.addWidget(self.dodavanjeSastojaka, *pozicija)
            elif sadrzaj == "13":
                self.dodavanjeOpreme = QPushButton("Dodavanje nove opreme")
                self.dodavanjeOpreme.clicked.connect(self.dodavanjeNoveOpreme)
                self.dodavanjeOpreme.setFixedSize(230, 20)
                self.grid.addWidget(self.dodavanjeOpreme, *pozicija)
            elif sadrzaj == "14":
                self.azurirajDugme = QPushButton("Azuriraj informacije")
                self.azurirajDugme.clicked.connect(self.azuriranjePotvrdjeno)
                self.grid.addWidget(self.azurirajDugme, *pozicija)
            elif sadrzaj == "16":
                self.brisanjeSastojka = QPushButton("Brisanje selektovanog sastojka")
                self.brisanjeSastojka.setFixedSize(230, 20)
                self.grid.addWidget(self.brisanjeSastojka, *pozicija)
                self.brisanjeSastojka.clicked.connect(self.brisanjeSastojakaFunkcija)
            elif sadrzaj == "17":
                self.brisanjeOpreme = QPushButton("Brisanej selektovane opreme")
                self.brisanjeOpreme.setFixedSize(230, 20)
                self.grid.addWidget(self.brisanjeOpreme, *pozicija)
                self.brisanjeOpreme.clicked.connect(self.brisanjeOpremeFunkcija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(130, 20)
                self.grid.addWidget(labela, *pozicija)

    def dodavanjeNoveOpreme(self):
        prozor = ProzorZaDodavanjeOpreme()
        self.setWindowModality(Qt.WindowModal)
        self.dugotrajnaOprema = prozor.dodatiUTabelu
        self.refresujTabeluOpreme()

    def refresujTabeluOpreme(self):
        oprema = self.privremenaOprema + self.dugotrajnaOprema
        svaOprema = nadjiOpremu(oprema)
        self.tabela = Tabela(len(svaOprema) + 1, 3)
        self.tabela.dodajZaglavlja(["Sifra", "Naziv", "Naziv marke"])
        self.tabela.setColumnWidth(0, 120)
        self.tabela.setColumnWidth(1, 219)
        self.tabela.setColumnWidth(2, 140)

        brojac = 1
        for aparat in svaOprema:
            self.tabela.setItem(brojac, 0, QTableWidgetItem(str(aparat.sifra)))
            self.tabela.setItem(brojac, 1, QTableWidgetItem(aparat.naziv))
            self.tabela.setItem(brojac, 2, QTableWidgetItem(aparat.marka))
            brojac += 1

        self.tabela.setFixedSize(522, 165)
        self.grid.addWidget(self.tabela, 15, 1)

    def dodavanjeNovihSastojaka(self):
        prozor = ProzorZaDodavanjeSastojaka()
        self.setWindowModality(Qt.WindowModal)
        self.noviSastojci = prozor.dodatiUTabelu
        self.refresujTabeluSastojaka()

    def refresujTabeluSastojaka(self):
        sastojci = self.privremenaSastojci + self.noviSastojci
        sviSastojci = nadjiSastojke(sastojci)
        self.postojeciSastojci = Tabela(len(sviSastojci) + 1, 3)
        self.postojeciSastojci.dodajZaglavlja(["Sifra", "Naziv sastojka", "Tip kolicine"])
        self.postojeciSastojci.setColumnWidth(0, 120)
        self.postojeciSastojci.setColumnWidth(1, 219)
        self.postojeciSastojci.setColumnWidth(2, 140)
        brojac = 1
        for sastojak in sviSastojci:
            self.postojeciSastojci.setItem(brojac, 0, QTableWidgetItem(str(sastojak.sifra)))
            self.postojeciSastojci.setItem(brojac, 1, QTableWidgetItem(sastojak.naziv))
            self.postojeciSastojci.setItem(brojac, 2, QTableWidgetItem(str(sastojak.tipKolicine)))
            brojac += 1
        self.postojeciSastojci.setFixedSize(522, 165)
        self.grid.addWidget(self.postojeciSastojci, 11, 1)

    def azuriranjePotvrdjeno(self):

        self.korisnik.ime = self.labelaIme.text()
        self.korisnik.prezime = self.labelaPrezime.text()
        self.korisnik.korisnickoIme = self.labelaKorisnicko.text()
        # self.korisnik.lozinka = self.labelaLozinka.text()
        self.korisnik.datumRodjenja = str(self.labelaDatum.date().toPyDate())
        self.korisnik.mesto.nazivMesta = self.labelaMesto.text()
        self.korisnik.adresa = self.labelaAdresa.text()
        self.korisnik.mesto.postanskiBroj = self.labelaPostanski.text()
        self.korisnik.mejl = self.labelaMejl.text()
        if self.comboBox.currentIndex() == 0:
            self.korisnik.pol = 0
        else:
            self.korisnik.pol = 1

        self.korisnik.oprema = self.privremenaOprema + self.dugotrajnaOprema
        self.korisnik.dugotrajniSastojci = self.privremenaSastojci + self.noviSastojci
        QApplication.instance().actionManager.informacije.upisiKorisnika()
        self.close()

    def brisanjeOpremeFunkcija(self):

        selektovaniRedovi = self.tabela.selectionModel().selectedRows()
        for red in selektovaniRedovi:

            if (red.row() > len(self.privremenaOprema)):

                self.dugotrajnaOprema.pop(red.row() - len(self.privremenaOprema) - 1)
                self.refresujTabeluOpreme()
            else:
                self.privremenaOprema.pop(red.row() - 1)
                self.refresujTabeluOpreme()

    def brisanjeSastojakaFunkcija(self):
        selektovaniRedovi = self.postojeciSastojci.selectionModel().selectedRows()
        for red in selektovaniRedovi:
            if (red.row() > len(self.privremenaSastojci)):
                self.noviSastojci.pop(red.row() - len(self.privremenaSastojci) - 1)
                self.refresujTabeluSastojaka()
            else:
                self.privremenaSastojci.pop(red.row() - 1)
                self.refresujTabeluSastojaka()
