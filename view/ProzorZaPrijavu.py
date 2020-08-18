#Kreiran prozor koji se prikazuje prilikom prijavljivanja

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
from PyQt5.QtCore import QSize
from view.ProzorZaRegistraciju import *

class ProzorZaPrijavu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.setFixedSize(800,600)
        image = QImage("..\slike\prijava.jpg")
        sImage = image.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)

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
                 '', '*', '',
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
                tekst = QLineEdit()
                grid.addWidget(tekst, *pozicija)
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
        prozor = ProzorZaRegistraciju()

    def prijava(self):
        pass


