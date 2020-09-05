from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import traceback
class PrikazRecepta(QDialog):
    def __init__(self,parent,recept):
        super().__init__(parent)
        try:
            self.recept = recept
            self.menadzerSastojci  =QApplication.instance().actionManager.sastojciMenadzer
            self.menadzerOprema = QApplication.instance().actionManager.opremaMenadzer
            self.initUi()
        except:
            traceback.print_exc()
        self.show()
    def initUi(self):
        self.setWindowTitle("Prikaz recepta")
        self.setModal(True)
        image = QImage("..\slike\slika6.jpg")
        sImage = image.scaled(QSize(800, 800))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.setFixedSize(800,800)
        self.izgled = QGridLayout()
        self.setLayout(self.izgled)
        matrica = ['1','','',
                 '3','','2',
                 '6', '', '7',
                 '4','','5',
                 '8','9','10']
        self.selekcije=[]
        pozicije = [(i, j) for i in range(5) for j in range(3)]
        for sadrzaj,pozicija in zip(matrica,pozicije):
            if sadrzaj=='1':
                labela =QLabel()
                labela.setText("<h1 style='color:black'><b>{0}<b></h1>".format(self.recept.naziv))
                labela.setFixedSize(130,40)
                self.izgled.addWidget(labela,*pozicija)
            if sadrzaj =='2':
                labela = QLabel()
                labela.setBackgroundRole(True)

                pixmapa = QPixmap('..\dizajn\\'+str(self.recept.id)+"."+str(self.recept.ekstenzijaSlike))
                labela.setPixmap(pixmapa)
                labela.setMinimumSize(300,300)
                self.izgled.addWidget(labela,*pozicija)
            if sadrzaj =='3':
                opis = QLabel()
                opis.setWordWrap(True)
                opis.setText("<h6><i>{0}</i></h6>".format(self.recept.opis))
                self.izgled.addWidget(opis,*pozicija)
                opis.setMaximumSize(200,300)
            if sadrzaj =='4':
                self.lista = QListWidget()
                for id in self.recept.sastojci.keys():
                    sastojak = self.menadzerSastojci.vratiSastojak(int(id))
                    self.lista.addItem("{0} {1}".format(sastojak.naziv,self.recept.sastojci[id]))
                self.lista.setFixedSize(200, 200)
                self.izgled.addWidget(self.lista,*pozicija)
            if sadrzaj=='5':
                self.listaOpreme = QListWidget()
                for id in self.recept.oprema:
                    oprema = self.menadzerOprema.vratiOpremu(id)
                    self.listaOpreme.addItem("{0} {1}".format(oprema.naziv,oprema.marka))
                self.listaOpreme.setFixedSize(200,200)
                self.izgled.addWidget(self.listaOpreme,*pozicija)
            if sadrzaj =='6':
                kategorije = QLabel()
                nazivi = []
                for id in self.recept.kategorije:
                    naziv = QApplication.instance().actionManager.receptiMenadzer.vratiNazivKategorije(id)
                    nazivi.append(naziv)
                spojeno = ",".join(nazivi)
                kategorije.setFixedSize(300,30)
                kategorije.setText("<h3>Kategorije: {0}</h3>".format(spojeno))
                self.izgled.addWidget(kategorije,*pozicija)
            if sadrzaj =='7':
                ocjena = QLabel("<h4>Ocjena :{0}</h4>".format(self.recept.ocena))
                ocjena.setFixedSize(200,30)
                self.izgled.addWidget(ocjena,*pozicija)
            if sadrzaj =='8':
                self.dodajSastojkeUKorpu=QPushButton("Dodaj sastojke")

                self.izgled.addWidget(self.dodajSastojkeUKorpu,*pozicija)
            if sadrzaj == '9':
               self.dodajOpremu =QPushButton("Dodaj opremu")

               self.izgled.addWidget(self.dodajOpremu,*pozicija)
            if sadrzaj =='10':
                self.ocjeniDugme = QPushButton("Ocjeni recept")

                self.izgled.addWidget(self.ocjeniDugme,*pozicija)



