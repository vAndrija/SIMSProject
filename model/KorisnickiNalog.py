import os


class KorisnickiNalog(object):
    def __init__(self, ime, prezime, korisnickoIme, lozinka, mejl, datumRodjenja, adresa, mesto, pol):
        self.korisnickoIme = korisnickoIme
        self.lozinka = lozinka
        self.ime = ime
        self.prezime = prezime
        self.mejl = mejl
        self.datumRodjenja = datumRodjenja
        self.adresa = adresa
        self.mesto = mesto
        self.pol = pol

    def promeniLozinku(self, novaLozinka):
        self.lozinka = novaLozinka

    def azurirajHtmlDokument(self, staroKorisnicko):
        osnovnaPutanja = os.getcwd()[:-4]
        with open(os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika", staroKorisnicko + ".html"), "r") as stream:
            sadrzaj = stream.readlines()

        os.remove(os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika", staroKorisnicko + ".html"))

        for i in range(len(sadrzaj)):
            if ('<h6 name="kIme">' in sadrzaj[i]):
                sadrzaj[i] = '<h6 name="kIme">{}</h6>\n'.format("Korisnicko ime: " + self.korisnickoIme)

        with open(os.path.join(osnovnaPutanja, "dizajn", "profilKorisnika", self.korisnickoIme + ".html"),
                  "w") as output:
            output.writelines(sadrzaj)

    def azurirajNalog(self, ime, prezime, korisnickoIme, mejl, datumRodjenja, adresa, nazivMesta, postanskiBroj, pol):
        self.ime = ime
        self.prezime = prezime
        self.korisnickoIme = korisnickoIme
        self.mejl = mejl
        self.datumRodjenja = datumRodjenja
        self.adresa = adresa
        self.mesto.nazivMesta = nazivMesta
        self.mesto.postanskiBroj = postanskiBroj
        self.pol = pol