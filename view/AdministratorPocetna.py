from PyQt5.QtWidgets import *
from view.ToolbarAdmin import *
from view.PrikazInformacijaKuvara import *
from view.Tabela import *
from view.ObavestavajucaPoruka import *
from view.ProzorZaRegistraciju import *
from view.ProzorZaAzuriranjeNaloga import *
import os
from PyQt5.QtWebEngineWidgets import *
from functools import partial

class AdministratorPocetna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sledecaPostojiTab1 = None
        self.sledecaStranicaBrTab1 = 0
        self.showMinimized()
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.show()
        self.setFixedSize(1000, 900)
        self.inicijalizacijaToolbar()
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

        self.informacije = QApplication.instance().actionManager.informacije

        self.inicijalizujTabove()

        self.hide()


    def inicijalizacijaToolbar(self):
        self.toolbar = ToolbarAdmin(self)

        self.addToolBar(self.toolbar)

    def inicijalizujTabove(self):
        self.tabovi = QTabWidget()
        # self.tab1 = QWidget()

        # self.inicijalizujTab1()
        self.inicijalizujTabKuvari()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabovi.addTab(self.tab1, "Kuvari pocetnici")
        self.tabovi.addTab(self.tab2, "Urednici")
        self.tabovi.addTab(self.tab3, "Reklame")

        self.setCentralWidget(self.tabovi)

    def inicijalizujTabKuvari(self):
        self.tab1 = QWidget()
        self.grid = QGridLayout()
        self.tab1.setLayout(self.grid)

        dio = os.getcwd()[:-4]
        dio = dio.split("\\")
        dio = "/".join(dio)
        putanja = 'file:///' + dio + 'dizajn/profilKorisnika'

        pozicije = [(i, j) for i in range(4) for j in range(2)]

        sviKuvari = self.informacije.sviKuvari

        self.dugmad = []
        trenutni = []

        if len(sviKuvari) >= (self.sledecaStranicaBrTab1 + 1)*4:
            if len(sviKuvari) == (self.sledecaStranicaBrTab1 + 1)*4:
                self.sledecaPostojiTab1 = False
            else:
                self.sledecaPostojiTab1 = True
            for i in range(self.sledecaStranicaBrTab1*4, self.sledecaStranicaBrTab1*4+4):
                trenutni.append(sviKuvari[i])
        else:
            self.sledecaPostojiTab1 = False
            for i in range(self.sledecaStranicaBrTab1 * 4, len(sviKuvari)):
                trenutni.append(sviKuvari[i])
            for i in range(len(sviKuvari), (self.sledecaStranicaBrTab1 + 1) * 4):
                trenutni.append("*")


        for pozicija, kuvar in zip(pozicije, trenutni):
            # if (pozicija[0] != 3):
                if (kuvar != "*"):
                    privrem = QWidget()
                    izgled1 = QVBoxLayout()
                    privrem.setLayout(izgled1)
                    privremeni = QWebEngineView()
                    privremeni.setUrl(QUrl(putanja + "/" + kuvar.korisnickoIme + ".html"))
                    izgled1.addWidget(privremeni)
                    dugme = QPushButton(">>")
                    self.dugmad.append(dugme)
                    dugme.clicked.connect(partial(self.prikazDetaljnihInformacija, kuvar))
                    dugme.setFixedSize(30, 30)
                    izgled1.addWidget(dugme)

                    self.grid.addWidget(privrem, *pozicija)

                else:
                    privrem = QWidget()
                    izgled1 = QVBoxLayout()
                    privrem.setLayout(izgled1)
                    self.grid.addWidget(privrem, *pozicija)

        pozicije = [(i, j) for i in range(4,6) for j in range(2)]

        dugmeSledecaStrana = QPushButton("Sledeca strana")
        dugmePrethodnaStrana =  QPushButton("Prethodna strana")
        dugmeDodajNovi = QPushButton("Dodajte novi nalog")

        dugmici = []
        if self.sledecaStranicaBrTab1 != 0:
            dugmici.append(dugmePrethodnaStrana)
            dugmePrethodnaStrana.clicked.connect(self.refresujPrethodnuTab1)
        else:
            dugmici.append(QLabel(""))
        if self.sledecaPostojiTab1:
            dugmici.append(dugmeSledecaStrana)
            dugmeSledecaStrana.clicked.connect(self.refresujSledecuTab1)
        else:
            dugmici.append(QLabel(""))
        dugmici.append(dugmeDodajNovi)

        for pozicija, dugme in zip(pozicije, dugmici):
            self.grid.addWidget(dugme, *pozicija)


    def refresujSledecuTab1(self):
        self.sledecaStranicaBrTab1 += 1
        self.inicijalizujTabove()

    def refresujPrethodnuTab1(self):
        self.sledecaStranicaBrTab1 -= 1
        self.inicijalizujTabove()



    def inicijalizujTab1(self):
        grid = QGridLayout()
        self.tab1.setLayout(grid)

        matrica = [ '', '', '',
                    '', '', '',
                 '', 'Izaberite nalog:', '',
                 '', '*', '',
                 '', '?', '',
                 '', '-', '',
                 '', '/', '',
                 '', '+', '',
                 '', '', '',
                 '', '', '',
                 '', '', '',
                 ]

        pozicije = [(i, j) for i in range(10) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "*":
                self.napraviTabeluKorisnika()
                grid.addWidget(self.kuvari, *pozicija)
            elif sadrzaj == "?":
                dugme = QPushButton("Obrisi nalog")
                dugme.clicked.connect(self.brisanjeNaloga)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "-":
                dugme = QPushButton("Azuriraj nalog")
                dugme.clicked.connect(self.azuriranjeNaloga)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                dugme = QPushButton("Prikazi detaljne informacije")
                dugme.clicked.connect(self.prikazDetaljnihAplikacija)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Dodaj novi nalog")
                dugme.clicked.connect(self.dodavanjeNovogNaloga)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(110, 20)
                grid.addWidget(labela, *pozicija)


    def napraviTabeluKorisnika(self):
        sviKuvari = self.informacije.sviKuvari
        self.kuvari = Tabela(len(sviKuvari) + 1, 4)
        self.kuvari.setColumnWidth(0,150)
        self.kuvari.setColumnWidth(1, 150)
        self.kuvari.setColumnWidth(2, 150)
        self.kuvari.setColumnWidth(3, 150)
        self.kuvari.dodajZaglavlja(["Ime", "Prezime", "Korisnicko ime", "Mejl"])

        brojac = 1
        for kuvarPocetnik in sviKuvari:
            # item1 = QTableWidgetItem(kuvarPocetnik.ime)
            # item1.setToolTip(kuvarPocetnik.ime)
            # item2 = QTableWidgetItem(kuvarPocetnik.prezime)
            # item2.setToolTip(kuvarPocetnik.prezime)
            # item3 = QTableWidgetItem(kuvarPocetnik.korisnickoIme)
            # item3.setToolTip(kuvarPocetnik.korisnickoIme)
            # item4 = QTableWidgetItem(kuvarPocetnik.mejl)
            # item4.setToolTip(kuvarPocetnik.mejl)
            # self.kuvari.setItem(brojac, 0, item1)
            # self.kuvari.setItem(brojac, 1, item2)
            # self.kuvari.setItem(brojac, 2, item3)
            # self.kuvari.setItem(brojac, 3, item4)
            self.dodajRedUTabelu(kuvarPocetnik, brojac)
            brojac += 1

        self.kuvari.setFixedSize(700, 500)


    def dodajRedUTabelu(self, kuvarPocetnik, brojReda):
        item1 = QTableWidgetItem(kuvarPocetnik.ime)
        item1.setToolTip(kuvarPocetnik.ime)
        item2 = QTableWidgetItem(kuvarPocetnik.prezime)
        item2.setToolTip(kuvarPocetnik.prezime)
        item3 = QTableWidgetItem(kuvarPocetnik.korisnickoIme)
        item3.setToolTip(kuvarPocetnik.korisnickoIme)
        item4 = QTableWidgetItem(kuvarPocetnik.mejl)
        item4.setToolTip(kuvarPocetnik.mejl)
        self.kuvari.setItem(brojReda, 0, item1)
        self.kuvari.setItem(brojReda, 1, item2)
        self.kuvari.setItem(brojReda, 2, item3)
        self.kuvari.setItem(brojReda, 3, item4)

    def prikazDetaljnihInformacija(self, kuvar):
        # sviKuvari = QApplication.instance().actionManager.informacije.sviKuvari
        # redovi = self.kuvari.selectionModel().selectedRows()
        # if len(redovi) == 0:
        #     ObavestavajucaPoruka("Morate oznaciti korisnika ciji pregled zelite.")
        # else:
        #     for red in redovi:
        #         if red.row()-1 < 0:
        #             ObavestavajucaPoruka("Ne mozete oznaciti red sa nazivima kolona.")
        #         else:
        #             kuvar = sviKuvari[red.row()-1]
                    prozor = PrikazInformacijaKuvara(kuvar)


    def dodavanjeNovogNaloga(self):
        prozor = ProzorZaRegistraciju()
        self.setWindowModality(Qt.WindowModal)
        registrovaniKorisnik = prozor.registrovaniKorisnik
        self.kuvari.insertRow(self.kuvari.rowCount())
        self.dodajRedUTabelu(registrovaniKorisnik, self.kuvari.rowCount()-1)

    def brisanjeNaloga(self):
        sviKuvari = QApplication.instance().actionManager.informacije.sviKuvari
        redovi = self.kuvari.selectionModel().selectedRows()
        if len(redovi) == 0:
            ObavestavajucaPoruka("Morate oznaciti korisnika kog zelite da obrisete.")
        else:
            for red in redovi:
                if red.row() - 1 < 0:
                    ObavestavajucaPoruka("Ne mozete oznaciti red sa nazivima kolona.")
                else:
                    potvrda = QMessageBox
                    odgovor = potvrda.question(self, '', "Da li ste sigurni da zelite da obrisete nalog?", potvrda.Yes | potvrda.No)
                    if odgovor == potvrda.Yes:
                        kuvar = sviKuvari[red.row() - 1]
                        sviKuvari.remove(kuvar)
                        QApplication.instance().actionManager.informacije.sviKuvari = sviKuvari
                        QApplication.instance().actionManager.informacije.upisiKorisnika()
                        self.kuvari.removeRow(red.row())


    def azuriranjeNaloga(self):
        sviKuvari = QApplication.instance().actionManager.informacije.sviKuvari
        redovi = self.kuvari.selectionModel().selectedRows()
        if len(redovi) == 0:
            ObavestavajucaPoruka("Morate oznaciti korisnika kog zelite da azurirate.")
        else:
            for red in redovi:
                if red.row() - 1 < 0:
                    ObavestavajucaPoruka("Ne mozete oznaciti red sa nazivima kolona.")
                else:
                    kuvar = sviKuvari[red.row() - 1]
                    prozor = ProzorZaAzuriranjeNaloga(kuvar)
                    self.setWindowModality(Qt.WindowModal)
                    self.dodajRedUTabelu(kuvar, red.row())


    def postaviPoziciju(self):
        dHeight = QApplication.desktop().height()
        dWidth = QApplication.desktop().width()
        wHeight = self.size().height()
        wWidth = self.size().width()
        y = (dHeight - wHeight) / 2
        x = (dWidth - wWidth) / 2
        y = y - 50
        self.move(x, y)