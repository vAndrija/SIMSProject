from model.KorisnickiNalog import *


class KuvarPocetnik(KorisnickiNalog):
    def __init__(self,ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol
                 ,dugotrajniSastojci,oprema,recepti,virtuelniKuvar,spisakZaKupovinu,praceniKuvari,praceneKategorije):
        super().__init__(ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol)
        self.dugotrajniSastojci = dugotrajniSastojci
        self.oprema = oprema
        self.recepti = recepti
        self.virtuelniKuvar = virtuelniKuvar
        self.spisakZaKupovinu = spisakZaKupovinu
        self.praceniKuvari = praceniKuvari
        self.praceneKategorije = praceneKategorije
