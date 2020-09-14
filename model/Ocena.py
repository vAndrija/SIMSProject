class Ocena(object):
    def __init__(self, vrednost, brojOcena, kuvari):
        self.vrednost = vrednost
        self.brojOcena = brojOcena
        self.kuvari = kuvari

    def azurirajOcenu(self, novaOcena, korisnickoIme):
        suma = self.vrednost * self.brojOcena + novaOcena
        self.brojOcena += 1
        self.vrednost = round(suma / self.brojOcena, 1)
        self.kuvari.append(korisnickoIme)
