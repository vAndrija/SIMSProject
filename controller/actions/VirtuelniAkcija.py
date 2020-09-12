from view.VirtuelniKuvar import *


class VirtuelniAkcija(QAction):
    def __init__(self, parent):
        super().__init__("Virtuelni kuvar", parent)
        self.parent = parent
        self.triggered.connect(self.actionCalled)
        self.setIcon(QIcon('..\slike\\virtuelniIkonica.png'))

    def actionCalled(self):
        VirtuelniKuvar(QApplication.instance().actionManager.glavniProzor)

