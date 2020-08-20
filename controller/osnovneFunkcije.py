from PyQt5.QtWidgets import *
def provjeraPostojanjaKorisnika(korisnickoIme,lozinka):
    baza=QApplication.instance().actionManager.informacije
    for kuvar in baza.sviKuvari:
        if(kuvar.korisnickoIme==korisnickoIme and kuvar.lozinka ==lozinka):
            return 0
    for urednik in baza.sviUrednici:
        if(urednik.korisnickoIme==korisnickoIme and urednik.lozinka==lozinka):
            return 1
    if baza.administrator.korisnickoIme==korisnickoIme and baza.administrator.lozinka==lozinka:
        return 2
    return 3

