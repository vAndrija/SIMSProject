from model.KorisnickiNalog import *

class Administrator(KorisnickiNalog):
    def __init__(self, ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol):
        super().__init__( ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol)