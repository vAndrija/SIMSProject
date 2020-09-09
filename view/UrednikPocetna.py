from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view.ToolbarAdmin import *
from view.KuvarPocetna import *
from view.PrikazReceptaUredniku import *

class UrednikPocetna(KuvarPocetna):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 950)


    def inicijalizacijaToolbar(self):
        self.toolbar = ToolbarAdmin(self)
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)


    def inicijalizujDesnuReklamu(self):
        pass


    def inicijalizujLijevuReklamu(self):
        pass

    def prikazRecepta(self,recept):
        PrikazReceptaUredniku(self, recept)