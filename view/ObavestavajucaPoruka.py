from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ObavestavajucaPoruka(QMessageBox):
    def __init__(self, porukaZaIspis):
        super().__init__()
        self.setWindowTitle("Aplikacija za kuvare pocetnike")
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        self.setText(porukaZaIspis)
        self.setFixedSize(350,200)
        self.exec_()