from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view.PraceniKuvari import *
class UredjivanjePratilaca(QAction):
    def __init__(self, parent):
        super().__init__("Pregled i uredjivanje pracenih kuvara", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\follow.png'))

    def actionCalled(self):
        prozor = PraceniKuvari(QApplication.instance().actionManager.glavniProzor)

