from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class SopstveniProfilAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Profil", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\user.png'))

    def actionCalled(self):
        pass
