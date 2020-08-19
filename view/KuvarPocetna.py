from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.Toolbar import *
import traceback

class KuvarPocetna(QMainWindow):
   def __init__(self):
       super().__init__()
       self.setWindowTitle("Aplikacija za kuvare pocetnike")
       self.show()
       self.setCentralWidget(QTabWidget())
       self.setFixedSize(1400,900)
       self.inicijalizujDesnuReklamu()
       self.inicijalizujLijevuReklamu()
       self.inicijalizacijaToolbar()
       sadrzaj = ""
       with open("..\slike\stajl.css", "r") as stream:
           sadrzaj = stream.read()
       self.setStyleSheet(sadrzaj)
       dHeight = QApplication.desktop().height()
       dWidth = QApplication.desktop().width()
       wHeight = self.size().height()
       wWidth =self.size().width()
       y = (dHeight - wHeight) / 2
       x = (dWidth - wWidth) / 2
       y =y - 50
       self.move(x,y)

   def inicijalizacijaToolbar(self):
       self.toolbar = Toolbar(self)

       self.addToolBar(self.toolbar)



   def inicijalizujLijevuReklamu(self):
       reklama = QWebEngineView()
       self.lijevaReklama = QDockWidget()
       self.lijevaReklama.setWidget(reklama)

       self.addDockWidget(Qt.LeftDockWidgetArea, self.lijevaReklama)
       self.lijevaReklama.setFeatures(QDockWidget.NoDockWidgetFeatures )
       self.lijevaReklama.setFixedSize(300,900)
       reklama.showFullScreen()
       reklama.setUrl(QUrl("https://online.idea.rs/#!/categories/60008342/idea-organic"))

   def inicijalizujDesnuReklamu(self):
       reklama = QWebEngineView()
       self.desnaReklama = QDockWidget()
       self.desnaReklama.setWidget(reklama)

       self.addDockWidget(Qt.RightDockWidgetArea, self.desnaReklama)
       self.desnaReklama.setFeatures(QDockWidget.NoDockWidgetFeatures)
       self.desnaReklama.setFixedSize(300, 900)
       reklama.showFullScreen()
       reklama.setUrl(QUrl("https://online.idea.rs/#!/offers"))

