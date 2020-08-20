#Kreiran prozor za pretragu recepata

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import traceback

class ProzorZaPretragu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.setFixedSize(800, 600)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        image = QImage("..\slike\pretraga.jpg")
        sImage = image.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

        grid = QGridLayout()
        self.setLayout(grid)

        matrica = ["List","","",
                   "Unos kategorije", "kat", "dodaj",
                   "Naziv recepta", "naziv", "",
                   "brisanje", "", "",
                   "Rezultat pretrage: ", "", ""
                   "", "", "",
                   "", "", "",
                   "",
                   "refresh", "", ""
                   ]



        pozicije = [(i, j) for i in range(9) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "List":
                self.lista = QTreeWidget()
                self.lista.setColumnCount(2)
                self.lista.setHeaderLabels(['Brisanje', 'Kategorija'])
                self.lista.setFixedSize(400, 120)

                grid.addWidget(self.lista, *pozicija)
            elif sadrzaj == "dodaj":
                dugme = QPushButton("Dodaj kategoriju")
                dugme.setFixedSize(250, 30)
                dugme.clicked.connect(self.dodajKategoriju)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "brisanje":
                dugme = QPushButton("Obrisi oznacene kategorije")
                dugme.setFixedSize(250, 30)
                dugme.clicked.connect(self.ukloniKategorije)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "refresh":
                dugme = QPushButton("Osvezi rezultate")
                dugme.setFixedSize(150, 30)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "kat":
                self.unetaKategorija = QLineEdit()
                self.unetaKategorija.setFixedSize(250, 25)
                grid.addWidget(self.unetaKategorija, *pozicija)
            elif sadrzaj == "naziv":
                self.unetNaziv = QLineEdit()
                self.unetNaziv.setFixedSize(250, 25)
                grid.addWidget(self.unetNaziv, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(200, 30)
                grid.addWidget(labela, *pozicija)

        self.exec()

    def dodajKategoriju(self):
        if(self.unetaKategorija.text() == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Morate uneti kategoriju!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        if(self.lista.topLevelItemCount() != 0):
            for i in range(self.lista.topLevelItemCount()):
                if self.lista.topLevelItem(i).text(1) == self.unetaKategorija.text():
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)

                    msg.setText("Ova kategorija vec postoji!")
                    msg.setWindowTitle("Greska")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec()
                    return

        item = QTreeWidgetItem()
        item.setCheckState(0, Qt.Unchecked)
        item.setText(1, self.unetaKategorija.text())
        self.lista.addTopLevelItem(item)
        self.unetaKategorija.setText(None)

    def ukloniKategorije(self):
        try:
            prolaz = True
            while (prolaz):

                prolaz = False

                for i in range(self.lista.topLevelItemCount()):
                    item = self.lista.topLevelItem(i)
                    if item.checkState(0) == Qt.Checked:
                        self.lista.takeTopLevelItem(i)
                        prolaz = True
                        break

            self.lista.repaint()
        except:
            traceback.print_exc()