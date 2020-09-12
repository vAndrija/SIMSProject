class Sastojak(object):
    def __init__(self, sifra, naziv, tipKolicine):
        self.sifra = sifra
        self.naziv = naziv
        self.tipKolicine = tipKolicine

    def __hash__(self):
        return hash(self.sifra)
