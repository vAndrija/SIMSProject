from view.ProzorZaPretragu import *


class PretragaAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Pretraga", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\search.png'))

    def actionCalled(self):
        QApplication.instance().actionManager.pretragaProzor = ProzorZaPretragu()
