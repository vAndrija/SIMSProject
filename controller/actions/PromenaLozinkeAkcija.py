from view.ProzorZaPromenuLozinke import *

class PromenaLozinkeAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Promena lozinke", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\\slike\\lozinkaIkonica.png'))

    def actionCalled(self):
        try:
            prozor = ProzorZaPromenuLozinke(QApplication.instance().actionManager.prijavljeniKorisnik)
        except Exception as e:
            print(e)