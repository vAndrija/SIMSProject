from model.Recept import *

class ObicniRecept(Recept):
    def __init__(self,id,naziv,oprema,sastojci,kategorije,ocena,opis):
        super().__init__(id,naziv,oprema,sastojci,kategorije,ocena)
        self.opis = opis