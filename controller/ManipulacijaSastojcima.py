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
            sifra = self.sviSastojci[self.sviSastojci()-1].sifra + 1

        noviSastojak = Sastojak(sifra, nazivSastojka, tipKolicine)

        self.sviSastojci.append(noviSastojak)
        self.upisiSastojak()


    def objToDict(self, obj):
        if isinstance(obj, TipKolicine):
            return obj.__str__()
        else:
            return obj.__dict__

    def upisiSastojak(self):
        with open('.\..\podaci\sastojci.json', 'w') as outfile:
            json.dump(self.sviSastojci, outfile, default=self.objToDict, indent=4)

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
