import json

import jsonpickle

from model.VirtuelniKuvar import *


class ManipulacijaVirtuelnimKuvarom:

    def __init__(self):
        self.sviVirtuelniKuvari = []
        self.ucitajVirtuelneKuvare()

    def objToDict(self, obj):
        """
        Pomocna funkcija za redefinisanje serijalizacije za json paket
        :param obj:
        :return:
        """

        return obj.__dict__

    def ucitajVirtuelneKuvare(self):
        try:
            tekst = open('.\..\podaci\\virtuelniKuvar.json').read()
            if tekst != "":
                self.podaci = jsonpickle.decode(tekst)
            else:
                return

            for podatak in self.podaci:
                vKuvar = VirtuelniKuvar(**podatak)
                self.sviVirtuelniKuvari.append(vKuvar)
        except:
            pass

    def upisiVirtuelneKuvare(self):
        """
        Funkcija koja vrsi serijalizaciju svih sastojaka iz liste u fajl sastojci.json.
        :return:
        """
        with open('.\..\podaci\\virtuelniKuvar.json', 'w') as izlazniFajl:
            json.dump(self.sviVirtuelniKuvari, izlazniFajl, default=self.objToDict, indent=4)

    def kreirajVirtuelniKuvar(self, kuvarPocetnik):
        id = None
        if len(self.sviVirtuelniKuvari) == 0:
            id = 0
        else:
            id = self.sviVirtuelniKuvari[-1].id + 1
        novi = VirtuelniKuvar(id, "", [])
        kuvarPocetnik.virtuelniKuvar = id
        self.sviVirtuelniKuvari.append(novi)
        self.upisiVirtuelneKuvare()

    def vratiVirtuelniKuvar(self, id):

        for vKuvar in self.sviVirtuelniKuvari:
            if vKuvar.id == id:
                return vKuvar
