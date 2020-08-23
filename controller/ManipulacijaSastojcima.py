from model.Sastojak import *
import json
import  jsonpickle
from model.TipKolicine import *

class ManipulacijaSastojcima(object):
    def __init__(self):
        super().__init__()
        self.podaci = []
        self.sviSastojci = []
        self.citanjeSastojaka()

    def kreirajSastojak(self, nazivSastojka, tipKolicine):
        if len(self.sviSastojci) == 0:
            sifra = 0
        else:
            sifra = self.sviSastojci[len(self.sviSastojci)-1].sifra + 1


        noviSastojak = Sastojak(sifra, nazivSastojka, tipKolicine)
        provera = self.proveraPostojanjaSastojka(noviSastojak)
        if provera == True:
            return None
        else:
            self.sviSastojci.append(noviSastojak)
            self.upisiSastojak()
            return noviSastojak


    def objToDict(self, obj):
        if isinstance(obj, TipKolicine):
            return obj.__str__()
        else:
            return obj.__dict__

    def upisiSastojak(self):
        with open('.\..\podaci\sastojci.json', 'w') as izlazniFajl:
            json.dump(self.sviSastojci, izlazniFajl, default=self.objToDict, indent=4)

    def citanjeSastojaka(self):
        tekst = open('.\..\podaci\sastojci.json').read()
        if tekst == "":
            self.podaci = []
        else:
            self.podaci = jsonpickle.decode(tekst)

        for podatak in self.podaci:
            sastojak = Sastojak(**podatak)
            if podatak["tipKolicine"] == "GRAM":
                tipKolicine = TipKolicine.GRAM
            elif podatak["tipKolicine"] == "KOMAD":
                tipKolicine = TipKolicine.KOMAD
            elif podatak["tipKolicine"] == "DL":
                tipKolicine = TipKolicine.DL
            elif podatak["tipKolicine"] == "PRSTOHVAT":
                tipKolicine = TipKolicine.PRSTOHVAT
            else:
                tipKolicine = TipKolicine.SUPENAKASIKA
            sastojak.tipKolicine = tipKolicine

            self.sviSastojci.append(sastojak)


    def proveraPostojanjaSastojka(self, sastojak):
        for jedanSastojak in self.sviSastojci:
            if jedanSastojak.naziv.upper() == sastojak.naziv.upper():
                return True
        return False
