from model.KorisnickiNalog import *

class KuvarPocetnik(KorisnickiNalog):
    def __init__(self):
        self.dugotrajniSastojci = []
        self.oprema = []
        self.recepti = []
        self.virtuelniKuvar = None
        self.spisakZaKupovinu = None
        self.praceniKuvari = []
        self.praceneKategorije = []
        