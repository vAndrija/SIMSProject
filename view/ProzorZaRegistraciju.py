# Kreiran prozor za registraciju, potrebno preuzeti informacije iz widgeta

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
from PyQt5.QtCore import *
from src.view.ProzorZaDodavanjeSastojaka import *


class ProzorZaRegistraciju(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.setFixedSize(1000,800)
        image = QImage("..\slike\zaRegistraciju.jpg")
        sImage = image.scaled(QSize(1000, 800))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

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

        self.tekstovi = []
        self.pol = None
        self.datum = None

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "-":
                tekst = QLineEdit()
                tekst.setFixedSize(250,25)
                self.tekstovi.append(tekst)
                grid.addWidget(tekst, *pozicija)
            elif sadrzaj == "*":
                comboBox = QComboBox()
                comboBox.addItem("Zenski")
                comboBox.addItem("Muski")
                self.pol = comboBox
                grid.addWidget(comboBox, *pozicija)
            elif sadrzaj == '/':
                datum = QDateEdit(calendarPopup = True)
                datum.setDateTime(QDateTime.currentDateTime())
                self.datum = datum
                grid.addWidget(datum,*pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Izaberite sastojke")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.dodavanjeSastojaka)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == ")":
                dugme = QPushButton("Izaberite opremu")
                dugme.setFixedSize(250,30)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "(":
                dugme = QPushButton("Registrujte se")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.registracija)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(200,60)
                grid.addWidget(labela, *pozicija)



        self.exec()

    def registracija(self):
        ime = self.tekstovi[0].text()
        prezime = self.tekstovi[1].text()
        kIme = self.tekstovi[2].text()
        lozinka = self.tekstovi[3].text()
        ponovnaLozinka = self.tekstovi[4].text()
        mejl = self.tekstovi[5].text()
        adresa = self.tekstovi[6].text()
        mesto = self.tekstovi[7].text()
        ppt = self.tekstovi[8].text()
        pol = self.pol.currentIndex()
        datum = self.datum.date().toPyDate()
        if lozinka != ponovnaLozinka:
            poruka = QMessageBox()
            poruka.setWindowTitle("Aplikacija za kuvare pocetnike")
            icon = QIcon("..\slike\ikonica.png")
            poruka.setWindowIcon(icon)
            poruka.setText("Vasa lozinka nije ispravna.")
            poruka.exec_()
        elif ime == "" or prezime == "" or kIme == "" or lozinka == "" or mejl == "" or adresa == "" or mesto == "" or ppt == "":
            poruka = QMessageBox()
            poruka.setWindowTitle("Aplikacija za kuvare pocetnike")
            icon = QIcon("..\slike\ikonica.png")
            poruka.setWindowIcon(icon)
            poruka.setText("Niste popunili sva polja.")
            poruka.exec_()
        else:
            korisnik = QApplication.instance().actionManager.informacije.kreirajKorisnika(ime,prezime,kIme,lozinka,mejl,str(datum),adresa,mesto,ppt,pol)


    def dodavanjeSastojaka(self):
        prozor = ProzorZaDodavanjeSastojaka()