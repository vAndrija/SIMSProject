from controller.actions.ManipulacijaKorisnikom import *

class ActionManager(object):

    def __init__(self,ref,glavni,aplikacija):

        self.glavniProzor = glavni
        self.prijava = aplikacija
        self.prijavljeniKorisnik =None
        self.informacije = ManipulacijaKorisnikom()
