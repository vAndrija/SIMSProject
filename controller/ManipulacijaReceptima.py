from model.ObicniRecept import *
import json
import os
import  jsonpickle
import shutil
class ManipulacijaReceptima():
    def __init__(self):
        self.recepti = []
        self.ucitajRecepte()
        self.kreirajRecept()

    def ucitajRecepte(self):
        tekst = open('.\..\podaci\\recepti.json').read()
        tekst = jsonpickle.decode(tekst)
        for item in tekst:
            recept = ObicniRecept(**item)
            self.recepti.append(recept)

    def objToDict(self, obj):
        return  obj.__dict__

    def sacuvajRecepte(self):
        with open('.\..\podaci\\recepti.json',"w") as stream:
            json.dump(self.recepti, stream, default=self.objToDict, indent=4)


    def kreirajRecept(self):
        #premjestanje fajla slike koji je ucitan prilikom dodavanja recepta
        putanja  =  os.path.join(os.getcwd()[:-4],'slike')
        putanjaSlike = "C:\\Users\\korisnik\\Desktop\\SIMS\\sampita.jpg"
        ekstenzija = "."+putanjaSlike.split(".")[1]
        shutil.move(putanjaSlike, putanja)
        os.rename(os.path.join(putanja,"sampita.jpg"),os.path.join(putanja,str(1)+".jpg"))

