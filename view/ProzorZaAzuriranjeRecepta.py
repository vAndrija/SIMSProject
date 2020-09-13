import traceback

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *

from src.view.AzurirajReceptDialog import AzurirajRecept
from view.ObavestavajucaPoruka import ObavestavajucaPoruka


class ProzorZaAzuriranjeRecepta(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.initUI()
        self.exec_()
    def refresh(self):
        if (self.nazivRecepta.text() == ""):
            self.izbrisiSveRecepte()
            self.dodajSveRecepte()
        else:

            self.filtrirajRecepte()

    def izbrisiIzMojihRecepata(self, id):
        for recept in self.mojiRecepti:
            if (recept.id == id):
                self.mojiRecepti.remove(recept)



    def dodajSveRecepte(self):
        for recept in self.mojiRecepti:
            brojac = self.tabelaRecepata.rowCount()

            self.tabelaRecepata.setRowCount(brojac)
            self.tabelaRecepata.insertRow(brojac)
            self.tabelaRecepata.setItem(brojac, 0, QTableWidgetItem(str(recept.id)))
            self.tabelaRecepata.setItem(brojac, 1, QTableWidgetItem(recept.naziv))
    def azurirajRecept(self):
        try:
            rows = self.tabelaRecepata.selectionModel().selectedRows()
            if (len(rows) == 0):
                ObavestavajucaPoruka("Oznacite recept")
                return
            if(len(rows) > 1):
                ObavestavajucaPoruka("Oznacite iskljucivo jedan recept")
                return
            for row in rows:
                if (row.row() == 0):
                    ObavestavajucaPoruka("Pogresno oznacena vrsta")
                    return
            self.id = self.tabelaRecepata.item(row.row(), 0).text()
            prozor = AzurirajRecept(int(self.id))
        except:
            traceback.print_exc()

    def filtrirajRecepte(self):
        tekst = self.nazivRecepta.text()
        self.izbrisiSveRecepte()
        for recept in self.mojiRecepti:

            if recept.naziv.upper().startswith(tekst.upper()):
                brojac = self.tabelaRecepata.rowCount()

                self.tabelaRecepata.setRowCount(brojac)
                self.tabelaRecepata.insertRow(brojac)
                self.tabelaRecepata.setItem(brojac, 0, QTableWidgetItem(str(recept.id)))
                self.tabelaRecepata.setItem(brojac, 1, QTableWidgetItem(recept.naziv))


    def odrediMojeRecepte(self):
        self.mojiRecepti = []
        for recept in self.menadzerRecepti.recepti:
            if recept.id in self.prijavljenKorisnik.recepti:
                self.mojiRecepti.append(recept)

    def initUI(self):
        self.menadzerRecepti = QApplication.instance().actionManager.receptiMenadzer
        self.prijavljenKorisnik = QApplication.instance().actionManager.prijavljeniKorisnik
        self.menadzerKorisnicima = QApplication.instance().actionManager.informacije
        self.odrediMojeRecepte()

        self.tabelaRecepata = QTableWidget()
        self.tabelaRecepata.setColumnCount(2)
        self.tabelaRecepata.setRowCount(1)
        self.tabelaRecepata.setItem(0,0,QTableWidgetItem("sifra recepta"))
        self.tabelaRecepata.setItem(0,1,QTableWidgetItem("naziv recepta"))
        self.tabelaRecepata.setColumnWidth(0,225)
        self.tabelaRecepata.setColumnWidth(1,225)
        self.dodajSveRecepte()
        grid  = QGridLayout()
        self.nazivPolje = QLineEdit()
        self.nazivPolje.textChanged.connect(self.refresh)#da radi u realnom vremenu, filtriranje u tabeli za naziv

        names = ['/', '^','',
                 '*', '','',
                 '^^^', '',''
                 ]
        self.tabelaRecepata.setFixedSize(450, 270)
        sadrzaj = ""
        with open("..\slike\stajlBrisanjeRecepta.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)
        positions = [(i, j) for i in range(3) for j in range(3)]
        for position, name in zip(positions, names):
            if name == '*':
                grid.addWidget(self.tabelaRecepata)
            elif name == '^':
                self.nazivPolje.setFixedSize(250, 25)
                grid.addWidget(self.nazivPolje,*position)
            elif name == '/':
                self.labelaNaziva = QLabel("Naziv recepta")
                grid.addWidget(self.labelaNaziva,*position)

            elif name == '^^^':
                self.azurirajReceptBtn = QPushButton('Azuriraj recept')
                self.azurirajReceptBtn.setFixedSize(250, 25)
                self.azurirajReceptBtn.clicked.connect(self.azurirajRecept)
                grid.addWidget(self.azurirajReceptBtn,*position)
        grid.addWidget(self.nazivPolje)
        #self.setLayout(grid)
        self.widget = QWidget()

        image = QImage("..\slike\slicica.jpg")

        sImage = image.scaled(QSize(650, 420))

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))


        #self.widget.setPalette(palette)
        self.widget.setPalette(palette)
        self.widget.setLayout(grid)


        self.izgled = QHBoxLayout()

        self.izgled.addWidget(self.widget)
        self.setLayout(self.izgled)
        self.setPalette(palette)

        self.setFixedWidth(700)
        self.setFixedHeight(600)
        self.move(300, 150)
        self.setWindowTitle('Azuriranje recepata')
        self.show()