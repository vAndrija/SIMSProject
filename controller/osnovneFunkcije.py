from PyQt5.QtWidgets import *
def provjeraPostojanjaKorisnika(korisnickoIme,lozinka):
    baza=QApplication.instance().actionManager.informacije
    for kuvar in baza.sviKuvari:
        if(kuvar.korisnickoIme==korisnickoIme and kuvar.lozinka ==lozinka):
            return kuvar
    for urednik in baza.sviUrednici:
        if(urednik.korisnickoIme==korisnickoIme and urednik.lozinka==lozinka):
            return urednik
    if baza.administrator.korisnickoIme==korisnickoIme and baza.administrator.lozinka==lozinka:
        return baza.administrator
    return None

def nadjiKorisnika(korisnickoIme):
    baza = QApplication.instance().actionManager.informacije
    for kuvar in baza.sviKuvari:
        if kuvar.korisnickoIme == korisnickoIme:
            return kuvar
    return None

