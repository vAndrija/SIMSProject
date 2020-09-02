from PyQt5.QtWidgets import *
from view.ToolbarAdmin import *
from view.PrikazInformacijaKuvara import *
from view.Tabela import *
from view.ObavestavajucaPoruka import *
from view.ProzorZaRegistraciju import *

class AdministratorPocetna(QMainWindow):
    def __init__(self):
        super().__init__()
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
        tabovi = QTabWidget()
        self.tab1 = QWidget()
        image = QImage("..\slike\prijava.jpg")
        sImage = image.scaled(self.tab1.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.tab1.setPalette(palette)
        self.inicijalizujTab1()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        tabovi.addTab(self.tab1, "Kuvari pocetnici")
        tabovi.addTab(self.tab2, "Urednici")
        tabovi.addTab(self.tab3, "Reklame")
        self.setCentralWidget(tabovi)

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
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "-":
                dugme = QPushButton("Azuriraj nalog")
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

    def prikazDetaljnihAplikacija(self):
        sviKuvari = QApplication.instance().actionManager.informacije.sviKuvari
        redovi = self.kuvari.selectionModel().selectedRows()
        if len(redovi) == 0:
            ObavestavajucaPoruka("Morate oznaciti korisnika ciji pregled zelite.")
        else:
            for red in redovi:
                if red.row()-1 < 0:
                    ObavestavajucaPoruka("Ne mozete oznaciti red sa nazivima kolona.")
                else:
                    kuvar = sviKuvari[red.row()-1]
                    prozor = PrikazInformacijaKuvara(kuvar)


    def dodavanjeNovogNaloga(self):
        prozor = ProzorZaRegistraciju()
        self.setWindowModality(Qt.WindowModal)
        registrovaniKorisnik = prozor.registrovaniKorisnik
        self.kuvari.insertRow(self.kuvari.rowCount())
        self.dodajRedUTabelu(registrovaniKorisnik, self.kuvari.rowCount()-1)

    def postaviPoziciju(self):
        dHeight = QApplication.desktop().height()
        dWidth = QApplication.desktop().width()
        wHeight = self.size().height()
        wWidth = self.size().width()
        y = (dHeight - wHeight) / 2
        x = (dWidth - wWidth) / 2
        y = y - 50
        self.move(x, y)