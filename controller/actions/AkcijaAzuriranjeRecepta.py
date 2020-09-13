from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication

from view.ProzorZaAzuriranjeRecepta import ProzorZaAzuriranjeRecepta
import traceback

class AkcijaAzuriranjaRecepta(QAction):
    def __init__(self, parent):
        super().__init__("Brisanje recepta", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\update.png'))

    def actionCalled(self):
        try:
            prozor = ProzorZaAzuriranjeRecepta(QApplication.instance().actionManager.glavniProzor)
        except:
            traceback.print_exc()