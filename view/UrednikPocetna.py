from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view.ToolbarAdmin import *

class UrednikPocetna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMinimized()
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        self.show()
        self.setFixedSize(1000, 950)
        self.inicijalizacijaToolbar()
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

        self.informacije = QApplication.instance().actionManager.informacije

        self.inicijalizujCentralniWidget()

        self.hide()

    def inicijalizacijaToolbar(self):
        self.toolbar = ToolbarAdmin(self)

        self.addToolBar(self.toolbar)

    def postaviPoziciju(self):
        dHeight = QApplication.desktop().height()
        dWidth = QApplication.desktop().width()
        wHeight = self.size().height()
        wWidth = self.size().width()
        y = (dHeight - wHeight) / 2
        x = (dWidth - wWidth) / 2
        y = y - 50
        self.move(x, y)

    def inicijalizujCentralniWidget(self):
        self.lista = QWidget()
        self.setCentralWidget(self.lista)
        self.izgled = QGridLayout()
        self.lista.setLayout(self.izgled)
        self.lista.show()