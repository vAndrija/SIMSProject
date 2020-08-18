class Recept(object):
    def __init__(self):
        self.id = None
        self.naziv = None
        self.oprema = []
        self.sastojci = {}
        self.kategorije = []
        self.ocena = None