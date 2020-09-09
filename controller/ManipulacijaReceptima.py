import json
import os
import shutil
import traceback
from model.Kategorija import *
import jsonpickle
from PyQt5.QtWidgets import *

from model.ObicniRecept import *


class ManipulacijaReceptima():
    def __init__(self):
        self.recepti = []
        self.kategorije = []
        self.receptiPrijavljenog = []

        self.ucitajKategorije()
        self.ucitajRecepte()
        #self.kreirajRecept("Piletina","C:\\Users\\korisnik\\Desktop\piletina.jpeg",
                           #"Glavno jelo za posebne prilike",[],["glavno jelo","ukusno"],{})

    def ucitajRecepte(self):
        """
        Funkcija ucitava sadrzaj iz .json fajla i kastuje ih u objekte ObicniRecept klase
        :return:
        """
        tekst = open('.\..\podaci\\recepti.json').read()
        tekst = jsonpickle.decode(tekst)
        for item in tekst:
            recept = ObicniRecept(**item)
            self.recepti.append(recept)



    def ucitajKategorije(self):
        tekst=  open('.\..\podaci\\kategorije.json').read()
        tekst= jsonpickle.decode(tekst)
        for item in tekst:
            kategorija = Kategorija(**item)
            self.kategorije.append(kategorija)

    def dodajKategoriju(self,naziv):
        kategorija= Kategorija(len(self.kategorije),naziv)
        self.kategorije.append(kategorija)
        self.sacuvajKategorije()

    def objToDict(self, obj):
        """
        Pomocna funkcija za redefinisanje serijalizacije za json paket
        :param obj:
        :return:
        """
        return obj.__dict__

    def sacuvajRecepte(self):
        """
        Funkcija vrsi serijalizaciju svih recepata iz liste u recepti.json fajl
        :return:
        """
        with open('.\..\podaci\\recepti.json', "w") as stream:
            json.dump(self.recepti, stream, default=self.objToDict, indent=4)


    def sacuvajKategorije(self):
        with open('.\..\podaci\\kategorije.json', "w") as stream:
            json.dump(self.kategorije, stream, default=self.objToDict, indent=4)


    def izbrisiRecept(self,id):
        for recept in self.recepti:
            if recept.id == id:

                recept.kategorije = []
                recept.naziv += '.-.'


    def kreirajRecept(self, naziv, putanjaSlike, opis, oprema, kategorije, sastojci):
        """
        Funkcija izvrsava kreiranje novog recepta u sledecim koracima:
        1. Premjesta sliku sa dobijene putanje u folder slike i mijenja joj naziv po predefinisanom pravilu
        2. Kreira izgled za nju radi prikazivanja na pocetnoj strani tako sto .html sablon kreira u
        odgovaarajuci folder i preimenuje ga prema predefinisanom pravilu
        3. Mijenja sadrzaj .html sablona da bi se prikazivala slika recepta i naziv novog recepta
        4. Kreira objekat tipa ObicanRecept, dodaje ga u listu svih recepata i vrsi njegovo serijalizovanje
        :param naziv: naziv recepta
        :param putanjaSlike:  putanja do slike recepta
        :param opis: opis recepta
        :param oprema:  oprema potreban za izradu recepta
        :param kategorije:  kategorije kojima pripada recept
        :param sastojci: sastojci koji idu u recept
        :return:
        """
        osnovnaPutanja = os.getcwd()[:-4]
        putanja = os.path.join(osnovnaPutanja, 'dizajn')
        ekstenzija =  putanjaSlike.split(".")[1]
        nazivSlike = putanjaSlike.split("/")[-1]
        id = self.recepti[-1].id + 1
        noviRecept = ObicniRecept(id, naziv, oprema, sastojci, kategorije, 0, ekstenzija, opis)
        shutil.move(putanjaSlike, putanja)
        os.rename(os.path.join(putanja, nazivSlike), os.path.join(putanja, str(id) +"." +ekstenzija))
        shutil.copy(os.path.join(osnovnaPutanja, "dizajn", "sablonPocetna.html"),
                    os.path.join(osnovnaPutanja, "dizajn", "pocetnaRecepti"))
        os.rename(os.path.join(osnovnaPutanja, "dizajn", "pocetnaRecepti", "sablonPocetna.html"),
                  os.path.join(osnovnaPutanja, "dizajn", "pocetnaRecepti", str(id) + ".html"))
        sadrzaj = []
        with open(os.path.join(osnovnaPutanja, "dizajn", "pocetnaRecepti", str(id) + ".html"), "r") as stream:
            sadrzaj = stream.readlines()

        for i in range(len(sadrzaj)):
            if ("<img src=" in sadrzaj[i]):
                sadrzaj[
                    i] = '<div class="box"><img src="{0}" class="rounded float-right" alt="Responsive image">\n'.format(
                    "..\\" + str(id) +"."+ ekstenzija)
            if ('<h3 class="name">' in sadrzaj[i]):
                sadrzaj[i] = '<h3 class="name">{}</h3>\n'.format(naziv)
        with open(os.path.join(osnovnaPutanja, "dizajn", "pocetnaRecepti", str(id) + ".html"), "w") as output:
            output.writelines(sadrzaj)

        self.recepti.append(noviRecept)
        self.sacuvajRecepte()
        QApplication.instance().actionManager.prijavljeniKorisnik.recepti.append(id)
        QApplication.instance().actionManager.informacije.upisiKorisnika()


    def receptiPretraga(self, naziv, kategorije,napredno):
        korisnik = QApplication.instance().actionManager.prijavljeniKorisnik
        try:
            povratna = []
            nedostajeOpreme = []
            nedostajeSastojaka = []
            for recept in self.recepti:

                if ( naziv!="" and (naziv.lower() in recept.naziv.lower())):
                    povratna.append(recept)
                    nedostajeOpreme.append(0)
                    nedostajeSastojaka.append(0)
                    for sastojak in recept.sastojci.keys():
                        postoji = False
                        for dugotrajni in korisnik.dugotrajniSastojci:
                            if(dugotrajni==sastojak):
                                postoji =True
                                break
                        if not postoji:
                            nedostajeSastojaka[len(povratna)-1]+=1
                    for oprema in recept.oprema:
                        postoji = False
                        for opremaKuvar in korisnik.oprema:
                            if oprema==opremaKuvar:
                                postoji=True
                                break
                        if not postoji:
                            nedostajeOpreme[len(povratna)-1]+=1
                    continue
                for kategorija in recept.kategorije:
                    if (kategorija in kategorije):
                        povratna.append(recept)
                        nedostajeOpreme.append(0)
                        nedostajeSastojaka.append(0)
                        for sastojak in recept.sastojci.keys():
                            postoji = False
                            for dugotrajni in korisnik.dugotrajniSastojci:
                                if (dugotrajni == sastojak):
                                    postoji = True
                                    break
                            if not postoji:
                                nedostajeSastojaka[len(povratna) - 1] += 1
                        for oprema in recept.oprema:
                            postoji = False
                            for opremaKuvar in korisnik.oprema:
                                if oprema == opremaKuvar:
                                    postoji = True
                                    break
                            if not postoji:
                                nedostajeOpreme[len(povratna) - 1] += 1
                        break
            QApplication.instance().actionManager.glavniProzor.inicijalizujPocetnu()
            QApplication.instance().actionManager.glavniProzor.sledecaPostoji =True
            QApplication.instance().actionManager.glavniProzor.sledecaStranicaBrojac = 0
            QApplication.instance().actionManager.glavniProzor.refresujPocetnu(povratna,nedostajeOpreme,nedostajeSastojaka,napredno)

        except:
            traceback.print_exc()

    def vratiRecept(self, id):
        for recept in self.recepti:
            if (recept.id == id):
                return recept




    def vratiIdKategorije(self,naziv):
        for kategorija in self.kategorije:
            if(kategorija.naziv.lower()==naziv.lower()):
                return kategorija.id


    def vracanjeToolTipSadrzaja(self,recept):

        sadrzaj ='<ul>Stvari koje nedostaju<br/>'
        kuvarPocetnik = QApplication.instance().actionManager.prijavljeniKorisnik
        for oprema in recept.oprema:
            postoji=False
            for opremaKuvar in kuvarPocetnik.oprema:
                if(oprema==opremaKuvar):
                    postoji=True
                    break
            if not postoji:
                objekat = QApplication.instance().actionManager.opremaMenadzer.vratiOpremu(oprema)
                sadrzaj +='<li>{0}</li>'.format(objekat.naziv)
        for sastojak in recept.sastojci.keys():
            postoji=False
            for dugotrajniSastojak in kuvarPocetnik.dugotrajniSastojci:
                if(sastojak==dugotrajniSastojak):
                    postoji=True
                    break
            if not postoji:
                objekat = QApplication.instance().actionManager.sastojciMenadzer.vratiSastojak(sastojak)
                sadrzaj +='<li>{0}</li>'.format(objekat.naziv)
        sadrzaj+='</ul>'
        return sadrzaj

    def receptiZaPrikaz(self):
        """
        Funkcija za ulogovanog kuvara pocetnika vraca sve recepte iz kategorija koje on prati
        i sve recepte od korisnika koje on prati radi prikazivanja na pocetnoj strani
        :return: lista recepata
        """
        recepti = []
        kuvarPocetnik = QApplication.instance().actionManager.prijavljeniKorisnik
        for pracenaKategorija in kuvarPocetnik.praceneKategorije:
            for recept in self.recepti:
                for kategorija in recept.kategorije:
                    if (kategorija == pracenaKategorija):
                        postoji = False
                        for postojeci in recepti:
                            if (recept.id == postojeci.id):
                                postoji = True
                        if not postoji:
                            recepti.append(recept)
                        break
        for praceniKuvar in kuvarPocetnik.praceniKuvari:
            kuvar = QApplication.instance().actionManager.informacije.vratiKuvara(praceniKuvar)
            for receptId in kuvar.recepti:
                recept = self.vratiRecept(receptId)
                postoji = False
                for postojeci in recepti:
                    if (recept.id == postojeci.id):
                        postoji = True
                if not postoji:
                    recepti.append(recept)

        return recepti


    def vratiNaziveKategorija(self):

        povratna=[]
        for kategorija in self.kategorije:
            povratna.append(kategorija.naziv)

        return povratna

    def postojanjeKategorije(self,naziv):
        for kategorija in self.kategorije:
            if(naziv.lower() == kategorija.naziv.lower()):
                return kategorija.id
        return -1


    def vratiNazivKategorije(self,id):
        for kategorija in self.kategorije:
            if kategorija.id==id:
                return kategorija.naziv

    def vratiKategoriju(self,naziv):
        for kategorija in self.kategorije:
            if(naziv.lower()==kategorija.naziv.lower()):
                return kategorija


    def pronadjiReceptePrijavljenog(self):
        kuvarPocetnik = QApplication.instance().actionManager.prijavljeniKorisnik
        recepti = kuvarPocetnik.recepti
        for id in recepti:
            for recept in self.recepti:
                if recept.id == id:
                    self.receptiPrijavljenog.append(recept)