from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from view.ObavestavajucaPoruka import *
from model.Administrator import *
from model.Urednik import *

class PrikazInformacijaAdminaIUrednika(QDialog):
    def __init__(self, korisnik):
        super().__init__()
        self.korisnik = korisnik
        self.initUI()
        self.inicijalizujGrid()
        self.exec_()


    def initUI(self):
        self.setWindowTitle("Prikaz profila")
        self.setFixedSize(700,650)
        image = QImage("..\slike\\urednik.jpg")
        sImage = image.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)


    def inicijalizujGrid(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        matrica = ['Ime:', '1', '',
                   'Prezime:', '2', '',
                   'Korisnicko ime:', '3', '',
                   'Mejl:', '4', '',
                   'Datum rodjenja:', '5', '',
                   'Adresa:', '6', '',
                   'Naziv mesta:', '7', '',
                   'Postanski broj:', '8', '',
                   'Pol:', '9', '',
                    '10', '', '']

        pozicije = [(i, j) for i in range(10) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "1":
                self.labelaIme = QLineEdit(self.korisnik.ime)
                self.labelaIme.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaIme, *pozicija)
            elif sadrzaj == "2":
                self.labelaPrezime = QLineEdit(self.korisnik.prezime)
                self.labelaPrezime.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaPrezime, *pozicija)
            elif sadrzaj == "3":
                self.labelaKorisnicko = QLineEdit(self.korisnik.korisnickoIme)
                self.labelaKorisnicko.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaKorisnicko, *pozicija)
            elif sadrzaj == "4":
                self.labelaMejl = QLineEdit(self.korisnik.mejl)
                self.labelaMejl.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaMejl, *pozicija)

            elif sadrzaj == "5":
                self.labelaDatum = QDateEdit(calendarPopup=True)
                self.labelaDatum.setDateTime(QDateTime.fromString(self.korisnik.datumRodjenja,"yyyy-MM-dd"))

                self.labelaDatum.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaDatum, *pozicija)
            elif sadrzaj == "6":
                self.labelaAdresa = QLineEdit(self.korisnik.adresa)
                self.labelaAdresa.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaAdresa, *pozicija)
            elif sadrzaj == "7":
                self.labelaMesto = QLineEdit(self.korisnik.mesto.nazivMesta)
                self.labelaMesto.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaMesto, *pozicija)
            elif sadrzaj == "8":
                self.labelaPostanski = QLineEdit(self.korisnik.mesto.postanskiBroj)
                self.labelaPostanski.setFixedSize(130, 20)
                self.grid.addWidget(self.labelaPostanski, *pozicija)
            elif sadrzaj == "9":
                self.comboBox = QComboBox()
                self.comboBox.addItem("Zenski")
                self.comboBox.addItem("Muski")
                if self.korisnik.pol == 0:
                    self.comboBox.setCurrentIndex(0)
                else:
                    self.comboBox.setCurrentIndex(1)
                self.comboBox.setFixedSize(130, 20)
                self.grid.addWidget(self.comboBox, *pozicija)
            elif sadrzaj == "10":
                dugme = QPushButton("Azuriraj profil")
                dugme.clicked.connect(self.azurirajProfil)
                self.grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(260, 20)
                self.grid.addWidget(labela, *pozicija)

    def azurirajProfil(self):
        try:
            if self.labelaIme.text() == self.korisnik.ime and self.labelaKorisnicko.text() == self.korisnik.korisnickoIme and self.labelaPrezime.text() == self.korisnik.prezime and self.korisnik.datumRodjenja == str(
                self.labelaDatum.date().toPyDate()) and self.labelaAdresa.text() == self.korisnik.adresa and self.labelaMejl.text() == self.korisnik.mejl and self.labelaMesto.text() == self.korisnik.mesto.nazivMesta and self.labelaPostanski.text() == self.korisnik.mesto.postanskiBroj:
                    ObavestavajucaPoruka("Morate naciniti neke promene.")
            else:
                self.korisnik.ime = self.labelaIme.text()
                self.korisnik.prezime = self.labelaPrezime.text()
                self.korisnik.korisnickoIme = self.labelaKorisnicko.text()
                self.korisnik.datumRodjenja = str(self.labelaDatum.date().toPyDate())
                self.korisnik.mesto.nazivMesta = self.labelaMesto.text()
                self.korisnik.adresa = self.labelaAdresa.text()
                self.korisnik.mesto.postanskiBroj = self.labelaPostanski.text()
                self.korisnik.mejl = self.labelaMejl.text()
                if self.comboBox.currentIndex() == 0:
                    self.korisnik.pol = 0
                else:
                    self.korisnik.pol = 1

                if isinstance(self.korisnik, Administrator):
                    QApplication.instance().actionManager.informacije.upisiAdministratora()
                else:
                    QApplication.instance().actionManager.informacije.upisiUrednike()
                self.close()
        except Exception as e:
            print(e)


