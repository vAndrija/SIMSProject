import traceback

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QGridLayout, QLineEdit, QLabel, QPushButton, QWidget, \
    QHBoxLayout, QTableWidget, QApplication


class ProzorZaBrisanjeRecepta(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        try:
            self.initUI()
        except:
            traceback.print_exc()
        self.exec_()

    def ispisi(self):
        if (self.nazivRecepta.text() == ""):
            self.izbrisiSveRecepte()
            self.dodajSveRecepte()
        else:

            self.filtrirajRecepte()

    def izbrisiIzMojihRecepata(self, id):
        for recept in self.mojiRecepti:
            if (recept.id == id):
                self.mojiRecepti.remove(recept)

    def izbrisiRecept(self):
        rows = self.tabelaRecepata.selectionModel().selectedRows()
        brojac = 0
        for row in rows:
            try:
                if (row.row() == 0):
                    continue

                sifra = self.tabelaRecepata.item(row.row() - brojac, 0).text()
                naziv = self.tabelaRecepata.item(row.row() - brojac, 1).text()
                self.tabelaRecepata.removeRow(row.row() - brojac)

                self.menadzerRecepti.izbrisiRecept(int(sifra))
                for receptId in self.prijavljenKorisnik.recepti:
                    if receptId == int(sifra):
                        self.prijavljenKorisnik.recepti.remove(receptId)
                        break

                self.izbrisiIzMojihRecepata(int(sifra))

                brojac += 1
            except:
                traceback.print_exc()
        self.menadzerRecepti.sacuvajRecepte()
        self.menadzerKorisnicima.upisiKorisnika()

    def dodajSveRecepte(self):
        for recept in self.mojiRecepti:
            brojac = self.tabelaRecepata.rowCount()

            self.tabelaRecepata.setRowCount(brojac)
            self.tabelaRecepata.insertRow(brojac)
            self.tabelaRecepata.setItem(brojac, 0, QTableWidgetItem(str(recept.id)))
            self.tabelaRecepata.setItem(brojac, 1, QTableWidgetItem(recept.naziv))

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

    def izbrisiSveRecepte(self):
        self.tabelaRecepata.setRowCount(1)

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
        self.tabelaRecepata.setItem(0, 0, QTableWidgetItem("Sifra recepta"))
        self.tabelaRecepata.setItem(0, 1, QTableWidgetItem("Naziv recepta"))

        self.tabelaRecepata.setColumnWidth(0, 225)
        self.tabelaRecepata.setColumnWidth(1, 225)
        self.dodajSveRecepte()
        self.setModal(True)
        grid = QGridLayout()
        self.nazivRecepta = QLineEdit()
        self.nazivRecepta.textChanged.connect(self.ispisi)  # da radi u realnom vremenu, filtriranje u tabeli za naziv

        names = ['/', '^', '',
                 '*', '', '',
                 '^^^', '', ''
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
                self.nazivRecepta.setFixedSize(250, 25)
                grid.addWidget(self.nazivRecepta, *position)
            elif name == '/':
                self.labelaNaziva = QLabel("Naziv recepta:")
                grid.addWidget(self.labelaNaziva, *position)

            elif name == '^^^':
                self.izbrisiReceptBtn = QPushButton('Izbrisi recept')
                self.izbrisiReceptBtn.setFixedSize(250, 25)
                self.izbrisiReceptBtn.clicked.connect(self.izbrisiRecept)
                grid.addWidget(self.izbrisiReceptBtn, *position)
        grid.addWidget(self.nazivRecepta)
        # self.setLayout(grid)
        self.widget = QWidget()

        image = QImage('..\slike\slicicaBrisanje.jpg')

        sImage = image.scaled(QSize(700, 600))

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))

        self.widget.setPalette(palette)
        self.widget.setLayout(grid)

        self.izgled = QHBoxLayout()

        self.izgled.addWidget(self.widget)
        self.setLayout(self.izgled)
        self.setPalette(palette)

        self.setFixedWidth(700)
        self.setFixedHeight(600)
        self.move(300, 150)
        self.setWindowTitle('Brisanje recepta')
        self.show()
