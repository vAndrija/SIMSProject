from model.KorisnickiNalog import *
from model.Mesto import *
import json
import  jsonpickle

class ManipulacijaKorisnikom(object):
    def __init__(self):
        super().__init__()
        self.sviKorisnici = []
        self.podaci = {}
        self.podaci['korisnici'] = []

    def kreirajKorisnika(self, ime, prezime, kIme, lozinka, mejl, datum, adresa, mesto, postanskiBr, pol):
        noviKorisnik = KorisnickiNalog()
        noviKorisnik.ime = ime
        noviKorisnik.prezime = prezime
        noviKorisnik.korisnickoIme = kIme
        noviKorisnik.lozinka = lozinka
        noviKorisnik.mejl = mejl
        noviKorisnik.datumRodjenja = datum
        noviKorisnik.adresa = adresa
        grad = Mesto()
        grad.nazivMesta = mesto
        grad.postanskiBroj = postanskiBr
        noviKorisnik.mesto = grad
        noviKorisnik.pol = pol

        self.citanjeKorisnika()
        self.sviKorisnici.append(noviKorisnik)
        self.upisiKorisnika(noviKorisnik)


    def upisiKorisnika(self,korisnik):
        jsonKorisnik = {'ime' : korisnik.ime,
                        'prezime' : korisnik.prezime,
                        'korisnickoIme' : korisnik.korisnickoIme,
                        'lozinka' : korisnik.lozinka,
                        'mejl' : korisnik.mejl,
                        'datumRodjenja' : str(korisnik.datumRodjenja),
                        'adresa' : korisnik.adresa,
                        'mesto' : { 'nazivMesta' : korisnik.mesto.nazivMesta,
                                    'postanskiBroj' : korisnik.mesto.postanskiBroj},
                        'pol' : korisnik.pol
                        }
        self.podaci['korisnici'].append(jsonKorisnik)
        with open('.\..\podaci\kuvari.json', 'w') as outfile:
            json.dump(self.podaci, outfile, default=lambda  o: o.__dict__, indent=4)

    def citanjeKorisnika(self):
        # with open('.\..\podaci\kuvari.json', 'r') as outfile:
        #     self.sviKorisnici = json.load(outfile,default=lambda  o: o.__dict__,indent = 4)
        tekst = open('.\..\podaci\kuvari.json').read()
        if tekst == "":
            self.podaci = {}
            self.podaci['korisnici'] = []
        else:
            self.podaci = jsonpickle.decode(tekst)