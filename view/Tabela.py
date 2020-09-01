from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Tabela(QTableWidget):
    def __init__(self, brojRedova, brojKolona):
        super().__init__()
        self.setRowCount(brojRedova)
        self.setColumnCount(brojKolona)

    def dodajZaglavlja(self, lista):
        brojac = 0
        for stavka in lista:
            bold = QFont()
            bold.setBold(True)
            item = QTableWidgetItem(stavka)
            item.setFont(bold)
            self.setItem(0, brojac, item)
            brojac += 1