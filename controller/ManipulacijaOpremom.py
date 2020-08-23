from model.Oprema import *
import  json
import  jsonpickle

class ManipulacijaOpremom(object):
    def __init__(self):
        super().__init__()
        self.svaOprema = []
        self.podaci = []
        self.citanjeOpreme()


    def kreirajOpremu(self, naziv, marka):
        if len(self.svaOprema) == 0:
            sifra = 0
        else:
            sifra = self.svaOprema[len(self.svaOprema) - 1].sifra + 1

        novaOprema = Oprema(sifra, naziv, marka)

        provera = self.proveraPostojanjaOpreme(novaOprema)
        if provera:
            return None
        else:
            self.svaOprema.append(novaOprema)
            self.upisiOpremu()
            return novaOprema


    def objToDict(self, obj):
        return obj.__dict__


    def upisiOpremu(self):
        with open('.\..\podaci\oprema.json', 'w') as izlazniFajl:
            json.dump(self.svaOprema, izlazniFajl, default=self.objToDict, indent=4)

    def citanjeOpreme(self):
        tekst = open('.\..\podaci\oprema.json').read()
        if tekst == "":
            self.podaci = []
        else:
            self.podaci = jsonpickle.decode(tekst)

        for podatak in self.podaci:
            oprema = Oprema(**podatak)
            self.svaOprema.append(oprema)

    def proveraPostojanjaOpreme(self, novaOprema):
        for oprema in self.svaOprema:
            if oprema.naziv.upper() == novaOprema.naziv.upper():
                return True

        return False