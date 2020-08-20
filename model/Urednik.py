from model.KorisnickiNalog import *

class Urednik(KorisnickiNalog):
    def __init__(self, ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol,noviRecepti):
        super().__init__(ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol)
        self.noviRecepti = noviRecepti