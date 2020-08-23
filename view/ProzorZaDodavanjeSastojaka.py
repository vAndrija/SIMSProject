# Napomena: da li dodati novi sastojak u tabelu vec postojecih sastojaka

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from model.TipKolicine import *

class ProzorZaDodavanjeSastojaka(QDialog):
    def __init__(self):
        super().__init__()
        self.dodatiUTabelu = []
        self.sastojciMenadzer = QApplication.instance().actionManager.sastojciMenadzer

        self.initUI()

    def initUI(self):
        """
        Funkcija koja definise izgled prozora koji se prikazuje kada korisnik zeli da doda dugotrajne sastojke
        prilikom registracije.
        :return:
        """
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        ikonica = QIcon('..\slike\ikonica.png')
        self.setWindowIcon(ikonica)
        self.setFixedSize(800,900)
        image = QImage("..\slike\sastojci.jpg")
        sImage = image.scaled(QSize(800, 900))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

        self.postaviGrid()

        self.exec_()

    def postaviGrid(self):
        """
        Funkcija koja postavlja layout prozora za dodavanje dugotrajnih sastojaka prilikom registracije.
        :return:
        """
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = [ '', '', '',
                    '', '', '',
                 '', 'Izaberite sastojke:', '',
                 '', '*', '',
                 '', '?', '',
                 '', 'Dodajte novi sastojak:', '',
                 '', 'Unesite ime sastojka:', '',
                    '', '-', '',
                 '', 'Izaberite tip kolicine sastojka:', '',
                    '', '/', '',
                    '', '+', '',
                    '', '!', '',
                    '', '#', '',
                    '', '', '',
                 ]

        pozicije = [(i, j) for i in range(14) for j in range(3)]

        self.postojeciSastojci = None
        self.dodatiSastojci = None


        for pozicija, sadrzaj in zip(pozicije, matrica):
            if sadrzaj == "-":
                self.nazivSastojka = QLineEdit()
                self.nazivSastojka.setFixedSize(250,25)
                grid.addWidget(self.nazivSastojka, *pozicija)
            elif sadrzaj == "*":
                sviSastojci = self.sastojciMenadzer.sviSastojci
                self.postojeciSastojci = QTableWidget()
                self.postojeciSastojci.setColumnCount(3)
                self.postojeciSastojci.setRowCount(len(sviSastojci) + 1)
                self.postojeciSastojci.setColumnWidth(0, 120)
                self.postojeciSastojci.setColumnWidth(1,219)
                self.postojeciSastojci.setColumnWidth(2, 140)
                bold = QFont()
                bold.setBold(True)
                item = QTableWidgetItem("Naziv sastojka")
                item.setFont(bold)
                item.setTextAlignment(Qt.AlignCenter)
                item1 = QTableWidgetItem("Tip kolicine")
                item1.setFont(bold)
                item1.setTextAlignment(Qt.AlignCenter)
                item2 = QTableWidgetItem("Sifra")
                item2.setFont(bold)
                item2.setTextAlignment(Qt.AlignCenter)
                self.postojeciSastojci.setItem(0,0, item2)
                self.postojeciSastojci.setItem(0,1, item)
                self.postojeciSastojci.setItem(0,2, item1)
                brojac = 1
                for sastojak in sviSastojci:
                    self.postojeciSastojci.setItem(brojac, 0, QTableWidgetItem(str(sastojak.sifra)))
                    self.postojeciSastojci.setItem(brojac, 1, QTableWidgetItem(sastojak.naziv))
                    self.postojeciSastojci.setItem(brojac, 2, QTableWidgetItem(str(sastojak.tipKolicine)))
                    brojac += 1
                self.postojeciSastojci.setFixedSize(500, 165)
                grid.addWidget(self.postojeciSastojci, *pozicija)
            elif sadrzaj == "?":
                dugme = QPushButton("Dodaj sastojak")
                dugme.setFixedSize(250, 30)
                dugme.clicked.connect(self.dodajSastojak)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                self.comboBox = QComboBox()
                self.comboBox.addItem('Gram')
                self.comboBox.addItem('DL')
                self.comboBox.addItem('Komad')
                self.comboBox.addItem('Supena kasika')
                self.comboBox.addItem('Prstohvat')
                grid.addWidget(self.comboBox, *pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Dodaj sastojak")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.dodavanjeNovogSastojka)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "!":
                self.dodatiSastojci = QTableWidget()
                self.dodatiSastojci.setColumnCount(3)
                self.dodatiSastojci.setRowCount(1)
                self.dodatiSastojci.setColumnWidth(0, 120)
                self.dodatiSastojci.setColumnWidth(1,219)
                self.dodatiSastojci.setColumnWidth(2, 140)

                bold = QFont()
                bold.setBold(True)
                item = QTableWidgetItem("Naziv sastojka")
                item.setFont(bold)
                item.setTextAlignment(Qt.AlignCenter)
                item1 = QTableWidgetItem("Tip kolicine")
                item1.setFont(bold)
                item1.setTextAlignment(Qt.AlignCenter)

                item2 = QTableWidgetItem("Sifra")
                item2.setFont(bold)
                item2.setTextAlignment(Qt.AlignCenter)

                self.dodatiSastojci.setItem(0,0, item2)
                self.dodatiSastojci.setItem(0,1, item)
                self.dodatiSastojci.setItem(0,2, item1)
                self.dodatiSastojci.setFixedSize(500, 165)
                grid.addWidget(self.dodatiSastojci, *pozicija)
            elif sadrzaj == "#":
                dugme = QPushButton("Zavrsi dodavanje")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.zavrsenoDodavanje)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(170,35)
                grid.addWidget(labela, *pozicija)


    def dodajSastojak(self):
        """
        Funkcija koja se poziva kada korisnik zali da oznaceni sastojak iz tabele postojecih sastojaka doda u
        listu svojih dugotrajnih sastojaka prilikom registracije. Aktivira se pritiskom na dugme 'Dodaj sastojak'.
        :return:
        """
        sviSastojci = self.sastojciMenadzer.sviSastojci
        redovi = self.postojeciSastojci.selectionModel().selectedRows()
        brojRedova = self.dodatiSastojci.rowCount()
        brojac = 0
        for red in redovi:
            if red.row()-1 < 0:
                self.kreirajDijalogSPorukom("Ne mozete oznaciti red sa nazivima kolona.")
            else:
                sastojak = sviSastojci[red.row()-1]
                if sastojak in self.dodatiUTabelu:
                    self.kreirajDijalogSPorukom("Vec ste dodali ovaj sastojak.")
                else:
                    self.dodatiSastojci.insertRow(brojRedova + brojac)
                    self.dodatiUTabelu.append(sastojak)
                    self.dodatiSastojci.setItem(brojRedova + brojac, 0, QTableWidgetItem(str(sastojak.sifra)))
                    self.dodatiSastojci.setItem(brojRedova + brojac, 1, QTableWidgetItem(sastojak.naziv))
                    self.dodatiSastojci.setItem(brojRedova + brojac, 2, QTableWidgetItem(str(sastojak.tipKolicine)))
                    brojac += 1


    def kreirajDijalogSPorukom(self, porukaZaIspis):
        """
        Funkcija koja se poziva kada je potrebno kreirati dijalog sa porukom koja se salje korisniku.
        :param porukaZaIspis: poruka koja se prikazuje korisniku
        :return:
        """
        poruka = QMessageBox()
        poruka.setWindowTitle("Aplikacija za kuvare pocetnike")
        icon = QIcon("..\slike\ikonica.png")
        poruka.setWindowIcon(icon)
        poruka.setText(porukaZaIspis)
        poruka.exec_()


    def zavrsenoDodavanje(self):
        """
        Funkcija koja se poziva kada korisnik pritisne dugme 'Zavrsi dodavanje'. Prozor za dodavanje sastojaka se
        sakriva.
        :return:
        """
        self.hide()
        return self.dodatiUTabelu


    def dodavanjeNovogSastojka(self):
        """
        Funkcija koja se poziva kada korisnik pritisne dugme 'Dodaj sastojak', a prethodno je uneo naziv sastojka
        i izabrao tip kolicine. Korisnik na ovaj nacin dodaje sastojak koji se ne nalazi u tabeli postojecih sastojaka.
        :return:
        """
        naziv = self.nazivSastojka.text()
        tip = self.comboBox.currentIndex()

        if tip == 0:
            tipKolicine = TipKolicine.GRAM
        elif tip == 1:
            tipKolicine = TipKolicine.DL
        elif tip == 2:
            tipKolicine = TipKolicine.KOMAD
        elif tip == 3:
            tipKolicine = TipKolicine.SUPENAKASIKA
        else:
            tipKolicine = TipKolicine.PRSTOHVAT
        if naziv == "":
            self.kreirajDijalogSPorukom("Potrebno je uneti naziv sastojka.")
        else:
            sastojak = self.sastojciMenadzer.kreirajSastojak(naziv, tipKolicine)
            if sastojak == None:

                self.kreirajDijalogSPorukom("Uneti sastojak vec postoji u listi sastojaka.")
            else:
                brojRedova = self.dodatiSastojci.rowCount()
                self.dodatiSastojci.insertRow(brojRedova)
                self.dodatiUTabelu.append(sastojak)
                self.dodatiSastojci.setItem(brojRedova, 0, QTableWidgetItem(str(sastojak.sifra)))
                self.dodatiSastojci.setItem(brojRedova, 1, QTableWidgetItem(sastojak.naziv))
                self.dodatiSastojci.setItem(brojRedova, 2, QTableWidgetItem(str(sastojak.tipKolicine)))