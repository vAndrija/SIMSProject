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
        """
        Funkcija koja poziva konstruktor klase Oprema i dodaje novi objekat u listu opreme koja je vec sacuvana.
        :param naziv: naziv novog aparata
        :param marka: naziv marke novog aparata
        :return:
        """
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
        """
        Pomocna funkcija za redefinisanje serijalizacije za json paket
        :param obj:
        :return:
        """
        return obj.__dict__


    def upisiOpremu(self):
        """
        Funkcija koja vrsi serijalizaciju svih aparata iz liste u fajl oprema.json.
        :return:
        """
        with open('.\..\podaci\oprema.json', 'w') as izlazniFajl:
            json.dump(self.svaOprema, izlazniFajl, default=self.objToDict, indent=4)

    def citanjeOpreme(self):
        """
        Funkcija koja ucitava sve aparate iz oprema.json fajla i smesta ih u listu.
        :return:
        """
        tekst = open('.\..\podaci\oprema.json').read()
        if tekst == "":
            self.podaci = []
        else:
            self.podaci = jsonpickle.decode(tekst)

        for podatak in self.podaci:
            oprema = Oprema(**podatak)
            self.svaOprema.append(oprema)

    def proveraPostojanjaOpreme(self, novaOprema):
        """
        Funkcija koja proverava da li je prosledjeni aparat vec upisan u fajl oprema.json.
        :param novaOprema: objekat koji se proverava
        :return:
        """
        for oprema in self.svaOprema:
            if oprema.naziv.upper() == novaOprema.naziv.upper() and oprema.marka.upper() == novaOprema.marka.upper():
                return True

        return False

    def provjeraPostojanjaOpreme(self,noviNaziv):
        """
        Funkcija koja na osnovu naziva opreme vraca da li je ista oprema u pitanju
        :param noviNaziv:
        :return:
        """
        for oprema in self.svaOprema:
            if oprema.naziv.upper() == noviNaziv.upper():
                return True

        return False

    def vratiOpremu(self,id):
        for oprema in self.svaOprema:
            if oprema.sifra==int(id):
                return oprema

    def vratiOpremuPoNazivu(self,naziv):
        for oprema in self.svaOprema:
            if oprema.naziv.upper() == naziv.upper():
                return oprema
