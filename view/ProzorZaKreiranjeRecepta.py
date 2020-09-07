from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QLineEdit, QComboBox, QLabel, QPlainTextEdit, QTableWidget,
                             QTableWidgetItem, QScrollArea, QMainWindow, QFileDialog, QAbstractItemView)
from enum import Enum

from src.view.ObavjestavajucaPoruka import ObavjestavajucaPoruka


class QStringList(object):
    pass


class ProzorZaKreiranjeRecepta(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def popunjenaPoljaRecept(self):
        if(self.nazivRecepta.text() == ""):
            return False;
        if(self.putanja.text() == ""):
            return False;

        if(self.informacije.toPlainText() == ""):
            return False
        if(self.tabelaSastojaka.rowCount() <= 1):
            return False
        if(self.tabelaKategorija.rowCount() <= 1):
            return False

        print(self.tabelaKategorija.rowCount())
        return True
    def popunjenaPoljaSastojci(self):
        if(self.nazivSastojka.text() == ""):
            return False
        if(self.kolicinaSastojka.text() == ""):
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
            if(row.row() == 0):
                continue

            self.tabelaSastojaka.removeRow(row.row() - brojac)
            brojac += 1
    def vecDodatSastojak(self):
        for i in range(1,self.tabelaSastojaka.rowCount()):
            if(self.nazivSastojka.text().upper() == self.tabelaSastojaka.item(i,1).text().upper()):
                return True
        return False
    def vecDodataStavka(self):
        for i in range(1,self.tabelaOpreme.rowCount()):
            if(self.nazivStavkeOpreme.text().upper() == self.tabelaOpreme.item(i,1).text().upper()):
                return True
        return False
    def dodajSastojak(self):
        if(self.popunjenaPoljaSastojci() != True):
            ObavjestavajucaPoruka("POPUNITE SVA POLJA!")
            return
        if(self.provjeriKolicinu() != True):
            ObavjestavajucaPoruka("UNESITE ISKLJUCIVO BROJ ZA KOLICINU")
            return
        if(self.vecDodatSastojak()):
            ObavjestavajucaPoruka("Sastojak je vec dodat")
            return
        brojac = self.tabelaSastojaka.rowCount()

        self.tabelaSastojaka.setRowCount(brojac)
        self.tabelaSastojaka.insertRow(brojac)



        self.tabelaSastojaka.setItem(brojac, 0, QTableWidgetItem("DODATI SIFRU KASNIJE"))
        self.tabelaSastojaka.setItem(brojac, 1, QTableWidgetItem(self.nazivSastojka.text()))
        self.tabelaSastojaka.setItem(brojac, 2, QTableWidgetItem(self.kolicinaSastojka.text()))
        self.tabelaSastojaka.setItem(brojac, 3, QTableWidgetItem(str(self.combo.currentText())))

    def dodajStavkuOpreme(self):
        if(self.nazivStavkeOpreme.text() == ""):
            ObavjestavajucaPoruka("Unesite naziv stavke")
            return
        if(self.vecDodataStavka()):
            ObavjestavajucaPoruka("Stavka je vec unijeta")
            return

        brojac = self.tabelaOpreme.rowCount()

        self.tabelaOpreme.setRowCount(brojac)
        self.tabelaOpreme.insertRow(brojac)

        self.tabelaOpreme.setItem(brojac, 0, QTableWidgetItem("DODATI SIFRU KASNIJE"))
        self.tabelaOpreme.setItem(brojac, 1, QTableWidgetItem(self.nazivStavkeOpreme.text()))

    def dodajRecept(self):
        """
        funkcija uzima unijete podatke i poziva funkciju kreirajRecept(self, naziv, putanjaSlike, opis, oprema, kategorije, sastojci)
        s ciljem kreiranja novog recepta
        :return:
        """
        if(self.popunjenaPoljaRecept()!=True):
            ObavjestavajucaPoruka("Popunite sva polja!")
            return



    def izaberiSliku(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '', "")

        if(len(fname[0]) < 4):
            return
        if(fname[0][-4:] == ".jpg"):
            self.putanja.setText(fname[0])
            return
        elif(fname[0][-4:] == ".png"):
            self.putanja.setText(fname[0])
            return


        if(len(fname[0]) < 5):
            return

        if(fname[0][-5:] == ".jpeg"):
            self.putanja.setText(fname[0])
            return
        ObavjestavajucaPoruka("Izaberite iskljucivo sliku sa ekstenzijama jpg, png i jpeg")
    def vecDodataKategorija(self):
        for i in range(1,self.tabelaKategorija.rowCount()):
            if(self.kategorijaRecepta.text().upper() == self.tabelaKategorija.item(i,1).text().upper()):
                return True
        return False
    def dodajKategoriju(self):
        if (self.kategorijaRecepta.text() == ""):
            ObavjestavajucaPoruka("Unesite naziv kategorije")
            return

        if (self.vecDodataKategorija()):
            ObavjestavajucaPoruka("Kategorija je vec dodata")
            return
        brojac = self.tabelaKategorija.rowCount()

        self.tabelaKategorija.setRowCount(brojac)
        self.tabelaKategorija.insertRow(brojac)

        self.tabelaKategorija.setItem(brojac, 0, QTableWidgetItem("DODATI SIFRU KASNIJE"))
        self.tabelaKategorija.setItem(brojac, 1, QTableWidgetItem(self.kategorijaRecepta.text()))


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
        self.tabelaSastojaka.setColumnCount(4)
        self.tabelaSastojaka.setRowCount(1)

        self.tabelaSastojaka.setItem(0, 0, QTableWidgetItem("Sifra"))
        self.tabelaSastojaka.setItem(0, 1, QTableWidgetItem("Naziv sastojka"))
        self.tabelaSastojaka.setItem(0, 2, QTableWidgetItem("mjerna jedinica"))
        self.tabelaSastojaka.setItem(0, 3, QTableWidgetItem("kolicina"))



        self.tabelaOpreme = QTableWidget()
        self.tabelaOpreme.setColumnCount(2)
        self.tabelaOpreme.setRowCount(1)

        self.tabelaOpreme.setItem(0, 0, QTableWidgetItem("Sifra"))
        self.tabelaOpreme.setItem(0, 1, QTableWidgetItem("Naziv stavke"))

        self.tabelaKategorija = QTableWidget()
        self.tabelaKategorija.setColumnCount(2)
        self.tabelaKategorija.setRowCount(1)
        self.tabelaKategorija.setItem(0,0,QTableWidgetItem("Sifra"))
        self.tabelaKategorija.setItem(0,1,QTableWidgetItem("Naziv kategorije"))


        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Informacije o receptu', '', '', '',
                 '*', '', '', '',
                 '', '', '', '',
                 'Naziv recepta','^','','',
                 '..', '', '', '',
                 '..', '', '', '',
                'Kategorija recepta','^^','','',
                 '**','','','',#dodaj kategoriju
                 '***','','','',
                 '****','','','',
                 '..', '', '', '',
                 '..', '', '', '',

                 'Naziv sastojka', '^^^', '', '',
                 'mjerna jedinica', '!', '', '',
                 'kolicina','^^^^','','',
                 '/','','','',#dugme dodaj sastojak

                 '!!','','','',#tabela sa pregledom svih sastojaka
                 '$$','','','',
                 '..', '', '', '',
                 '..', '', '', '',
                 'Naziv stavke opreme','^^^^^','','',
                 '#','','','',#dodaj alat
                 '##','','','',#pregled svih potrebnih alata,tj tabela
                 '$$$','','','',
                 '..', '', '', '',
                 '..', '', '', '',
                 '//','^^^^^^','','', #dodaj sliku recepta
                 '$','','',''

                 ]

        self.combo = QComboBox(self)
        self.combo.addItem("komad")
        self.combo.addItem("gram")
        self.combo.addItem("supena kasika")
        self.combo.addItem("dl")
        self.combo.addItem("prstohvat")

        image = QImage("stajl\\profil.jpg")
        image2 = QImage("stajl\\bela.jfif")
        sImage = image.scaled(QSize(650, 420))
        sImage2 = image2.scaled((QSize(600,450)))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Window, QBrush(sImage2))




        sadrzaj = ""
        with open("stajl/stajlKreiranjeRecepta.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)
        positions = [(i, j) for i in range(28) for j in range(4)]


        for position, name in zip(positions, names):

            if name == '':
                continue
            if name == '*':
                self.informacije = QPlainTextEdit()
                self.informacije.setToolTip("Ovde bi trebalo da se nalazi uputstvo za pripremanje i jos neke bitne informacije vezano za recept")
                grid.addWidget(self.informacije, *position)
            elif name == '**':
                self.dodajKategorijuBtn = QPushButton("Dodaj kategoriju")
                self.dodajKategorijuBtn.clicked.connect(self.dodajKategoriju)
                grid.addWidget(self.dodajKategorijuBtn,*position)


            elif name == '***':
                grid.addWidget(self.tabelaKategorija,*position)
            elif name == '****':
                self.izbrisiKategorijuBtn = QPushButton("Izbrisi kategoriju")
                self.izbrisiKategorijuBtn.clicked.connect(self.izbrisiKategoriju)
                grid.addWidget(self.izbrisiKategorijuBtn,*position)
            elif name == "..":
                grid.addWidget(QLabel(""),*position)
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
                grid.addWidget(self.combo,*position)
            elif name == '/':
                dugme = QPushButton("Dodaj sastojak")
                dugme.clicked.connect(self.dodajSastojak)
                dugme.setFixedWidth(200)

                grid.addWidget(dugme,*position)
            elif name == '#':
                self.stavkaOpremeBtn = QPushButton("Dodaj  stavku opreme")
                self.stavkaOpremeBtn.setFixedWidth(200)
                self.stavkaOpremeBtn.clicked.connect(self.dodajStavkuOpreme)
                grid.addWidget(self.stavkaOpremeBtn,*position)
            elif name == '!!':
                grid.addWidget(self.tabelaSastojaka,*position)


            elif name == '##':
                grid.addWidget(self.tabelaOpreme, *position)
            elif name == '$':
                self.dodajReceptBtn = QPushButton("Dodaj recept")
                self.dodajReceptBtn.clicked.connect(self.dodajRecept)
                self.dodajReceptBtn.setFixedWidth(200)
                grid.addWidget(self.dodajReceptBtn,*position)
            elif name == '//':
                self.dodajSliku = QPushButton("Dodaj sliku recepta")
                self.dodajSliku.setFixedWidth(200)
                self.putanjaSlike = ""
                self.dodajSliku.clicked.connect(self.izaberiSliku)

                grid.addWidget(self.dodajSliku,*position)
            elif name == "$$":
                self.izbrisiSastojak = QPushButton("Izbrisi sastojak")
                self.izbrisiSastojak.setFixedWidth(200)
                self.izbrisiSastojak.clicked.connect(self.izbrisiSastojakIzTabele)
                grid.addWidget(self.izbrisiSastojak, *position)
            elif name == "$$$":
                self.izbrisiStavkuOpreme = QPushButton("Izbrisi stavku")
                self.izbrisiStavkuOpreme.setFixedWidth(200)
                grid.addWidget(self.izbrisiStavkuOpreme,*position)

            else:
                button = QLabel(name)
                grid.addWidget(button, *position)


        self.widget = QWidget()
        self.widget.setPalette(palette)
        self.widget.setLayout(grid)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.scroll.setPalette(palette2)
        self.setFixedWidth(700)
        self.setFixedHeight(600)
        self.move(300, 150)
        self.setWindowTitle('Dodavanje recepata')
        self.show()


class TipKolicine(Enum):
    GRAM = 0
    DL = 1
    KOMAD = 2
    SUPENAKASIKA = 3
    PRSTOHVAT = 4

    def __str__(self):
        return self.name
