import traceback

from PyQt5.QtWidgets import *


class PredgovorDijalog(QDialog):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.setModal(True)
        self.initUi()
        self.show()
        self.exec_()

    def initUi(self):
        self.setWindowTitle("Azuriranje predgovora")
        izgled = QVBoxLayout()
        self.tekst = QPlainTextEdit()
        self.setLayout(izgled)
        izgled.addWidget(self.tekst)
        dugme = QPushButton("Potvrdi azuriranje")
        izgled.addWidget(dugme)
        dugme.clicked.connect(self.potvrdjeno)

    def potvrdjeno(self):
        self.parent.azuriraniPredgovor = self.tekst.toPlainText()
        self.close()

