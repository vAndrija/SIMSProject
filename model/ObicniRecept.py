from model.Recept import *

class ObicniRecept(Recept):
    def __init__(self,id,naziv,oprema,sastojci,kategorije,ocena,ekstenzijaSlike,opis):
        super().__init__(id,naziv,oprema,sastojci,kategorije,ocena,ekstenzijaSlike)
        self.opis = opis