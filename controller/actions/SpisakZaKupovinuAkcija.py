from view.SpisakZaKupovinu import *
class SpisakZaKupovinuAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Spisak za kupovinu", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\spisakIkonica.png'))

    def actionCalled(self):
        SpisakZaKupovinu(QApplication.instance().actionManager.glavniProzor)