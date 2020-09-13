from controller.osnovneFunkcije import *
from view.ObavestavajucaPoruka import *
from view.Tabela import *


class PrikazInformacijaKuvara(QDialog):
    def __init__(self, korisnik, parent):
        super().__init__()
        self.parent = parent
        self.korisnik = korisnik
        self.initUI()
        self.inicijalizujGrid()

        self.exec_()

    def initUI(self):
        self.setWindowTitle("Prikaz profila")
        self.setFixedSize(800, 800)
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

    def inicijalizujGrid(self):
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = ['Ime:', '1', '',
                   'Prezime:', '2', '',
                   'Korisnicko ime:', '3', '',
                   'Azurirajte korisnicko ime:', '/', '',
                   'Mejl:', '4', '',
                   'Datum rodjenja:', '5', '',
                   'Adresa:', '6', '',
                   'Naziv mesta:', '7', '',
                   'Azurirajte naziv mesta:', '*', '',
                   'Postanski broj:', '8', '',
                   'Azurirajte postanski broj:', '-', '',
                   'Pol:', '9', '',
                   'Dugotrajni sastojci:', '', '',
                   '', '10', '',
                   'Dugotrajna oprema:', '', '',
                   '', '11', '',
                   '', '12', '',
                   '', '13', '',
                   ]

        pozicije = [(i, j) for i in range(18) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "1":
                labela = QLabel(self.korisnik.ime)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "2":
                labela = QLabel(self.korisnik.prezime)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "3":
                self.kIme = QLabel(self.korisnik.korisnickoIme)
                self.kIme.setFixedSize(170, 20)
                grid.addWidget(self.kIme, *pozicija)
            elif sadrzaj == "4":
                labela = QLabel(self.korisnik.mejl)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "5":
                labela = QLabel(self.korisnik.datumRodjenja)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "6":
                labela = QLabel(self.korisnik.adresa)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "7":
                self.mesto = QLabel(self.korisnik.mesto.nazivMesta)
                self.mesto.setFixedSize(170, 20)
                grid.addWidget(self.mesto, *pozicija)
            elif sadrzaj == "8":
                self.postanskiBr = QLabel(self.korisnik.mesto.postanskiBroj)
                self.postanskiBr.setFixedSize(170, 20)
                grid.addWidget(self.postanskiBr, *pozicija)
            elif sadrzaj == "9":
                if self.korisnik.pol == 0:
                    pol = "Zenski"
                else:
                    pol = "Muski"
                labela = QLabel(pol)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "10":
                sastojci = self.korisnik.dugotrajniSastojci
                sviSastojci = nadjiSastojke(sastojci)
                self.postojeciSastojci = Tabela(len(sviSastojci) + 1, 3)
                self.postojeciSastojci.dodajZaglavlja(["Sifra", "Naziv sastojka", "Tip kolicine"])
                self.postojeciSastojci.setColumnWidth(0, 120)
                self.postojeciSastojci.setColumnWidth(1, 219)
                self.postojeciSastojci.setColumnWidth(2, 140)
                brojac = 1
                for sastojak in sviSastojci:
                    self.postojeciSastojci.setItem(brojac, 0, QTableWidgetItem(str(sastojak.sifra)))
                    self.postojeciSastojci.setItem(brojac, 1, QTableWidgetItem(sastojak.naziv))
                    self.postojeciSastojci.setItem(brojac, 2, QTableWidgetItem(str(sastojak.tipKolicine)))
                    brojac += 1
                self.postojeciSastojci.setFixedSize(522, 165)
                grid.addWidget(self.postojeciSastojci, *pozicija)
            elif sadrzaj == "11":
                oprema = self.korisnik.oprema
                svaOprema = nadjiOpremu(oprema)
                tabela = Tabela(len(svaOprema) + 1, 3)
                tabela.dodajZaglavlja(["Sifra", "Naziv", "Naziv marke"])
                tabela.setColumnWidth(0, 120)
                tabela.setColumnWidth(1, 219)
                tabela.setColumnWidth(2, 140)

                brojac = 1
                for aparat in svaOprema:
                    tabela.setItem(brojac, 0, QTableWidgetItem(str(aparat.sifra)))
                    tabela.setItem(brojac, 1, QTableWidgetItem(aparat.naziv))
                    tabela.setItem(brojac, 2, QTableWidgetItem(aparat.marka))
                    brojac += 1

                tabela.setFixedSize(522, 165)
                grid.addWidget(tabela, *pozicija)
            elif sadrzaj == "12":
                dugme = QPushButton("Azuriraj nalog")
                dugme.clicked.connect(self.azurirajNalog)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "13":
                dugme = QPushButton("Obrisi nalog")
                dugme.clicked.connect(self.obrisiNalog)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                self.novoKIme = QLineEdit()
                self.novoKIme.setFixedWidth(170)
                self.novoKIme.setText(self.korisnik.korisnickoIme)
                grid.addWidget(self.novoKIme, *pozicija)
            elif sadrzaj == "*":
                self.novoMesto = QLineEdit()
                self.novoMesto.setFixedWidth(170)
                self.novoMesto.setText(self.korisnik.mesto.nazivMesta)
                grid.addWidget(self.novoMesto, *pozicija)
            elif sadrzaj == "-":
                self.noviPostanskiBr = QLineEdit()
                self.noviPostanskiBr.setFixedWidth(170)
                self.noviPostanskiBr.setText(self.korisnik.mesto.postanskiBroj)
                grid.addWidget(self.noviPostanskiBr, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(160, 20)
                grid.addWidget(labela, *pozicija)

    def azurirajNalog(self):
        if self.novoKIme.text() == "" and self.novoMesto.text() == "" and self.noviPostanskiBr.text() == "":
            ObavestavajucaPoruka("Niste uneli nove podatke.")
        else:
            if self.novoKIme.text() != "":
                staroKorisnicko = self.korisnik.korisnickoIme
                self.korisnik.korisnickoIme = self.novoKIme.text()
                self.kIme.setText(self.novoKIme.text())
                self.korisnik.azurirajHtmlDokument(staroKorisnicko)
                # QApplication.instance().actionManager.informacije.azurirajHtmlDokument(self.korisnik, staroKorisnicko)

            if self.novoMesto.text() != "":
                self.korisnik.mesto.nazivMesta = self.novoMesto.text()
                self.mesto.setText(self.novoMesto.text())

            if self.noviPostanskiBr.text() != "":
                self.korisnik.mesto.postanskiBroj = self.noviPostanskiBr.text()
                self.postanskiBr.setText(self.noviPostanskiBr.text())

            QApplication.instance().actionManager.informacije.upisiKorisnika()
            # QApplication.instance().actionManager.informacije.citanjeKorisnika()
            self.parent.refresujStranu()
            # mozda obrisati liniju ispod
            self.hide()

    def obrisiNalog(self):
        potvrda = QMessageBox
        odgovor = potvrda.question(self, '', "Da li ste sigurni da zelite da obrisete nalog?", potvrda.Yes | potvrda.No)
        if odgovor == potvrda.Yes:
            QApplication.instance().actionManager.informacije.obrisiKuvara(self.korisnik)
            QApplication.instance().actionManager.informacije.upisiKorisnika()
            self.parent.refresujStranu()
            self.hide()
