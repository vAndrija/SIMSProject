from model.KorisnickiNalog import *
from model.Administrator import *
from model.Urednik import *
from model.Mesto import *
from model.KuvarPocetnik import *
import json
import  jsonpickle

class ManipulacijaKorisnikom(object):
    def __init__(self):
        super().__init__()
        self.podaci = []
        self.sviKuvari = []
        self.sviUrednici = []
        self.administrator =None
        self.citanjeKorisnika()
        self.citajAdmineUrednike()



    def kreirajKorisnika(self, ime, prezime, kIme, lozinka, mejl, datum, adresa, mesto, postanskiBr, pol, sastojci, oprema,
                         recepti, kuvar, spisak, praceniKuvari, praceneKategorije):
        """
        Funkcija koja kreira novog korisnika, smesta ga u odgovarajucu listu i poziva funkciju koja
        upisuje korisnike u .json fajl.
        :param ime: ime novog korisnika
        :param prezime: prezime novog korisnika
        :param kIme: korisnicko ime novog korisnika
        :param lozinka: lozinka novog korisnika
        :param mejl: mejl novog korisnika
        :param datum: datum rodjenja novog korisnika
        :param adresa: adresa novog korisnika
        :param mesto: naziv mesta stanovanja novog korisnika
        :param postanskiBr: postanski broj mesta
        :param pol: pol novog korisnika
        :return:
        """
        grad = Mesto(mesto, postanskiBr)
        noviKorisnik = KuvarPocetnik(ime, prezime, kIme, lozinka, mejl, datum, adresa, grad, pol, sastojci, oprema, recepti,
                                     kuvar, spisak, praceniKuvari, praceneKategorije)


        self.sviKuvari.append(noviKorisnik)
        self.upisiKorisnika()
        return noviKorisnik

    def objToDict(self, obj):
        """
        Pomocna funkcija za redefinisanje serijalizacije za json paket
        :param obj:
        :return:
        """
        return  obj.__dict__

    def upisiKorisnika(self):
        """
        Funkcija koja vrsi serijalizaciju kuvara u kuvari.json fajl.
        :return:
        """
        with open('.\..\podaci\kuvari.json', 'w') as izlazniFajl:
            # json.dump(self.podaci, outfile, default=lambda  o: o.__dict__, indent=4)
            json.dump(self.sviKuvari, izlazniFajl, default= self.objToDict,  indent=4)

    def citanjeKorisnika(self):
        """
        Funnkcija koja ucitava kuvare iz fajla kuvari.json.
        :return:
        """
        # with open('.\..\podaci\kuvari.json', 'r') as outfile:
        #     self.sviKorisnici = json.load(outfile,default=lambda  o: o.__dict__,indent = 4)
        tekst = open('.\..\podaci\kuvari.json').read()
        if tekst == "":
            self.podaci = []
        else:
            self.podaci = jsonpickle.decode(tekst)

        for i in self.podaci:
            korisnik = KuvarPocetnik(**i)
            mesto = Mesto(**i['mesto'])
            korisnik.mesto = mesto
            self.sviKuvari.append(korisnik)


    def citajAdmineUrednike(self):
        """
        Funkcija koja ucitava administratore i urednike iz fajlova administratori.json i urednici.json.
        :return:
        """
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

    def vratiKuvara(self,korisnickoIme):
        for kuvar in self.sviKuvari:
            if(kuvar.korisnickoIme==korisnickoIme):
                return kuvar





