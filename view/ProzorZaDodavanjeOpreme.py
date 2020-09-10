# Napomena: da li dodati novi aparat u tabelu sa vec postojecim aparatima


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from view.ObavestavajucaPoruka import *
from view.Tabela import *

class ProzorZaDodavanjeOpreme(QDialog):
    def __init__(self):
        super().__init__()
        self.dodatiUTabelu = []
        self.opremaMenadzer = QApplication.instance().actionManager.opremaMenadzer
        self.initUI()

    def initUI(self):
        """
        Funkcija koja definise izgled prozora za dodavanje opreme prilikom registracije korisnika.
        :return:
        """
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        ikonica = QIcon('..\slike\ikonica.png')
        self.setWindowIcon(ikonica)
        self.setFixedSize(900,900)
        image = QImage("..\slike\oprema.jpg")
        sImage = image.scaled(QSize(900, 900))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

        self.postaviGrid()

        self.exec_()

    def postaviGrid(self):
        """
        Funkcija koja postavlja layout prozora za dodavanje opreme prilikom registracije korisnika.
        :return:
        """
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = [
                   '', '','Pretrazite tabelu:',
                    '', '', '1',
                   '', '', '*',
                   '', '', '?',
                   '', '','Dodajte novi aparat:',
                   '', '','Unesite ime:',
                   '', '', '-',
                   '', '', 'Unesite marku:',
                   '', '', '/',
                   '', '', '+',
                   '', '', '!',
                   '', '', '#',
                   '', '', '',
                    '', '', '',
                    '', '', '',
                   ]

        pozicije = [(i, j) for i in range(15) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):
            if sadrzaj == "-":
                self.nazivOpreme = QLineEdit()
                self.nazivOpreme.setFixedSize(250,25)
                grid.addWidget(self.nazivOpreme, *pozicija)
            elif sadrzaj == "*":
                svaOprema = self.opremaMenadzer.svaOprema

                self.postojecaOprema = Tabela(1, 3)
                self.postojecaOprema.dodajZaglavlja(["Sifra", "Naziv aparata", "Naziv marke"])
                self.postojecaOprema.setColumnWidth(0, 120)
                self.postojecaOprema.setColumnWidth(1,219)
                self.postojecaOprema.setColumnWidth(2, 140)

                self.popuniTabeluPostojece(svaOprema)

                self.postojecaOprema.setFixedSize(522, 165)
                grid.addWidget(self.postojecaOprema, *pozicija)
            elif sadrzaj == "?":
                dugme = QPushButton("Dodaj aparat")
                dugme.setFixedSize(250, 30)
                dugme.clicked.connect(self.dodajIzTabele)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                self.nazivMarke = QLineEdit()
                self.nazivMarke.setFixedSize(250,25)
                grid.addWidget(self.nazivMarke, *pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Dodaj aparat")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.dodajNoviAparat)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "!":
                self.dodataOprema = Tabela(1, 3)
                self.dodataOprema.setColumnWidth(0, 120)
                self.dodataOprema.setColumnWidth(1,219)
                self.dodataOprema.setColumnWidth(2, 140)
                self.dodataOprema.setFixedSize(522, 165)
                self.dodataOprema.dodajZaglavlja(["Sifra", "Naziv aparata", "Naziv marke"])
                grid.addWidget(self.dodataOprema, *pozicija)
            elif sadrzaj == "#":
                dugme = QPushButton("Zavrsi dodavanje")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.zavrsenoDodavanje)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "1":
                self.nazivFilter = QLineEdit()
                self.nazivFilter.textChanged.connect(self.izvrsiPretragu)
                self.nazivFilter.setFixedSize(250, 25)
                self.nazivFilter.setToolTip("Unesite ime aparata da biste pretrazili tabelu.")
                grid.addWidget(self.nazivFilter, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(150,35)
                grid.addWidget(labela, *pozicija)



    def dodajIzTabele(self):
        """
        Funkcija koja se poziva kada korisnik oznaci red u tabeli postojecih aparata i pritisne dugme "Dodaj aparat".
        Aparat koji je oznacen bice sacuvan u listi dodatih aparata.
        :return:
        """
        svaOprema = self.opremaMenadzer.svaOprema
        redovi = self.postojecaOprema.selectionModel().selectedRows()
        brojRedova = self.dodataOprema.rowCount()

        brojac = 0
        for red in redovi:
            if red.row() - 1 < 0:
                self.kreirajDijalogSPorukom("Ne mozete oznaciti red sa nazivima kolona.")
            else:
                # oprema = svaOprema[red.row() - 1]
                oprema = QApplication.instance().actionManager.opremaMenadzer.vratiOpremu(self.postojecaOprema.item(red.row(), 0).text())
                if oprema in self.dodatiUTabelu:
                    ObavestavajucaPoruka("Oznaceni aparat ste vec dodali.")
                else:
                    self.dodataOprema.insertRow(brojRedova + brojac)
                    self.dodatiUTabelu.append(oprema.sifra)
                    self.dodataOprema.setItem(brojRedova + brojac, 0, QTableWidgetItem(str(oprema.sifra)))
                    self.dodataOprema.setItem(brojRedova + brojac, 1, QTableWidgetItem(oprema.naziv))
                    self.dodataOprema.setItem(brojRedova + brojac, 2, QTableWidgetItem(oprema.marka))
                    brojac += 1



    def dodajNoviAparat(self):
        """
        Funkcija koja se poziva kada korisnik zeli da unese aparat koji se ne nalazi u tabeli postojecih aparata.
        Kreira se novi objekat, dodaje u listu dodatih aparata i prikazuje u tabeli dodatih aparata.
        :return:
        """
        naziv = self.nazivOpreme.text()
        marka = self.nazivMarke.text()

        oprema = self.opremaMenadzer.kreirajOpremu(naziv, marka)

        if naziv == "" or marka == "":
            ObavestavajucaPoruka("Morate uneti naziv i marku aparata.")
        else:
            if oprema == None:
                ObavestavajucaPoruka("Aparat vec postoji.")
            else:
                brojRedova = self.dodataOprema.rowCount()
                self.dodataOprema.insertRow(brojRedova)
                self.dodatiUTabelu.append(oprema.sifra)
                self.dodataOprema.setItem(brojRedova, 0, QTableWidgetItem(str(oprema.sifra)))
                self.dodataOprema.setItem(brojRedova, 1, QTableWidgetItem(oprema.naziv))
                self.dodataOprema.setItem(brojRedova, 2, QTableWidgetItem(oprema.marka))


    def zavrsenoDodavanje(self):
        """
        Funkcija koja se poziva kada korisnik pritisne dugme 'Zavrsi dodavanje'. Prozor za dodavanje opreme se
        sakriva.
        :return:
        """
        self.hide()
        return self.dodatiUTabelu



    def izvrsiPretragu(self):
        if self.nazivFilter.text() == "":
            self.postojecaOprema.setRowCount(1)
            self.popuniTabeluPostojece(self.opremaMenadzer.svaOprema)
        else:
            self.postojecaOprema.setRowCount(1)
            self.filtrirajTabeluPostojece()


    def popuniTabeluPostojece(self, svaOprema):
        self.postojecaOprema.setColumnWidth(0, 120)
        self.postojecaOprema.setColumnWidth(1, 219)
        self.postojecaOprema.setColumnWidth(2, 140)
        # self.postojecaOprema = Tabela(len(svaOprema) + 1, 3)
        brojac = self.postojecaOprema.rowCount()
        self.postojecaOprema.setRowCount(self.postojecaOprema.rowCount()+len(svaOprema))


        for aparat in svaOprema:
            self.postojecaOprema.setItem(brojac, 0, QTableWidgetItem(str(aparat.sifra)))
            self.postojecaOprema.setItem(brojac, 1, QTableWidgetItem(aparat.naziv))
            self.postojecaOprema.setItem(brojac, 2, QTableWidgetItem(aparat.marka))
            brojac += 1


    def filtrirajTabeluPostojece(self):
        naziv = self.nazivFilter.text()
        for i in self.opremaMenadzer.svaOprema:
            if i.naziv.upper().startswith(naziv.upper()):
                self.popuniTabeluPostojece([i])

