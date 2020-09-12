from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import traceback
from view.ObavestavajucaPoruka import *
class PrikazRecepta(QDialog):
    def __init__(self,parent,recept):
        super().__init__(parent)
        self.parent = parent
        self.recept = recept
        self.menadzerSastojci  =QApplication.instance().actionManager.sastojciMenadzer
        self.menadzerOprema = QApplication.instance().actionManager.opremaMenadzer
        self.initUi()

        self.show()
        self.exec_()
    def initUi(self):
        self.kuvarPocetnik = QApplication.instance().actionManager.prijavljeniKorisnik
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
        matrica = ['1','','11',
                 '3','','2',
                 '6', '', '7',
                 '4','','5',
                 '8','','9']
        self.sastojci=[]
        self.oprema = []
        pozicije = [(i, j) for i in range(5) for j in range(3)]
        for sadrzaj,pozicija in zip(matrica,pozicije):
            if sadrzaj=='1':
                labela =QLabel()
                labela.setText("<h1 style='color:black'><b>{0}<b></h1>".format(self.recept.naziv))
                labela.setFixedSize(300,40)
                self.izgled.addWidget(labela,*pozicija)
            if sadrzaj =='2':
                labela = QLabel()
                labela.setBackgroundRole(True)

                pixmapa = QPixmap('..\dizajn\\'+str(self.recept.id)+"."+str(self.recept.ekstenzijaSlike))
                pixmapa.scaled(350,350)
                labela.setPixmap(pixmapa)
                labela.setFixedSize(350,350)
                self.izgled.addWidget(labela,*pozicija)
            if sadrzaj =='3':
                opis = QLabel()
                opis.setWordWrap(True)
                opis.setText("<h6><i>{0}</i></h6>".format(self.recept.opis))
                self.izgled.addWidget(opis,*pozicija)
                opis.setMaximumSize(350,350)
            if sadrzaj =='4':
                self.lista = QListWidget()
                for id in self.recept.sastojci.keys():

                    sastojak = self.menadzerSastojci.vratiSastojak(int(id))
                    self.sastojci.append(sastojak)
                    self.lista.addItem("{0} {1}".format(sastojak.naziv,self.recept.sastojci[id]))
                self.lista.setFixedSize(350, 350)
                self.lista.setSelectionMode(1)
                self.izgled.addWidget(self.lista,*pozicija)
            if sadrzaj=='5':
                self.listaOpreme = QListWidget()
                for id in self.recept.oprema:
                    oprema = self.menadzerOprema.vratiOpremu(id)
                    self.oprema.append(oprema)
                    self.listaOpreme.addItem("{0} {1}".format(oprema.naziv,oprema.marka))
                self.listaOpreme.setFixedSize(350,350)
                self.listaOpreme.setSelectionMode(1)
                self.izgled.addWidget(self.listaOpreme,*pozicija)
            if sadrzaj =='6':
                kategorije = QLabel()
                kategorije.setWordWrap(True)
                nazivi = []
                for id in self.recept.kategorije:
                    naziv = QApplication.instance().actionManager.receptiMenadzer.vratiNazivKategorije(id)
                    nazivi.append(naziv)
                spojeno = ",".join(nazivi)
                kategorije.setFixedSize(350,50)
                kategorije.setText("<h3>Kategorije: {0}</h3>".format(spojeno))
                self.izgled.addWidget(kategorije,*pozicija)
            if sadrzaj =='7':
                self.ocjena = QLabel("<h4>Ocjena :{0}</h4>".format(self.recept.ocena.vrednost), self)
                self.ocjena.setFixedSize(350,30)
                self.izgled.addWidget(self.ocjena,*pozicija)
        self.definisanjeDugmica(matrica,pozicije)
        if QApplication.instance().actionManager.receptiMenadzer.proveriPripadnostRecepta(self.recept.id) == False:
            self.dodajElementeZaOcenjivanje()

    def definisanjeDugmica(self,matrica,pozicije):

        for sadrzaj, pozicija in zip(matrica, pozicije):
            if sadrzaj =='8':
                self.dodajSastojkeUKorpu=QPushButton("Dodaj sastojke")
                self.dodajSastojkeUKorpu.clicked.connect(self.dodajSastojak)
                self.izgled.addWidget(self.dodajSastojkeUKorpu,*pozicija)
            if sadrzaj == '9':
               self.dodajOpremu =QPushButton("Dodaj opremu")
               self.dodajOpremu.clicked.connect(self.dodajOpremuMetoda)
               self.izgled.addWidget(self.dodajOpremu,*pozicija)
            if sadrzaj =='11':
                self.dodajUKuvar = QPushButton('Dodaj u kuvar')
                self.dodajUKuvar.clicked.connect(self.dodavanjeUVirtuelniKuvar)
                self.izgled.addWidget(self.dodajUKuvar,*pozicija)

    def dodajElementeZaOcenjivanje(self):
        labela = QLabel("<h3>Izaberite ocenu:</h3>")
        self.izgled.addWidget(labela, 2, 1)
        self.comboOcena = QComboBox()
        for i in range(1,11):
            self.comboOcena.addItem(str(i))
        font = QFont()
        font.setBold(True)
        self.comboOcena.setFont(font)
        self.izgled.addWidget(self.comboOcena, 3, 1)
        self.ocjeniDugme = QPushButton("Ocjeni recept")
        self.ocjeniDugme.clicked.connect(self.oceniRecept)
        self.izgled.addWidget(self.ocjeniDugme, 4, 1)


    def oceniRecept(self):
        if QApplication.instance().actionManager.receptiMenadzer.proveriPrethodnoOcenjivanje(self.recept) == False:
            ocena = self.comboOcena.currentIndex() + 1
            QApplication.instance().actionManager.receptiMenadzer.dodajOcenuReceptu(self.recept, ocena)
            self.ocjena.setText("<h4>Ocjena :{0}</h4>".format(self.recept.ocena.vrednost))
        else:
            ObavestavajucaPoruka("Vec ste ocenili ovaj recept.")



    def dodavanjeUVirtuelniKuvar(self):

        try:
            vKuvar = QApplication.instance().actionManager.vKuvarMenadzer.vratiVirtuelniKuvar(
                self.kuvarPocetnik.virtuelniKuvar
            )
            vKuvar.recepti.append(self.recept.id)
            QApplication.instance().actionManager.vKuvarMenadzer.upisiVirtuelneKuvare()
        except:
            traceback.print_exc()


    def dodajSastojak(self):
        indeksi = self.lista.selectionModel().selectedIndexes()
        kolicina = None
        if indeksi == []:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Morate selektovati zeljeni sastojak!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        while(True):
            kolicina, ok = QInputDialog.getText(self, 'Unos kolicine',
                                            'Unesite zeljenu kolicinu:')
            if ok != True:
                return
            if  not kolicina.isnumeric() or int(kolicina)<=0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                msg.setText("Kolicina koju ste unijeli nije validna!")
                msg.setWindowTitle("Greska")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

            else:
                kolicina = int(kolicina)
                break
        sastojak = None
        for x in indeksi:
            sastojak = self.sastojci[x.row()]
        spisak = QApplication.instance().actionManager.spiskoviMenadzer.vratiSpisak(
            self.kuvarPocetnik.spisakZaKupovinu
        )
        if str(sastojak.sifra) in spisak.sastojci:
            spisak.sastojci[str(sastojak.sifra)] = spisak.sastojci[str(sastojak.sifra)]+kolicina
        else:
            spisak.sastojci[str(sastojak.sifra)] = kolicina
        QApplication.instance().actionManager.spiskoviMenadzer.upisiSpiskove()


    def dodajOpremuMetoda(self):
        indeksi = self.listaOpreme.selectionModel().selectedIndexes()
        kolicina = None
        if indeksi == []:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Morate selektovati zeljenu opremu!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        while (True):
            kolicina, ok = QInputDialog.getText(self, 'Unos kolicine',
                                                'Unesite zeljene kolicinu:')
            if ok != True:
                return
            if not kolicina.isnumeric() or int(kolicina) <= 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                msg.setText("Kolicina koju ste unijeli nije validna!")
                msg.setWindowTitle("Greska")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

            else:
                kolicina = int(kolicina)
                break
        oprema = None
        for x in indeksi:
            oprema = self.oprema[x.row()]
        spisak = QApplication.instance().actionManager.spiskoviMenadzer.vratiSpisak(
            self.kuvarPocetnik.spisakZaKupovinu
        )
        if str(oprema.sifra) in spisak.oprema:
            spisak.oprema[str(oprema.sifra)] = spisak.oprema[str(oprema.sifra)] + kolicina
        else:
            spisak.oprema[str(oprema.sifra)] = kolicina
        QApplication.instance().actionManager.spiskoviMenadzer.upisiSpiskove()
