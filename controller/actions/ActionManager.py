from controller.ManipulacijaKorisnikom import *
from controller.ManipulacijaReceptima import *
class ActionManager(object):

    def __init__(self,ref,glavni,aplikacija):

        self.glavniProzor = glavni
        self.prijava = aplikacija
        self.prijavljeniKorisnik =None
        self.informacije = ManipulacijaKorisnikom()
        self.receptiMenadzer = ManipulacijaReceptima()
