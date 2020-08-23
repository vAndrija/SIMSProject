# Napomena: da li dodati novi aparat u tabelu sa vec postojecim aparatima


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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
                   '', '','Izaberite opremu:',
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

        pozicije = [(i, j) for i in range(14) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):
            if sadrzaj == "-":
                self.nazivOpreme = QLineEdit()
                self.nazivOpreme.setFixedSize(250,25)
                grid.addWidget(self.nazivOpreme, *pozicija)
            elif sadrzaj == "*":
                svaOprema = self.opremaMenadzer.svaOprema
                self.postojecaOprema = QTableWidget()
                self.postojecaOprema.setColumnCount(3)
                self.postojecaOprema.setRowCount(len(svaOprema) + 1)
                self.postojecaOprema.setColumnWidth(0, 120)
                self.postojecaOprema.setColumnWidth(1,219)
                self.postojecaOprema.setColumnWidth(2, 140)
                bold = QFont()
                bold.setBold(True)
                item = QTableWidgetItem("Naziv aparata")
                item.setFont(bold)
                item.setTextAlignment(Qt.AlignCenter)
                item1 = QTableWidgetItem("Naziv marke")
                item1.setFont(bold)
                item1.setTextAlignment(Qt.AlignCenter)
                item2 = QTableWidgetItem("Sifra")
                item2.setFont(bold)
                item2.setTextAlignment(Qt.AlignCenter)
                self.postojecaOprema.setItem(0,0, item2)
                self.postojecaOprema.setItem(0,1, item)
                self.postojecaOprema.setItem(0,2, item1)

                brojac = 1
                for aparat in svaOprema:
                    self.postojecaOprema.setItem(brojac, 0, QTableWidgetItem(str(aparat.sifra)))
                    self.postojecaOprema.setItem(brojac, 1, QTableWidgetItem(aparat.naziv))
                    self.postojecaOprema.setItem(brojac, 2, QTableWidgetItem(aparat.marka))
                    brojac += 1

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
                self.dodataOprema = QTableWidget()
                self.dodataOprema.setColumnCount(3)
                self.dodataOprema.setRowCount(1)
                self.dodataOprema.setColumnWidth(0, 120)
                self.dodataOprema.setColumnWidth(1,219)
                self.dodataOprema.setColumnWidth(2, 140)

                bold = QFont()
                bold.setBold(True)
                item = QTableWidgetItem("Naziv aparata")
                item.setFont(bold)
                item.setTextAlignment(Qt.AlignCenter)
                item1 = QTableWidgetItem("Naziv marke")
                item1.setFont(bold)
                item1.setTextAlignment(Qt.AlignCenter)

                item2 = QTableWidgetItem("Sifra")
                item2.setFont(bold)
                item2.setTextAlignment(Qt.AlignCenter)

                self.dodataOprema.setItem(0,0, item2)
                self.dodataOprema.setItem(0,1, item)
                self.dodataOprema.setItem(0,2, item1)
                self.dodataOprema.setFixedSize(522, 165)
                grid.addWidget(self.dodataOprema, *pozicija)
            elif sadrzaj == "#":
                dugme = QPushButton("Zavrsi dodavanje")
                dugme.setFixedSize(250,30)
                dugme.clicked.connect(self.zavrsenoDodavanje)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(110,35)
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
                oprema = svaOprema[red.row() - 1]
                if oprema in self.dodatiUTabelu:
                    self.kreirajDijalogSPorukom("Oznaceni aparat ste vec dodali.")
                else:
                    self.dodataOprema.insertRow(brojRedova + brojac)
                    self.dodatiUTabelu.append(oprema)
                    self.dodataOprema.setItem(brojRedova + brojac, 0, QTableWidgetItem(str(oprema.sifra)))
                    self.dodataOprema.setItem(brojRedova + brojac, 1, QTableWidgetItem(oprema.naziv))
                    self.dodataOprema.setItem(brojRedova + brojac, 2, QTableWidgetItem(oprema.marka))
                    brojac += 1


    def kreirajDijalogSPorukom(self, tekstPoruke):
        """
        Funkcija koja se poziva kada je potrebno kreirati dijalog sa porukom koja se salje korisniku.
        :param tekstPoruke: poruka koja ce biti ispisana u dijalogu
        :return:
        """
        poruka = QMessageBox()
        poruka.setWindowTitle("Aplikacija za kuvare pocetnike")
        icon = QIcon("..\slike\ikonica.png")
        poruka.setWindowIcon(icon)
        poruka.setText(tekstPoruke)
        poruka.exec_()



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
            self.kreirajDijalogSPorukom("Morate uneti naziv i marku aparata.")
        else:
            if oprema == None:
                self.kreirajDijalogSPorukom("Aparat vec postoji.")
            else:
                brojRedova = self.dodataOprema.rowCount()
                self.dodataOprema.insertRow(brojRedova)
                self.dodatiUTabelu.append(oprema)
                print("DA")
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


