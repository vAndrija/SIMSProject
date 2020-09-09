from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from view.Tabela import *
from view.ObavestavajucaPoruka import *

class PrikazReceptaUredniku(QDialog):
    def __init__(self, parent, recept):
        super().__init__(parent)
        self.recept = recept
        self.menadzerSastojci = QApplication.instance().actionManager.sastojciMenadzer
        self.menadzerOprema = QApplication.instance().actionManager.opremaMenadzer
        self.dodateKategorije = []
        try:
            self.initUI()
        except Exception as e:
            print(e)
        self.show()

    def initUI(self):
        self.setWindowTitle("Prikaz recepta")
        self.setModal(True)
        image = QImage("..\slike\slika6.jpg")
        sImage = image.scaled(QSize(1000, 900))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.setFixedSize(1000,900)
        self.izgled = QGridLayout()
        self.setLayout(self.izgled)
        matrica = ['1','','',
                 '3','','2',
                 '6', '', '7',
                 '12', '8', '9',
                 '4','','5',
                   '', '', '',
                  '10', '', '11',
                   ]
        self.selekcije=[]
        pozicije = [(i, j) for i in range(7) for j in range(3)]
        for sadrzaj,pozicija in zip(matrica,pozicije):
            if sadrzaj=='1':
                self.noviNaziv =QTextEdit()
                self.noviNaziv.setText("<h1 style='color:black'><b>{0}<b></h1>".format(self.recept.naziv))
                self.noviNaziv.setFixedSize(300,50)
                self.izgled.addWidget(self.noviNaziv,*pozicija)
            if sadrzaj =='2':
                labela = QLabel()
                labela.setBackgroundRole(True)

                pixmapa = QPixmap('..\dizajn\\'+str(self.recept.id)+"."+str(self.recept.ekstenzijaSlike))
                pixmapa.scaled(350,350)
                labela.setPixmap(pixmapa)
                labela.setFixedSize(350,350)
                self.izgled.addWidget(labela,*pozicija)
            if sadrzaj =='3':
                self.noviOpis = QTextEdit()
                self.noviOpis.setWordWrapMode(QTextOption.WordWrap)
                self.noviOpis.setText("<h6><i>{0}</i></h6>".format(self.recept.opis))
                self.izgled.addWidget(self.noviOpis,*pozicija)
                self.noviOpis.setMaximumSize(350,350)
            if sadrzaj =='4':
                sviSastojci = self.menadzerSastojci.sviSastojci
                self.tabelaSastojci = Tabela(len(sviSastojci) + 1, 3)
                self.tabelaSastojci.dodajZaglavlja(["Sifra", "Naziv sastojka", "Tip kolicine"])
                self.tabelaSastojci.setColumnWidth(0, 90)
                self.tabelaSastojci.setColumnWidth(1, 150)
                self.tabelaSastojci.setColumnWidth(2, 120)
                brojac = 1
                for sastojak in sviSastojci:
                    self.tabelaSastojci.setItem(brojac, 0, QTableWidgetItem(str(sastojak.sifra)))
                    self.tabelaSastojci.setItem(brojac, 1, QTableWidgetItem(sastojak.naziv))
                    self.tabelaSastojci.setItem(brojac, 2, QTableWidgetItem(str(sastojak.tipKolicine)))
                    brojac += 1
                self.tabelaSastojci.setFixedSize(400, 165)
                self.izgled.addWidget(self.tabelaSastojci, *pozicija)
            if sadrzaj=='5':
                svaOprema = self.menadzerOprema.svaOprema

                self.tabelaOprema = Tabela(len(svaOprema) + 1, 3)
                self.tabelaOprema.dodajZaglavlja(["Sifra", "Naziv aparata", "Naziv marke"])
                self.tabelaOprema.setColumnWidth(0, 80)
                self.tabelaOprema.setColumnWidth(1,150)
                self.tabelaOprema.setColumnWidth(2, 120)

                brojac = 1
                for aparat in svaOprema:
                    self.tabelaOprema.setItem(brojac, 0, QTableWidgetItem(str(aparat.sifra)))
                    self.tabelaOprema.setItem(brojac, 1, QTableWidgetItem(aparat.naziv))
                    self.tabelaOprema.setItem(brojac, 2, QTableWidgetItem(aparat.marka))
                    brojac += 1

                self.tabelaOprema.setFixedSize(400, 165)
                self.izgled.addWidget(self.tabelaOprema,*pozicija)
            if sadrzaj =='6':
                self.kategorije = QLabel()
                self.kategorije.setWordWrap(True)
                nazivi = []
                for id in self.recept.kategorije:
                    naziv = QApplication.instance().actionManager.receptiMenadzer.vratiNazivKategorije(id)
                    nazivi.append(naziv)
                spojeno = ",".join(nazivi)
                # self.kategorije.setFixedSize(350,50)
                self.kategorije.setText("<b>Kategorije: {0}</b>".format(spojeno))
                self.kategorije.setFont(QFont('Times', 12))
                self.izgled.addWidget(self.kategorije,*pozicija)
            if sadrzaj =='7':
                ocjena = QLabel("<h4>Ocjena :{0}</h4>".format(self.recept.ocena))
                ocjena.setAlignment(Qt.AlignCenter)
                ocjena.setFixedSize(350,30)
                self.izgled.addWidget(ocjena,*pozicija)
            if sadrzaj == "8":
                self.kategorijeNazivi = QApplication.instance().actionManager.receptiMenadzer.vratiNaziveKategorija()
                for kategorija in self.recept.kategorije:
                    self.kategorijeNazivi.remove(QApplication.instance().actionManager.receptiMenadzer.vratiNazivKategorije(kategorija))
                kompleter = QCompleter(self.kategorijeNazivi)
                kompleter.setCaseSensitivity(Qt.CaseInsensitive)
                self.unetaKategorija = QLineEdit()
                self.unetaKategorija.setCompleter(kompleter)
                self.unetaKategorija.setFixedSize(150, 25)
                self.izgled.addWidget(self.unetaKategorija, *pozicija)
            if sadrzaj == "9":
                dugme = QPushButton("Dodaj kategoriju")
                dugme.clicked.connect(self.dodajNovuKategoriju)
                self.izgled.addWidget(dugme, *pozicija)
            if sadrzaj == "10":
                dugme = QPushButton("Azuriraj recept")
                dugme.clicked.connect(self.azurirajRecept)
                self.izgled.addWidget(dugme, *pozicija)
            if sadrzaj == "11":
                dugme = QPushButton("Obrisi recept")
                dugme.clicked.connect(self.obrisiRecept)
                self.izgled.addWidget(dugme, *pozicija)
            if sadrzaj == "12":
                labela = QLabel("<h3>Dodajte kategoriju receptu:</h3>")
                self.izgled.addWidget(labela, *pozicija)

    def dodajNovuKategoriju(self):
        kategorija = self.unetaKategorija.text()
        if kategorija == "":
            ObavestavajucaPoruka("Morate uneti naziv kategorije.")
            return
        for id in self.recept.kategorije:
            if QApplication.instance().actionManager.receptiMenadzer.vratiNazivKategorije(id) == kategorija:
                ObavestavajucaPoruka("Uneta kategorija je vec dodeljena receptu.")
                return
        for id in self.dodateKategorije:
            if QApplication.instance().actionManager.receptiMenadzer.vratiNazivKategorije(id) == kategorija:
                ObavestavajucaPoruka("Uneta kategorija je vec dodeljena receptu.")
                return
        provera = False
        for kat in self.kategorijeNazivi:
            if kat.lower() == kategorija.lower():
                provera = True
        if provera == False:
            ObavestavajucaPoruka("Morate uneti kategoriju koja postoji.")
            return
        id = QApplication.instance().actionManager.receptiMenadzer.postojanjeKategorije(kategorija)
        self.dodateKategorije.append(id)
        tekst = self.kategorije.text()
        tekst += ", "
        tekst += kategorija
        self.kategorije.setText("<b>{0}</b>".format(tekst))

    def azurirajRecept(self):
        try:
            naziv = self.noviNaziv.toPlainText()
            opis = self.noviOpis.toPlainText()
            if naziv == self.recept.naziv and opis == self.recept.opis and len(self.dodateKategorije) == 0:
                ObavestavajucaPoruka("Morate naciniti neke izmene.")
            else:
                potvrda = QMessageBox
                odgovor = potvrda.question(self, 'Potvrda',
                    "Da li ste sigurni da zelite da azurirate recept. Ako pritisnete Yes necete vise imati pristup ovom receptu.",
                                           potvrda.Yes | potvrda.No)
                if odgovor == potvrda.Yes:
                    if naziv != self.recept.naziv:
                        self.recept.naziv = naziv
                        QApplication.instance().actionManager.receptiMenadzer.azurirajHtmlDokument(self.recept)
                    self.recept.opis = opis
                    for kategorija in self.dodateKategorije:
                        self.recept.kategorije.append(kategorija)
                    self.sacuvajPromene()
                    self.close()
        except Exception as e:
            print(e)


    def obrisiRecept(self):
        potvrda = QMessageBox
        odgovor = potvrda.question(self, 'Potvrda',
                "Da li ste sigurni da zelite da obrisete recept. Ako pritisnete Yes vise necete imati pravo da ga azurirate.",
                                   potvrda.Yes | potvrda.No)
        if odgovor == potvrda.Yes:
            self.sacuvajPromene()
            self.close()


    def sacuvajPromene(self):
        QApplication.instance().actionManager.receptiMenadzer.izbrisiRecept(self.recept.id)
        QApplication.instance().actionManager.receptiMenadzer.izbrisiReceptKorisniku(self.recept.id)
        QApplication.instance().actionManager.prijavljeniKorisnik.noviRecepti.remove(int(self.recept.id))
        QApplication.instance().actionManager.receptiMenadzer.sacuvajRecepte()
        QApplication.instance().actionManager.informacije.upisiUrednike()
        receptiZaUredjivanje = QApplication.instance().actionManager.receptiMenadzer.pronadjiRecepteZaUredjivanje(
            QApplication.instance().actionManager.prijavljeniKorisnik)
        QApplication.instance().actionManager.glavniProzor.inicijalizujPocetnu()
        QApplication.instance().actionManager.glavniProzor.sledecaPostoji = True
        QApplication.instance().actionManager.glavniProzor.sledecaStranicaBrojac -= 1
        if len(receptiZaUredjivanje) == QApplication.instance().actionManager.glavniProzor.sledecaStranicaBrojac * 4:
            QApplication.instance().actionManager.glavniProzor.sledecaStranicaBrojac -= 1
        QApplication.instance().actionManager.glavniProzor.refresujPocetnu(receptiZaUredjivanje, None, None,
                                                                           None)


