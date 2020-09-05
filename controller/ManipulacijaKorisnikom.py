from model.KorisnickiNalog import *
from model.Administrator import *
from model.Urednik import *
from model.Mesto import *
from model.KuvarPocetnik import *
import json
import  jsonpickle
import os
import shutil
import traceback

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

        osnovnaPutanja = os.getcwd()[:-4]
        shutil.copy(os.path.join(osnovnaPutanja, "dizajn", "sablonProfilKorisnika.html"),
                    os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika"))
        os.rename(os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika", "sablonProfilKorisnika.html"),
                  os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika", kIme + ".html"))

        sadrzaj = []
        with open(os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika", kIme + ".html"), "r") as stream:
            sadrzaj = stream.readlines()

        for i in range(len(sadrzaj)):
            if ('<h6 name="kIme">' in sadrzaj[i]):
                sadrzaj[i] = '<h6 name="kIme">{}</h6>\n'.format("Korisnicko ime: " + kIme)
            if ('<h6 name="ime">' in sadrzaj[i]):
                sadrzaj[i] = '<h6 name="kIme">{}</h6>\n'.format("Ime: " + ime)
            if ('<h6 name="kIme">' in sadrzaj[i]):
                sadrzaj[i] = '<h6 name="prezime">{}</h6>\n'.format("Prezime: " + prezime)

        with open(os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika", kIme + ".html"), "w") as output:
            output.writelines(sadrzaj)


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




