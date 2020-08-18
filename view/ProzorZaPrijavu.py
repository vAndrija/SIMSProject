#Kreiran prozor koji se prikazuje prilikom prijavljivanja

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
from PyQt5.QtCore import QSize

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

        labela1 = QLabel("Unesite korisnicko ime:", self)
        labela1.setFont(QFont("Times", 10, QFont.Bold))
        labela1.move(330,200)

        tekst1 = QLineEdit(self)
        tekst1.move(340,220)

        labela2 = QLabel("Unesite lozinku:", self)
        labela2.setFont(QFont("Times", 10, QFont.Bold))
        labela2.move(350, 250)

        tekst2 = QLineEdit(self)
        tekst2.move(340, 270)

        dugme1 = QPushButton("Prijavite se", self)
        dugme1.move(360,300)
        dugme1.setStyleSheet("background-color: beige")

        dugme2 = QPushButton("Registrujte se", self)
        dugme2.move(360,400)
        dugme2.setStyleSheet("background-color: beige")




        self.show()