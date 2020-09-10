from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from view.Tabela import *
import traceback
class PrikazKategorija(QDialog):


    def __init__(self,parent):

        super().__init__(parent)

        self.setWindowTitle("Uredjivanje pracenih kategorija")
        self.initUi()
        self.setModal(True)
        self.show()


    def initUi(self):
        self.setFixedSize(700, 700)
        image = QImage("..\slike\kategorije.jpg")
        sImage = image.scaled(QSize(700, 700))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)
        self.definisiIzgled()

    def definisiIzgled(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.kuvarPocetnik = QApplication.instance().actionManager.prijavljeniKorisnik
        self.nazivi  =[]
        for kategorija in self.kuvarPocetnik.praceneKategorije:
            self.nazivi.append(QApplication.instance().actionManager.receptiMenadzer.vratiNazivKategorije(kategorija))
        matrica = ['', 'Pracene kategorije:', '',
                   '', '1', '',
                   '', '4','',
                   '','Dodavanje nove kategorije:','',
                   '', '2', '',
                   '', '3', '',
                   ]
        pozicije = [(i, j) for i in range(6) for j in range(3)]
        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "1":
                self.tabela= Tabela(len(self.nazivi) + 1, 2)
                self.tabela.dodajZaglavlja(["Sifra","Naziv"])
                self.tabela.setColumnWidth(0, 120)
                self.tabela.setColumnWidth(1, 120)
                brojac = 1
                for naziv in self.nazivi:
                    self.tabela.setItem(brojac, 0, QTableWidgetItem(
                        str(self.kuvarPocetnik.praceneKategorije[brojac-1])))
                    self.tabela.setItem(brojac, 1, QTableWidgetItem(naziv))
                    brojac += 1
                self.tabela.setFixedSize(270, 160)
                self.grid.addWidget(self.tabela, *pozicija)
            elif sadrzaj == "2":
                self.kategorijeNazivi = QApplication.instance().actionManager.receptiMenadzer.vratiNaziveKategorija()
                kompleter = QCompleter(self.kategorijeNazivi)
                kompleter.setCaseSensitivity(Qt.CaseInsensitive)
                self.labela = QLineEdit()
                self.labela.setCompleter(kompleter)
                self.labela.setFixedSize(180, 20)
                self.grid.addWidget(self.labela, *pozicija)
            elif sadrzaj == "3":
                self.dugme = QPushButton("Dodaj novu kategoriju")
                self.dugme.setFixedSize(200,20)
                self.grid.addWidget(self.dugme)
                self.dugme.clicked.connect(self.dodavanjeNove)
            elif sadrzaj =="4":
                self.brisanje = QPushButton("Izbrisi kategoriju")
                self.brisanje.setFixedSize(200,20)
                self.grid.addWidget(self.brisanje)
                self.brisanje.clicked.connect(self.brisanjeKategorije)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(180, 20)
                self.grid.addWidget(labela, *pozicija)

    def brisanjeKategorije(self):
        selektovaniRedovi = self.tabela.selectionModel().selectedRows()
        for red in selektovaniRedovi:
                self.nazivi.pop(red.row() - 1)
                self.kuvarPocetnik.praceneKategorije.pop(red.row()-1)
                QApplication.instance().actionManager.informacije.upisiKorisnika()
                self.refresujTabelu()

    def dodavanjeNove(self):

        if self.labela.text().lower() not in self.kategorijeNazivi:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Potrebno je uneti vec postojecu kategoriju!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return
        if self.labela.text().lower() in  self.nazivi:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ne mozete pratiti jednu kategoriju dva puta!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        if (self.labela.text() == ""):
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Morate uneti kategoriju!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        id = QApplication.instance().actionManager.receptiMenadzer.postojanjeKategorije(self.labela.text().lower())
        self.kuvarPocetnik.praceneKategorije.append(id)
        self.nazivi.append(self.labela.text().lower())
        QApplication.instance().actionManager.informacije.upisiKorisnika()
        self.refresujTabelu()



    def refresujTabelu(self):
        self.tabela = Tabela(len(self.nazivi) + 1, 2)
        self.tabela.dodajZaglavlja(["Sifra", "Naziv"])
        self.tabela.setColumnWidth(0, 120)
        self.tabela.setColumnWidth(1, 120)
        brojac = 1
        for naziv in self.nazivi:
            self.tabela.setItem(brojac, 0, QTableWidgetItem(
                str(self.kuvarPocetnik.praceneKategorije[brojac - 1])))
            self.tabela.setItem(brojac, 1, QTableWidgetItem(naziv))
            brojac += 1
        self.tabela.setFixedSize(270, 160)
        self.grid.addWidget(self.tabela, 1,1)