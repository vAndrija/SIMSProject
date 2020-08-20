class Sastojak(object):
    def __init__(self):
        self.sifra = None
        self.naziv = None
        self.tipKolicine = None

    def __hash__(self):
        return hash(self.sifra)