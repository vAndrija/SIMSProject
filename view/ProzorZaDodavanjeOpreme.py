from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ProzorZaDodavanjeOpreme(QDialog):
    def __init__(self):
        super().__init__()
        self.opremaMenadzer = QApplication.instance().actionManager.opremaMenadzer
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        ikonica = QIcon('..\slike\ikonica.png')
        self.setWindowIcon(ikonica)
        self.setFixedSize(900,900)
        image = QImage("..\slike\oprema.jpg")
        sImage = image.scaled(QSize(900, 900))
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
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = [
                   '', '','Izaberite opremu:',
                   '', '', '*',
                   '', '', '?',
                   '', '','Dodajte novi aparat:',
                   '', '','Unesite ime:',
                   '', '', '-',
                   '', '', 'Unesite marku:',
                   '', '', '/',
                   '', '', '+',
                   '', '', '!',
                   '', '', '#',
                   '', '', '',
                    '', '', '',
                    '', '', '',
                   ]

        pozicije = [(i, j) for i in range(14) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):
            if sadrzaj == "-":
                self.nazivOpreme = QLineEdit()
                self.nazivOpreme.setFixedSize(250,25)
                grid.addWidget(self.nazivOpreme, *pozicija)
            elif sadrzaj == "*":
                self.postojecaOprema = QTableWidget()
                self.postojecaOprema.setColumnCount(3)
                self.postojecaOprema.setRowCount(1)
                self.postojecaOprema.setColumnWidth(0, 120)
                self.postojecaOprema.setColumnWidth(1,219)
                self.postojecaOprema.setColumnWidth(2, 140)
                bold = QFont()
                bold.setBold(True)
                item = QTableWidgetItem("Naziv aparata")
                item.setFont(bold)
                item.setTextAlignment(Qt.AlignCenter)
                item1 = QTableWidgetItem("Naziv marke")
                item1.setFont(bold)
                item1.setTextAlignment(Qt.AlignCenter)
                item2 = QTableWidgetItem("Sifra")
                item2.setFont(bold)
                item2.setTextAlignment(Qt.AlignCenter)
                self.postojecaOprema.setItem(0,0, item2)
                self.postojecaOprema.setItem(0,1, item)
                self.postojecaOprema.setItem(0,2, item1)
                self.postojecaOprema.setFixedSize(550, 165)
                grid.addWidget(self.postojecaOprema, *pozicija)
            elif sadrzaj == "?":
                dugme = QPushButton("Dodaj aparat")
                dugme.setFixedSize(250, 30)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                self.nazivMarke = QLineEdit()
                self.nazivMarke.setFixedSize(250,25)
                grid.addWidget(self.nazivMarke, *pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Dodaj aparat")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.dodajNoviAparat)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "!":
                self.dodataOprema = QTableWidget()
                self.dodataOprema.setColumnCount(3)
                self.dodataOprema.setRowCount(1)
                self.dodataOprema.setColumnWidth(0, 120)
                self.dodataOprema.setColumnWidth(1,219)
                self.dodataOprema.setColumnWidth(2, 140)

                bold = QFont()
                bold.setBold(True)
                item = QTableWidgetItem("Naziv aparata")
                item.setFont(bold)
                item.setTextAlignment(Qt.AlignCenter)
                item1 = QTableWidgetItem("Naziv marke")
                item1.setFont(bold)
                item1.setTextAlignment(Qt.AlignCenter)

                item2 = QTableWidgetItem("Sifra")
                item2.setFont(bold)
                item2.setTextAlignment(Qt.AlignCenter)

                self.dodataOprema.setItem(0,0, item2)
                self.dodataOprema.setItem(0,1, item)
                self.dodataOprema.setItem(0,2, item1)
                self.dodataOprema.setFixedSize(550, 165)
                grid.addWidget(self.dodataOprema, *pozicija)
            elif sadrzaj == "#":
                dugme = QPushButton("Zavrsi dodavanje")
                dugme.setFixedSize(250,30)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(100,35)
                grid.addWidget(labela, *pozicija)


    def dodajNoviAparat(self):
        naziv = self.nazivOpreme.text()
        marka = self.nazivMarke.text()

        oprema = self.opremaMenadzer.kreirajOpremu(naziv, marka)

