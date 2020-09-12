from controller.ManipulacijaKorisnikom import *
from controller.ManipulacijaOpremom import *
from controller.ManipulacijaReceptima import *
from controller.ManipulacijaSastojcima import *
from controller.ManipulacijaSpiskomZaKupovinu import *
from controller.ManipulacijaVirtuelnimKuvarom import ManipulacijaVirtuelnimKuvarom


class ActionManager(object):

    def __init__(self, aplikacija):
        self.glavniProzor = None
        self.prijava = aplikacija
        self.prijavljeniKorisnik = None
        self.pretragaProzor = None
        self.informacije = ManipulacijaKorisnikom()
        self.receptiMenadzer = ManipulacijaReceptima()
        self.sastojciMenadzer = ManipulacijaSastojcima()
        self.opremaMenadzer = ManipulacijaOpremom()
        self.spiskoviMenadzer = ManipulacijaSpiskomZaKupovinu()
        self.vKuvarMenadzer = ManipulacijaVirtuelnimKuvarom()
