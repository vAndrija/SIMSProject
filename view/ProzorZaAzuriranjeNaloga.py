from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view.ObavestavajucaPoruka import *
from  controller.osnovneFunkcije import *

class ProzorZaAzuriranjeNaloga(QDialog):
    def __init__(self, korisnik):
        super().__init__()
        self.korisnik = korisnik
        self.initUI()
        self.initGrid()
        self.exec_()

    def initUI(self):
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.setFixedSize(650,550)
        image = QImage("..\slike\profil.jpg")
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


    def initGrid(self):
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = [ '', '', '',
                    'Trenutno korisnicko ime:', '', '',
                    '1', '', '',
                    'Unesite novo korisnicko ime:', '', '',
                  '2', '', '',
                  'Trenutni naziv mesta prebivalista:', '', '',
                    '3', '', '',
                  'Unesite novi naziv mesta prebivalista:', '', '',
                  '4', '', '',
                  'Trenutni postanski broj mesta prebivalista:', '', '',
                    '5', '', '',
                  'Unesite novi postanski broj mesta prebivalista:', '', '',
                  '6', '', '',
                  '', '*', '',
                 ]

        pozicije = [(i, j) for i in range(14) for j in range(3)]


        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "1":
                italic = QFont()
                italic.setItalic(True)
                labela = QLabel(self.korisnik.korisnickoIme)
                labela.setFont(italic)
                labela.setFixedSize(130, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "2":
                self.novoKorisnicko = QLineEdit()
                grid.addWidget(self.novoKorisnicko, *pozicija)
            elif sadrzaj == "3":
                italic = QFont()
                italic.setItalic(True)
                labela = QLabel(self.korisnik.mesto.nazivMesta)
                labela.setFont(italic)
                labela.setFixedSize(130,20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "4":
                self.noviNazivMesta = QLineEdit()
                grid.addWidget(self.noviNazivMesta, *pozicija)
            elif sadrzaj == "5":
                italic = QFont()
                italic.setItalic(True)
                labela = QLabel(self.korisnik.mesto.postanskiBroj)
                labela.setFont(italic)
                labela.setFixedSize(130,20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "6":
                self.noviPostanskiBroj = QLineEdit()
                grid.addWidget(self.noviPostanskiBroj, *pozicija)
            elif sadrzaj == "*":
                dugme = QPushButton("Azuriraj")
                dugme.clicked.connect(self.azuriranjeNaloga)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(270, 20)
                grid.addWidget(labela, *pozicija)


    def azuriranjeNaloga(self):
        provera = False
        staroKorisnicko = self.korisnik.korisnickoIme
        if self.novoKorisnicko.text() != "":
            self.korisnik.korisnickoIme = self.novoKorisnicko.text()
            provera = True
        if self.noviNazivMesta.text() != "":
            provera = True
            self.korisnik.mesto.nazivMesta = self.noviNazivMesta.text()
        if self.noviPostanskiBroj.text() != "":
            self.korisnik.mesto.postanskiBroj = self.noviPostanskiBroj.text()
            provera = True
        if provera == False:
            ObavestavajucaPoruka("Morate uneti nove podatke da biste azurirali nalog.")
        else:
            azurirajKuvara(staroKorisnicko, self.korisnik)
            self.hide()


