import json
import  jsonpickle
from model.SpisakZaKupovinu import *
from PyQt5.QtWidgets import *

class ManipulacijaSpiskomZaKupovinu:

    def __init__(self):
        self.sviSpiskovi = []
        self.ucitajSpiskove()

    def objToDict(self, obj):
        """
        Pomocna funkcija za redefinisanje serijalizacije za json paket
        :param obj:
        :return:
        """

        return obj.__dict__
    def ucitajSpiskove(self):
        tekst = open('.\..\podaci\spiskovi.json').read()
        if tekst != "":
            self.podaci = jsonpickle.decode(tekst)
        else:
            return

        for podatak in self.podaci:
            spisak =SpisakZaKupovinu(**podatak)
            self.sviSpiskovi.append(spisak)

    def upisiSpiskove(self):
        """
        Funkcija koja vrsi serijalizaciju svih sastojaka iz liste u fajl sastojci.json.
        :return:
        """
        with open('.\..\podaci\spiskovi.json', 'w') as izlazniFajl:
            json.dump(self.sviSpiskovi, izlazniFajl, default=self.objToDict, indent=4)

    def kreirajSpisakZaKupovinu(self,kuvarPocetnik):
        id = None
        if len(self.sviSpiskovi) == 0:
            id = 0
        else:
            id = self.sviSpiskovi[-1].id+1
        novi = SpisakZaKupovinu(id,{},{})
        kuvarPocetnik.spisakZaKupovinu = id
        self.sviSpiskovi.append(novi)
        self.upisiSpiskove()

    def vratiSpisak(self,id):

        for spisak in self.sviSpiskovi:
            if spisak.id ==id:
                return spisak

