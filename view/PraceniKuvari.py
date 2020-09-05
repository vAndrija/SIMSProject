from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from view.Tabela import *
import traceback

class PraceniKuvari(QDialog):

    def __init__(self,parent):
        super().__init__(parent)

        self.initUI()
        self.setModal(True)
        self.show()



    def initUI(self):
        self.setWindowTitle("Prikaz i uredjivanje pracenih kuvara")
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        self.setFixedSize(600,600)
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)
        self.definisiIzgled()

    def definisiIzgled(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.kuvarPocetnik  = QApplication.instance().actionManager.prijavljeniKorisnik
        matrica = ['Praceni kuvari:', '', '',
                   '', '1', '',
                   '', '4', '',
                   'Dodavanje novog kuvara:', '2', '',
                   '', '3', '',
                   ]

        self.sviKorisnici = []
        for korisnik in QApplication.instance().actionManager.informacije.sviKuvari:
            if korisnik is not self.kuvarPocetnik:
                self.sviKorisnici.append(korisnik.korisnickoIme)

        pozicije = [(i, j) for i in range(5) for j in range(3)]
        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "1":
                self.tabela = Tabela(len(self.kuvarPocetnik.praceniKuvari) + 1, 3)
                self.tabela.dodajZaglavlja(["Korisnicko"])
                self.tabela.setColumnWidth(0, 120)

                brojac = 1
                for naziv in self.kuvarPocetnik.praceniKuvari:
                    self.tabela.setItem(brojac, 0, QTableWidgetItem(
                       naziv))
                    brojac += 1
                self.tabela.setFixedSize(150, 160)
                self.grid.addWidget(self.tabela, *pozicija)
            elif sadrzaj == "2":

                kompleter = QCompleter(self.sviKorisnici)
                kompleter.setCaseSensitivity(Qt.CaseInsensitive)
                self.labela = QLineEdit()
                self.labela.setCompleter(kompleter)
                self.labela.setFixedSize(130, 20)
                self.grid.addWidget(self.labela, *pozicija)
            elif sadrzaj == "3":
                self.dugme = QPushButton("Zaprati kuvara")
                self.dugme.setFixedSize(200, 20)
                self.grid.addWidget(self.dugme)
                self.dugme.clicked.connect(self.dodavanjeNovog)
            elif sadrzaj == "4":
                self.brisanje = QPushButton("Optrati kuvara")
                self.brisanje.setFixedSize(200, 20)
                self.grid.addWidget(self.brisanje)
                self.brisanje.clicked.connect(self.otpratiKuvara)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(130, 20)
                self.grid.addWidget(labela, *pozicija)


    def otpratiKuvara(self):
        selektovaniRedovi = self.tabela.selectionModel().selectedRows()
        for red in selektovaniRedovi:
            self.kuvarPocetnik.praceniKuvari.pop(red.row() - 1)
            QApplication.instance().actionManager.informacije.upisiKorisnika()
            self.refresujTabelu()

    def dodavanjeNovog(self):
        if self.labela.text() not in self.sviKorisnici:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Potrebno je uneti vec postojeceg korisnika!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return
        if self.labela.text() in  self.kuvarPocetnik.praceniKuvari:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ne mozete pratiti jednog korisnika dva puta!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        if (self.labela.text() == ""):
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Morate uneti korisnicko ime!")
            msg.setWindowTitle("Greska")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        self.kuvarPocetnik.praceniKuvari.append(self.labela.text())
        QApplication.instance().actionManager.informacije.upisiKorisnika()
        self.refresujTabelu()

    def refresujTabelu(self):
        self.tabela = Tabela(len(self.kuvarPocetnik.praceniKuvari) + 1, 3)
        self.tabela.dodajZaglavlja(["Korisnicko"])
        self.tabela.setColumnWidth(0, 120)

        brojac = 1
        for naziv in self.kuvarPocetnik.praceniKuvari:
            self.tabela.setItem(brojac, 0, QTableWidgetItem(
                naziv))

            brojac += 1
        self.tabela.setFixedSize(150, 160)
        self.grid.addWidget(self.tabela, 1,1)