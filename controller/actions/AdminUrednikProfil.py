from view.PrikazInformacijaAdminaIUrednika import *

class AdminUrednikProfil(QAction):
    def __init__(self, parent):
        super().__init__("Prikaz profila", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\user.png'))

    def actionCalled(self):
        prozor = PrikazInformacijaAdminaIUrednika(QApplication.instance().actionManager.prijavljeniKorisnik)