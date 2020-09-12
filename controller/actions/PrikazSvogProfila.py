from view.PrikazSopstvenihInformacija import *


class SopstveniProfilAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Profil", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\user.png'))

    def actionCalled(self):
        PrikazSopstvenihInformacija(QApplication.instance().actionManager.prijavljeniKorisnik)
