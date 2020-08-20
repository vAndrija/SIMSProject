from model.KorisnickiNalog import *
from model.Administrator import *
from model.Urednik import *
from model.Mesto import *
import json
import  jsonpickle

class ManipulacijaKorisnikom(object):
    def __init__(self):
        super().__init__()
        self.podaci = []
        self.sviKorisnici = []
        self.sviUrednici = []
        self.administrator =None
        self.citanjeKorisnika()
        self.citajAdmineUrednike()

    def kreirajKorisnika(self, ime, prezime, kIme, lozinka, mejl, datum, adresa, mesto, postanskiBr, pol):
        grad = Mesto(mesto, postanskiBr)
        noviKorisnik = KorisnickiNalog(ime, prezime, kIme, lozinka, mejl, datum, adresa, grad, pol)


        self.sviKorisnici.append(noviKorisnik)
        self.upisiKorisnika(noviKorisnik)

    def objToDict(self, obj):
        return  obj.__dict__

    def upisiKorisnika(self,korisnik):
        with open('.\..\podaci\kuvari.json', 'w') as outfile:
            # json.dump(self.podaci, outfile, default=lambda  o: o.__dict__, indent=4)
            json.dump(self.sviKorisnici, outfile, default= self.objToDict,  indent=4)

    def citanjeKorisnika(self):
        # with open('.\..\podaci\kuvari.json', 'r') as outfile:
        #     self.sviKorisnici = json.load(outfile,default=lambda  o: o.__dict__,indent = 4)
        tekst = open('.\..\podaci\kuvari.json').read()
        if tekst == "":
            self.podaci = []
        else:
            self.podaci = jsonpickle.decode(tekst)

        for i in self.podaci:
            print(i)
            korisnik = KorisnickiNalog(**i)
            mesto = Mesto(**i['mesto'])
            korisnik.mesto = mesto
            self.sviKorisnici.append(korisnik)


    def citajAdmineUrednike(self):
        tekst = open('.\..\podaci\\administratori.json').read()
        tekst = jsonpickle.decode(tekst)
        self.administrator = Administrator(**tekst)
        mjesto = Mesto(**tekst['mesto'])
        self.administrator.mesto=mjesto

        tekst=open('.\\..\\podaci\\urednici.json').read()
        podaci = jsonpickle.decode(tekst)
        for ur in podaci:
            urednik = Urednik(**ur)
            mjesto = Mesto(**ur['mesto'])
            urednik.mesto=mjesto
            self.sviUrednici.append(urednik)
            print(urednik)
            print(type(urednik.mesto))



