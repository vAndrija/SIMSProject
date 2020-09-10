from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.Tabela import *
from model.Sastojak import *
from model.Oprema import *
import traceback
class SpisakZaKupovinu(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.setModal(True)
        try:
            self.initUI()
        except:
            traceback.print_exc()
        self.show()
        self.exec_()

    def initUI(self):
        self.setWindowTitle("Spisak za kupovinu")
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        self.setFixedSize(600, 600)
        image = QImage("..\slike\spisakPozadina.jpg")
        sImage = image.scaled(QSize(600, 600))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)
        self.definisiIzgled()

    def definisiIzgled(self):
        self.menadzerSastojci = QApplication.instance().actionManager.sastojciMenadzer
        self.menadzerOprema = QApplication.instance().actionManager.opremaMenadzer
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.kuvarPocetnik = QApplication.instance().actionManager.prijavljeniKorisnik
        matrica = ['0', '', '',
                   '', '1', '',
                   '2', '', '',
                   '3', '', '',
                   '4', '', ''
                   ]

        self.proizvodi=[]
        self.spisak = QApplication.instance().actionManager.spiskoviMenadzer.vratiSpisak(
            self.kuvarPocetnik.spisakZaKupovinu
        )
        for kljuc in self.spisak.sastojci.keys():
            self.proizvodi.append(self.menadzerSastojci.vratiSastojak(kljuc))

        for kljuc in self.spisak.oprema.keys():
            self.proizvodi.append(self.menadzerOprema.vratiOpremu(kljuc))

        pozicije = [(i, j) for i in range(5) for j in range(3)]
        for pozicija,sadrzaj  in zip(pozicije,matrica):
            if sadrzaj=="1":
                self.tabela = Tabela(len(self.proizvodi)+1,3)
                self.tabela.dodajZaglavlja(["Naziv", "Tip kol./Marka","Kolicina"])
                self.tabela.setColumnWidth(0, 120)
                self.tabela.setColumnWidth(1, 160)
                self.tabela.setColumnWidth(2, 80)
                brojac=1
                for proizvod in self.proizvodi:
                    if isinstance(proizvod,Sastojak):

                        self.tabela.setItem(brojac, 0, QTableWidgetItem(
                            str(proizvod.naziv)))
                        self.tabela.setItem(brojac, 1, QTableWidgetItem(
                            str(str(proizvod.tipKolicine))
                        ))
                        self.tabela.setItem(brojac, 2, QTableWidgetItem(
                            str(str(self.spisak.sastojci[str(proizvod.sifra)]))
                        ))
                    else:
                        self.tabela.setItem(brojac, 0, QTableWidgetItem(
                            str(proizvod.naziv)))
                        self.tabela.setItem(brojac, 1, QTableWidgetItem(
                            str(str(proizvod.marka))
                        ))
                        self.tabela.setItem(brojac, 2, QTableWidgetItem(
                            str(str(self.spisak.oprema[str(proizvod.sifra)]))
                        ))
                    brojac += 1
                self.tabela.setFixedSize(385,400)
                self.grid.addWidget(self.tabela,*pozicija)
            elif sadrzaj =="2":
                self.narucivanje = QPushButton("Naruci sa sajta")
                self.grid.addWidget(self.narucivanje,*pozicija)
            elif sadrzaj =="3":
                self.slanjeEmail = QPushButton("Slanje spiska na email")
                self.grid.addWidget(self.slanjeEmail,*pozicija)
            elif sadrzaj =="4":
                self.stampanje = QPushButton("Stampanje spiska")
                self.grid.addWidget(self.stampanje,*pozicija)
            elif sadrzaj =="0":
                labela = QLabel('<h6>{0}</h6>'.format('Dodati proizvodi u korpu:'))
                labela.setFixedSize(180,20)
                self.grid.addWidget(labela,*pozicija)
            else:
                labela = QLabel(sadrzaj)
                self.grid.addWidget(labela,*pozicija)
