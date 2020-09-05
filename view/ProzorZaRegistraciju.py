# Kreiran prozor za registraciju, potrebno preuzeti informacije iz widgeta

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
from PyQt5.QtCore import *
from view.ProzorZaDodavanjeSastojaka import *
from view.ProzorZaDodavanjeOpreme import *
from view.ObavestavajucaPoruka import *


class ProzorZaRegistraciju(QDialog):
    def __init__(self):
        super().__init__()
        self.dugotrajniSastojci = []
        self.dugotrajnaOprema = []
        self.initUI()

    def initUI(self):
        """
        Funkcija koja se definise izgled prozora za registraciju novog korisnika aplikacije.
        :return:
        """
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

        self.grid = QGridLayout()
        self.setLayout(self.grid)

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
                 '', '', '', '',
                   '', '', '', '',
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
                self.grid.addWidget(tekst, *pozicija)
            elif sadrzaj == "*":
                comboBox = QComboBox()
                comboBox.addItem("Zenski")
                comboBox.addItem("Muski")
                self.pol = comboBox
                self.grid.addWidget(comboBox, *pozicija)
            elif sadrzaj == '/':
                datum = QDateEdit(calendarPopup = True)
                datum.setDateTime(QDateTime.currentDateTime())
                self.datum = datum
                self.grid.addWidget(datum,*pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(200,60)
                self.grid.addWidget(labela, *pozicija)

        self.dodajOpremuISastojke()
        self.dodajDugmeRegistracije()



        self.exec()

    def dodajOpremuISastojke(self):
        self.dugmeSastojci = QPushButton("Izaberite sastojke")
        self.dugmeSastojci.setFixedSize(250, 30)
        self.dugmeSastojci.clicked.connect(self.dodavanjeSastojaka)
        self.grid.addWidget(self.dugmeSastojci, 11, 2)

        self.dugmeOprema = QPushButton("Izaberite opremu")
        self.dugmeOprema.setFixedSize(250, 30)
        self.dugmeOprema.clicked.connect(self.dodavanjeOpremen)
        self.grid.addWidget(self.dugmeOprema, 11, 3)

    def dodajDugmeRegistracije(self):
        dugme = QPushButton("Registrujte se")
        dugme.setFixedSize(250, 30)
        dugme.clicked.connect(self.registracija)
        self.grid.addWidget(dugme, 12, 3)

    def registracija(self):
        """
        Funkcija koja preuzima podatke koje je korisnik uneo i kreira novog korisnika aplikacije.
        :return:
        """

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
        if ime == "" or prezime == "" or kIme == "" or lozinka == "" or mejl == "" or adresa == "" or mesto == "" or ppt == "":
            ObavestavajucaPoruka("Niste popunili sva polja.")
        else:
            if lozinka != ponovnaLozinka:
                ObavestavajucaPoruka("Vasa lozinka nije ispravna.")
            self.registrovaniKorisnik = QApplication.instance().actionManager.informacije.kreirajKorisnika(ime,prezime,kIme,lozinka,mejl,str(datum),adresa,mesto,ppt,pol,
                                                                                          self.dugotrajniSastojci, self.dugotrajnaOprema, [], 0, 0, [], [])
            self.hide()


    def dodavanjeSastojaka(self):
        """
        Funkcija koja se poziva kada korisnik pritisne dugme 'Dodaj sastojke'. Prikazuje se prozor za dodavanje
        dugotrajnih sastojaka.
        :return:
        """
        prozor = ProzorZaDodavanjeSastojaka()
        self.setWindowModality(Qt.WindowModal)
        self.dugotrajniSastojci = prozor.dodatiUTabelu

    def dodavanjeOpremen(self):
        """
        Funkcija koja se pozica kada korisnik pritisne dugme 'Dodaj opremu'. Prikazuje se prozor za dodavanje opreme.
        :return:
        """
        prozor = ProzorZaDodavanjeOpreme()
        self.setWindowModality(Qt.WindowModal)
        self.dugotrajnaOprema = prozor.dodatiUTabelu

