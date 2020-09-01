from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.Toolbar import *
from view.ProzorZaPretragu import *
import traceback
import os


class KuvarPocetna(QMainWindow):
   def __init__(self):
       super().__init__()
       self.showMinimized()
       self.setWindowTitle("Aplikacija za kuvare pocetnike")
       self.show()
       self.sledecaStranica=0
       self.setFixedSize(1360,700)
       self.inicijalizujDesnuReklamu()
       self.inicijalizujLijevuReklamu()
       self.inicijalizacijaToolbar()
       icon = QIcon("..\slike\ikonica.png")
       self.setWindowIcon(icon)
       sadrzaj = ""
       with open("..\slike\stajl.css", "r") as stream:
           sadrzaj = stream.read()
       self.setStyleSheet(sadrzaj)

       self.inicijalizujPocetnu()
       self.hide()


   def postaviPoziciju(self):
       dHeight = QApplication.desktop().height()
       dWidth = QApplication.desktop().width()
       wHeight = self.size().height()
       wWidth = self.size().width()
       y = (dHeight - wHeight) / 2
       x = (dWidth - wWidth) / 2
       y = y - 50
       self.move(x, y)

   def inicijalizacijaToolbar(self):
       self.toolbar = Toolbar(self)

       self.addToolBar(self.toolbar)

   def inicijalizujPocetnu(self):
        """
       
        :return: 
        """""
        self.lista = QWidget()
        self.setCentralWidget(self.lista)
        self.izgled = QGridLayout()
        self.lista.setLayout(self.izgled)
        self.lista.show()

   def refresujPocetnu(self):
       try:
           dio = os.getcwd()[:-4]
           dio = dio.split("\\")
           dio = "/".join(dio)
           putanja = 'file:///' + dio + 'dizajn/pocetnaRecepti'
           pozicije = [(i, j) for i in range(4) for j in range(2)]
           self.dugmad = []
           self.recepti = QApplication.instance().actionManager.receptiMenadzer.receptiZaPrikaz()
           trenutni = []
           if (len(self.recepti) >= (self.sledecaStranica + 1 * 6)):
               for i in range(self.sledecaStranica * 6, self.sledecaStranica + 6):
                   trenutni.append(self.recepti[i])
           else:

               for i in range(self.sledecaStranica * 6, len(self.recepti)):
                   trenutni.append(self.recepti[i])
               for i in range(self.sledecaStranica * 6, len(self.recepti),
                               (self.sledecaStranica+1)*6):
                    trenutni.append("*")


           for pozicija, recept in zip(pozicije, trenutni):
               if (pozicija[0] != 3):
                   if(recept!="*"):
                       privrem = QWidget()
                       izgled1 = QVBoxLayout()
                       privrem.setLayout(izgled1)
                       privremeni = QWebEngineView()
                       print(os.path.join(putanja, str(recept.id) + ".html"))
                       privremeni.setUrl(QUrl(putanja+"/"+ str(recept.id) + ".html"))
                       izgled1.addWidget(privremeni)
                       dugme = QPushButton(">>")
                       self.dugmad.append(dugme)
                       dugme.setFixedSize(30, 30)
                       izgled1.addWidget(dugme)
                       self.izgled.addWidget(privrem, *pozicija)
                   else:
                       privrem = QWidget()
                       izgled1 = QVBoxLayout()
                       privrem.setLayout(izgled1)
                       self.izgled.addWidget(privrem, *pozicija)

           self.trenutniRecepti = 4
           self.sledecaStranica = QPushButton("Sledeca stranica")
           self.izgled.addWidget(self.sledecaStranica, 3, 0)
       except:
           traceback.print_exc()

   def inicijalizujLijevuReklamu(self):
       """
       Funkcija izvrsava inicijalizovanje i postavljanje pocetnog sadrzaja lijeve reklame u prozoru
       :return:
       """
       reklama = QWebEngineView()
       self.lijevaReklama = QDockWidget()
       self.lijevaReklama.setWidget(reklama)
       self.addDockWidget(Qt.LeftDockWidgetArea, self.lijevaReklama)
       self.lijevaReklama.setFeatures(QDockWidget.NoDockWidgetFeatures )
       self.lijevaReklama.setFixedSize(300,900)
       reklama.showFullScreen()
       reklama.setUrl(QUrl("https://online.idea.rs/#!/categories/60008342/idea-organic"))

   def inicijalizujDesnuReklamu(self):
       """
              Funkcija izvrsava inicijalizovanje i postavljanje pocetnog sadrzaja desne reklame u prozoru
              :return:
              """
       reklama = QWebEngineView()
       self.desnaReklama = QDockWidget()
       self.desnaReklama.setWidget(reklama)
       self.addDockWidget(Qt.RightDockWidgetArea, self.desnaReklama)
       self.desnaReklama.setFeatures(QDockWidget.NoDockWidgetFeatures)
       self.desnaReklama.setFixedSize(300, 900)
       reklama.showFullScreen()
       reklama.setUrl(QUrl("https://online.idea.rs/#!/offers"))

