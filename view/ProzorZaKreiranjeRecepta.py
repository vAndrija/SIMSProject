import traceback

from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QLineEdit, QComboBox, QLabel, QPlainTextEdit, QTableWidget,
                             QTableWidgetItem, QScrollArea, QFileDialog, QDialog,
                             QHBoxLayout)

from model.TipKolicine import TipKolicine
from view.ObavestavajucaPoruka import ObavestavajucaPoruka


class QStringList(object):
    pass


class ProzorZaKreiranjeRecepta(QDialog):

    def __init__(self):
        super().__init__()
        self.menadzerReceptima = QApplication.instance().actionManager.receptiMenadzer
        self.menadzerSastojcima = QApplication.instance().actionManager.sastojciMenadzer
        self.menadzerOpremom = QApplication.instance().actionManager.opremaMenadzer

        self.initUI()
        self.exec_()

    def popunjenaPoljaRecept(self):
        if (self.nazivRecepta.text() == ""):
            return False;
        if (self.putanja.text() == ""):
            return False;

        if (self.informacije.toPlainText() == ""):
            return False
        if (self.tabelaSastojaka.rowCount() <= 1):
            return False
        if (self.tabelaKategorija.rowCount() <= 1):
            return False

        print(self.tabelaKategorija.rowCount())
        return True

    def popunjenaPoljaSastojci(self):
        if (self.nazivSastojka.text() == ""):
            return False
        if (self.kolicinaSastojka.text() == ""):
            return False;

        return True

    def provjeriKolicinu(self):
        try:
            float(self.kolicinaSastojka.text())
            return True
        except ValueError:
            return False

    def izbrisiSastojakIzTabele(self):

        rows = self.tabelaSastojaka.selectionModel().selectedRows()
        brojac = 0
        for row in rows:
            if (row.row() == 0):
                continue

            self.tabelaSastojaka.removeRow(row.row() - brojac)
            brojac += 1

    def vecDodatSastojak(self):
        for i in range(0, self.tabelaSastojaka.rowCount()):
            if (self.nazivSastojka.text().upper() == self.tabelaSastojaka.item(i, 0).text().upper()):
                return True
        return False

    def vecDodataStavka(self):
        for i in range(0, self.tabelaOpreme.rowCount()):
            if (self.nazivStavkeOpreme.text().upper() == self.tabelaOpreme.item(i, 0).text().upper()):
                return True
        return False

    def dodajSastojak(self):
        if (self.popunjenaPoljaSastojci() != True):
            ObavestavajucaPoruka("POPUNITE SVA POLJA!")
            return
        if (self.provjeriKolicinu() != True):
            ObavestavajucaPoruka("UNESITE ISKLJUCIVO BROJ ZA KOLICINU")
            return
        if (self.vecDodatSastojak()):
            ObavestavajucaPoruka("Sastojak je vec dodat")
            return
        brojac = self.tabelaSastojaka.rowCount()

        self.tabelaSastojaka.setRowCount(brojac)
        self.tabelaSastojaka.insertRow(brojac)

        self.tabelaSastojaka.setItem(brojac, 0, QTableWidgetItem(self.nazivSastojka.text()))
        self.tabelaSastojaka.setItem(brojac, 2, QTableWidgetItem(self.kolicinaSastojka.text()))
        self.tabelaSastojaka.setItem(brojac, 1, QTableWidgetItem(str(self.combo.currentText())))

    def dodajStavkuOpreme(self):
        if (self.nazivStavkeOpreme.text() == ""):
            ObavestavajucaPoruka("Unesite naziv stavke")
            return
        if (self.vecDodataStavka()):
            ObavestavajucaPoruka("Stavka je vec unijeta")
            return

        brojac = self.tabelaOpreme.rowCount()

        self.tabelaOpreme.setRowCount(brojac)
        self.tabelaOpreme.insertRow(brojac)

        self.tabelaOpreme.setItem(brojac, 0, QTableWidgetItem(self.nazivStavkeOpreme.text()))

    def vratiTipKolicine(self, naziv):
        if naziv == "Gram":
            tipKolicine = TipKolicine.GRAM
        elif naziv == "DL":
            tipKolicine = TipKolicine.DL
        elif naziv == "Komad":
            tipKolicine = TipKolicine.KOMAD
        elif naziv == "Supena kasika":
            tipKolicine = TipKolicine.SUPENAKASIKA
        else:
            tipKolicine = TipKolicine.PRSTOHVAT
        return tipKolicine

    def dodajRecept(self):
        """
        funkcija uzima unijete podatke i poziva funkciju kreirajRecept(self, naziv, putanjaSlike, opis, oprema, kategorije, sastojci)
        s ciljem kreiranja novog recepta
        :return:
        """
        try:
            if (self.popunjenaPoljaRecept() != True):
                ObavestavajucaPoruka("Popunite sva polja!")
                return
            oprema = []
            kategorije = []
            sastojci = {}

            for i in range(1, self.tabelaSastojaka.rowCount()):
                nazivSastojka = self.tabelaSastojaka.item(i, 0).text()
                tipKolicine = self.vratiTipKolicine(self.tabelaSastojaka.item(i, 1).text())

                if (self.menadzerSastojcima.provjeraPostojanjaSastojkaUBazi(nazivSastojka, tipKolicine) == False):

                    self.menadzerSastojcima.kreirajSastojak(nazivSastojka, tipKolicine)

                    sastojak = self.menadzerSastojcima.vratiSastojakPoNazivuITipuKolicine(nazivSastojka, tipKolicine)
                    sastojci[sastojak.sifra] = float(self.tabelaSastojaka.item(i, 2).text())
                else:
                    sastojak = self.menadzerSastojcima.vratiSastojakPoNazivuITipuKolicine(nazivSastojka, tipKolicine)
                    sastojci[sastojak.sifra] = float(self.tabelaSastojaka.item(i, 2).text())

            for i in range(1, self.tabelaOpreme.rowCount()):
                nazivOpreme = self.tabelaOpreme.item(i, 0).text()
                if (self.menadzerOpremom.provjeraPostojanjaOpreme(nazivOpreme) == True):

                    stavka = self.menadzerOpremom.vratiOpremuPoNazivu(nazivOpreme)
                    oprema.append(stavka.sifra)
                else:

                    self.menadzerOpremom.kreirajOpremu(nazivOpreme, "")
                    stavka = self.menadzerOpremom.vratiOpremuPoNazivu(nazivOpreme)
                    oprema.append(stavka.sifra)

            for i in range(1, self.tabelaKategorija.rowCount()):
                nazivKategorije = self.tabelaKategorija.item(i, 0).text()

                if (self.menadzerReceptima.postojanjeKategorije(nazivKategorije) != -1):

                    idKat = self.menadzerReceptima.vratiIdKategorije(nazivKategorije)
                    kategorije.append(idKat)
                else:
                    self.menadzerReceptima.dodajKategoriju(nazivKategorije)
                    kategorija = self.menadzerReceptima.vratiKategoriju(nazivKategorije)
                    kategorije.append(kategorija.id)

            naziv = self.nazivRecepta.text()
            putanjaSlike = self.putanja.text()
            opis = self.informacije.toPlainText()

            self.menadzerReceptima.kreirajRecept(naziv, putanjaSlike, opis, oprema, kategorije, sastojci)
        except:
            traceback.print_exc()

    def izaberiSliku(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '', "")

        if (len(fname[0]) < 4):
            return
        if (fname[0][-4:] == ".jpg"):
            self.putanja.setText(fname[0])
            return
        elif (fname[0][-4:] == ".png"):
            self.putanja.setText(fname[0])
            return

        if (len(fname[0]) < 5):
            return

        if (fname[0][-5:] == ".jpeg"):
            self.putanja.setText(fname[0])
            return
        ObavestavajucaPoruka("Izaberite iskljucivo sliku sa ekstenzijama jpg, png i jpeg")

    def vecDodataKategorija(self):
        for i in range(0, self.tabelaKategorija.rowCount()):
            if (self.kategorijaRecepta.text().upper() == self.tabelaKategorija.item(i, 0).text().upper()):
                return True
        return False

    def dodajKategoriju(self):
        if (self.kategorijaRecepta.text() == ""):
            ObavestavajucaPoruka("Unesite naziv kategorije")
            return

        if (self.vecDodataKategorija()):
            ObavestavajucaPoruka("Kategorija je vec dodata")
            return
        brojac = self.tabelaKategorija.rowCount()

        self.tabelaKategorija.setRowCount(brojac)
        self.tabelaKategorija.insertRow(brojac)

        self.tabelaKategorija.setItem(brojac, 0, QTableWidgetItem(self.kategorijaRecepta.text()))

    def izbrisiStavkuOpremeIzTabele(self):
        rows = self.tabelaOpreme.selectionModel().selectedRows()
        brojac = 0
        for row in rows:
            if (row.row() == 0):
                continue
            self.tabelaOpreme.removeRow(row.row() - brojac)
            brojac += 1

    def izbrisiKategoriju(self):
        rows = self.tabelaKategorija.selectionModel().selectedRows()
        brojac = 0
        for row in rows:
            if (row.row() == 0):
                continue
            self.tabelaKategorija.removeRow(row.row() - brojac)
            brojac += 1

    def initUI(self):
        self.tabelaSastojaka = QTableWidget()
        self.tabelaSastojaka.setColumnCount(3)
        self.tabelaSastojaka.setRowCount(1)

        self.tabelaSastojaka.setItem(0, 0, QTableWidgetItem("Naziv sastojka"))
        self.tabelaSastojaka.setItem(0, 1, QTableWidgetItem("mjerna jedinica"))
        self.tabelaSastojaka.setItem(0, 2, QTableWidgetItem("kolicina"))

        self.tabelaOpreme = QTableWidget()
        self.tabelaOpreme.setColumnCount(1)
        self.tabelaOpreme.setColumnWidth(0, self.tabelaOpreme.width())
        self.tabelaOpreme.setRowCount(1)

        self.tabelaOpreme.setItem(0, 0, QTableWidgetItem("Naziv stavke"))

        self.tabelaKategorija = QTableWidget()
        self.tabelaKategorija.setColumnCount(1)
        self.tabelaKategorija.setColumnWidth(0, self.tabelaKategorija.width())
        self.tabelaKategorija.setRowCount(1)

        self.tabelaKategorija.setItem(0, 0, QTableWidgetItem("Naziv kategorije"))

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Informacije o receptu', '', '', '',
                 '*', '', '', '',
                 '', '', '', '',
                 'Naziv recepta', '^', '', '',
                 '..', '', '', '',
                 '..', '', '', '',
                 'Kategorija recepta', '^^', '', '',
                 '**', '', '', '',  # dodaj kategoriju
                 '***', '', '', '',
                 '****', '', '', '',
                 '..', '', '', '',
                 '..', '', '', '',

                 'Naziv sastojka', '^^^', '', '',
                 'mjerna jedinica', '!', '', '',
                 'kolicina', '^^^^', '', '',
                 '/', '', '', '',  # dugme dodaj sastojak

                 '!!', '', '', '',  # tabela sa pregledom svih sastojaka
                 '$$', '', '', '',
                 '..', '', '', '',
                 '..', '', '', '',
                 'Naziv stavke opreme', '^^^^^', '', '',
                 '#', '', '', '',  # dodaj alat
                 '##', '', '', '',  # pregled svih potrebnih alata,tj tabela
                 '$$$', '', '', '',
                 '..', '', '', '',
                 '..', '', '', '',
                 '//', '^^^^^^', '', '',  # dodaj sliku recepta
                 '$', '', '', ''

                 ]

        self.combo = QComboBox(self)
        self.combo.addItem("Gram")
        self.combo.addItem("DL")
        self.combo.addItem("Komad")
        self.combo.addItem("Supena kasika")
        self.combo.addItem("Prstohvat")

        image = QImage('..\slike\kreiranjeReceptaIkonica.jpg')
        image2 = QImage('..\slike\bijelaPozadina.jfif')
        sImage = image.scaled(QSize(650, 420))
        sImage2 = image2.scaled((QSize(1000, 1000)))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Window, QBrush(sImage2))
        self.setModal(True)
        sadrzaj = ""
        with open("..\slike\stajlKreiranjeRecepta.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)
        positions = [(i, j) for i in range(28) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            if name == '*':
                self.informacije = QPlainTextEdit()
                self.informacije.setToolTip(
                    "Ovde bi trebalo da se nalazi uputstvo za pripremanje i jos neke bitne informacije vezano za recept")
                grid.addWidget(self.informacije, *position)
            elif name == '**':
                self.dodajKategorijuBtn = QPushButton("Dodaj kategoriju")
                self.dodajKategorijuBtn.clicked.connect(self.dodajKategoriju)
                grid.addWidget(self.dodajKategorijuBtn, *position)


            elif name == '***':
                grid.addWidget(self.tabelaKategorija, *position)
            elif name == '****':
                self.izbrisiKategorijuBtn = QPushButton("Izbrisi kategoriju")
                self.izbrisiKategorijuBtn.clicked.connect(self.izbrisiKategoriju)
                grid.addWidget(self.izbrisiKategorijuBtn, *position)
            elif name == "..":
                grid.addWidget(QLabel(""), *position)
            elif name == '^':
                self.nazivRecepta = QLineEdit()
                self.nazivRecepta.setFixedSize(250, 25)
                grid.addWidget(self.nazivRecepta, *position)
            elif name == '^^':
                self.kategorijaRecepta = QLineEdit()
                self.kategorijaRecepta.setFixedSize(250, 25)
                grid.addWidget(self.kategorijaRecepta, *position)
            elif name == '^^^':
                self.nazivSastojka = QLineEdit()
                self.nazivSastojka.setFixedSize(250, 25)
                grid.addWidget(self.nazivSastojka, *position)
            elif name == '^^^^':
                self.kolicinaSastojka = QLineEdit()
                self.kolicinaSastojka.setFixedSize(250, 25)
                grid.addWidget(self.kolicinaSastojka, *position)
            elif name == '^^^^^':
                self.nazivStavkeOpreme = QLineEdit()
                self.nazivStavkeOpreme.setFixedSize(250, 25)
                grid.addWidget(self.nazivStavkeOpreme, *position)
            elif name == '^^^^^^':
                self.putanja = QLineEdit()
                self.putanja.setEnabled(False)
                grid.addWidget(self.putanja, *position)
            elif name == '!':
                grid.addWidget(self.combo, *position)
            elif name == '/':
                dugme = QPushButton("Dodaj sastojak")
                dugme.clicked.connect(self.dodajSastojak)
                dugme.setFixedWidth(200)

                grid.addWidget(dugme, *position)
            elif name == '#':
                self.stavkaOpremeBtn = QPushButton("Dodaj  stavku opreme")
                self.stavkaOpremeBtn.setFixedWidth(200)
                self.stavkaOpremeBtn.clicked.connect(self.dodajStavkuOpreme)
                grid.addWidget(self.stavkaOpremeBtn, *position)
            elif name == '!!':
                grid.addWidget(self.tabelaSastojaka, *position)


            elif name == '##':
                grid.addWidget(self.tabelaOpreme, *position)
            elif name == '$':
                self.dodajReceptBtn = QPushButton("Dodaj recept")
                self.dodajReceptBtn.clicked.connect(self.dodajRecept)
                self.dodajReceptBtn.setFixedWidth(200)
                grid.addWidget(self.dodajReceptBtn, *position)
            elif name == '//':
                self.dodajSliku = QPushButton("Dodaj sliku recepta")
                self.dodajSliku.setFixedWidth(200)
                self.putanjaSlike = ""
                self.dodajSliku.clicked.connect(self.izaberiSliku)

                grid.addWidget(self.dodajSliku, *position)
            elif name == "$$":
                self.izbrisiSastojak = QPushButton("Izbrisi sastojak")
                self.izbrisiSastojak.setFixedWidth(200)
                self.izbrisiSastojak.clicked.connect(self.izbrisiSastojakIzTabele)
                grid.addWidget(self.izbrisiSastojak, *position)
            elif name == "$$$":
                self.izbrisiStavkuOpreme = QPushButton("Izbrisi stavku")
                self.izbrisiStavkuOpreme.clicked.connect(self.izbrisiStavkuOpremeIzTabele)
                self.izbrisiStavkuOpreme.setFixedWidth(200)
                grid.addWidget(self.izbrisiStavkuOpreme, *position)

            else:
                button = QLabel(name)
                grid.addWidget(button, *position)

        self.widget = QWidget()
        self.widget.setPalette(palette)
        self.widget.setLayout(grid)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.widget)
        self.izgled = QHBoxLayout()
        self.izgled.addWidget(self.scroll)
        self.scroll.setPalette(palette2)
        self.setPalette(palette2)
        self.setLayout(self.izgled)
        self.setFixedWidth(700)
        self.setFixedHeight(600)

        self.move(300, 150)
        self.setWindowTitle('Dodavanje recepata')
        self.show()
