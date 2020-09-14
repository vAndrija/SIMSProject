import os

class Recept(object):
    def __init__(self, id, naziv, oprema, sastojci, kategorije, ocena, ekstenzijaSlike):
        self.id = id
        self.naziv = naziv
        self.oprema = oprema
        self.sastojci = sastojci
        self.kategorije = kategorije
        self.ocena = ocena
        self.ekstenzijaSlike = ekstenzijaSlike


    def izbrisiRecept(self):
        self.kategorije = []
        self.naziv += '.-.'


    def azurirajHtmlDokument(self):
        osnovnaPutanja = os.getcwd()[:-4]
        putanja = os.path.join(osnovnaPutanja, 'dizajn')
        with open(os.path.join(osnovnaPutanja, "dizajn", "pocetnaRecepti", str(self.id) + ".html"), "r") as stream:
            sadrzaj = stream.readlines()

        for i in range(len(sadrzaj)):
            if ('<h3 class="name">' in sadrzaj[i]):
                sadrzaj[i] = '<h3 class="name">{}</h3>\n'.format(self.naziv)
        with open(os.path.join(osnovnaPutanja, "dizajn", "pocetnaRecepti", str(self.id) + ".html"), "w") as output:
            output.writelines(sadrzaj)

    def proveriPrethodnoOcenjivanje(self, korisnik):
        for korisnicko in self.ocena.kuvari:
            if korisnicko == korisnik.korisnickoIme:
                return True
        return False

    def dodajOcenuReceptu(self, novaOcena, korisnickoIme):
        self.ocena.azurirajOcenu(novaOcena, korisnickoIme)
