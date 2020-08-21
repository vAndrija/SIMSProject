from controller.ManipulacijaKorisnikom import *
from controller.ManipulacijaReceptima import *
class ActionManager(object):

    def __init__(self,aplikacija):

        self.glavniProzor = None
        self.prijava = aplikacija
        self.prijavljeniKorisnik =None
        self.informacije = ManipulacijaKorisnikom()
        self.receptiMenadzer = ManipulacijaReceptima()
