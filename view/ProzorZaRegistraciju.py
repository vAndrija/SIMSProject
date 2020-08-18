# Kreiran prozor za registraciju, potrebno preuzeti informacije iz widgeta

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
from PyQt5.QtCore import *

class ProzorZaRegistraciju(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.setFixedSize(1000,800)
        image = QImage("..\slike\zaRegistraciju.jpg")
        sImage = image.scaled(QSize(1000, 800))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)

        grid = QGridLayout()
        self.setLayout(grid)

        matrica = ['', '', 'Unesite ime:', '-',
                 '', '', 'Unesite prezime:', '-',
                 '', '', 'Unesite korisnicko ime:', '-',
                 '', '', 'Unesite lozinku:', '-',
                 '', '', 'Ponovo unesite lozinku:', '-',
                 '', '', 'Unesite mejl:', '-',
                 '', '', 'Unesite datumRodjenja:', '/',
                 '', '', 'Unesite adresu:', '-',
                 '', '', 'Unesite mesto:', '-',
                 '', '', 'Unesite postanski broj:', '-',
                 '', '', 'Izaberite pol:', '*',
                 '', '', '+', ')',
                   '', '', '', '(',
                 ]

        pozicije = [(i, j) for i in range(13) for j in range(4)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "-":
                tekst = QLineEdit()
                tekst.setFixedSize(250,25)
                grid.addWidget(tekst, *pozicija)
            elif sadrzaj == "*":
                # list = QListWidget()
                # item = QListWidgetItem("Muski")
                # item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                # item.setCheckState(Qt.Unchecked)
                # list.addItem(item)
                # item1 = QListWidgetItem("Zenski")
                # item1.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                # item1.setCheckState(Qt.Unchecked)
                # list.addItem(item1)
                # grid.addWidget(list)
                comboBox = QComboBox()
                comboBox.addItem("Zenski")
                comboBox.addItem("Muski")
                grid.addWidget(comboBox, *pozicija)
            elif sadrzaj == '/':
                datum = QDateEdit(calendarPopup = True)
                datum.setDateTime(QDateTime.currentDateTime())
                grid.addWidget(datum,*pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Izaberite sastojke")
                dugme.setFixedSize(250,30)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == ")":
                dugme = QPushButton("Izaberite opremu")
                dugme.setFixedSize(250,30)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "(":
                dugme = QPushButton("Registrujte se")
                dugme.setFixedSize(250,30)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(200,100)
                grid.addWidget(labela, *pozicija)



        self.exec()