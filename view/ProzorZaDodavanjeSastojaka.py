from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from model.TipKolicine import *

class ProzorZaDodavanjeSastojaka(QDialog):
    def __init__(self):
        super().__init__()
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
                tekst = QLineEdit()
                tekst.setFixedSize(250,25)
                grid.addWidget(tekst, *pozicija)
            elif sadrzaj == "*":
                self.postojeciSastojci = QTableWidget()
                self.postojeciSastojci.setColumnCount(2)
                self.postojeciSastojci.setRowCount(1)
                self.postojeciSastojci.setColumnWidth(0, 214)
                self.postojeciSastojci.setColumnWidth(1,214)
                self.postojeciSastojci.setItem(0,0, QTableWidgetItem("Naziv sastojka"))
                self.postojeciSastojci.setItem(0,1, QTableWidgetItem("Tip kolicine sastojka"))
                self.postojeciSastojci.setFixedSize(450, 120)
                grid.addWidget(self.postojeciSastojci, *pozicija)
            elif sadrzaj == "?":
                dugme = QPushButton("Dodaj sastojak")
                dugme.setFixedSize(250, 30)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                comboBox = QComboBox()
                comboBox.addItem('Gram')
                comboBox.addItem('DL')
                comboBox.addItem('Komad')
                comboBox.addItem('Prstohvat')
                comboBox.addItem('Supena kasika')
                grid.addWidget(comboBox, *pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Dodaj sastojak")
                dugme.setFixedSize(250,30)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "!":
                self.dodatiSastojci = QTableWidget()
                self.dodatiSastojci.setColumnCount(2)
                self.dodatiSastojci.setRowCount(1)
                self.dodatiSastojci.setColumnWidth(0, 214)
                self.dodatiSastojci.setColumnWidth(1,214)
                self.dodatiSastojci.setItem(0,0, QTableWidgetItem("Naziv sastojka"))
                self.dodatiSastojci.setItem(0,1, QTableWidgetItem("Tip kolicine sastojka"))
                self.dodatiSastojci.setFixedSize(450, 120)
                grid.addWidget(self.dodatiSastojci, *pozicija)
            elif sadrzaj == "#":
                dugme = QPushButton("Zavrsi dodavanje")
                dugme.setFixedSize(250,30)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(170,35)
                grid.addWidget(labela, *pozicija)

        self.exec_()