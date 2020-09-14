from model.KorisnickiNalog import *


class KuvarPocetnik(KorisnickiNalog):
    def __init__(self, ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol
                 , dugotrajniSastojci, oprema, recepti, virtuelniKuvar, spisakZaKupovinu, praceniKuvari,
                 praceneKategorije, promocija):
        super().__init__(ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol)
        self.dugotrajniSastojci = dugotrajniSastojci
        self.oprema = oprema
        self.recepti = recepti
        self.virtuelniKuvar = virtuelniKuvar
        self.spisakZaKupovinu = spisakZaKupovinu
        self.praceniKuvari = praceniKuvari
        self.praceneKategorije = praceneKategorije
        self.promocija = promocija

    def proveriPripadnostRecepta(self, idRecepta):
        for recept in self.recepti:
            if recept == idRecepta:
                return True
        return False
