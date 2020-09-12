from PyQt5.QtWidgets import *


def provjeraPostojanjaKorisnika(korisnickoIme, lozinka):
    baza = QApplication.instance().actionManager.informacije
    for kuvar in baza.sviKuvari:
        if (kuvar.korisnickoIme == korisnickoIme and kuvar.lozinka == lozinka):
            return kuvar
    for urednik in baza.sviUrednici:
        if (urednik.korisnickoIme == korisnickoIme and urednik.lozinka == lozinka):
            return urednik
    if baza.administrator.korisnickoIme == korisnickoIme and baza.administrator.lozinka == lozinka:
        return baza.administrator
    return None


def nadjiKorisnika(korisnickoIme):
    baza = QApplication.instance().actionManager.informacije
    for kuvar in baza.sviKuvari:
        if kuvar.korisnickoIme == korisnickoIme:
            return kuvar
    return None


def nadjiSastojke(sastojci):
    nadjenjiSastojci = []
    for sastojak in sastojci:
        for sastojakUBazi in QApplication.instance().actionManager.sastojciMenadzer.sviSastojci:
            if sastojak == sastojakUBazi.sifra:
                nadjenjiSastojci.append(sastojakUBazi)
                break
    return nadjenjiSastojci


def nadjiOpremu(oprema):
    nadjenaOprema = []
    for aparat in oprema:
        for aparatUBazi in QApplication.instance().actionManager.opremaMenadzer.svaOprema:
            if aparat == aparatUBazi.sifra:
                nadjenaOprema.append(aparatUBazi)
    return nadjenaOprema


def azurirajKuvara(staroKorisnicko, azuriranKuvar):
    for kuvar in QApplication.instance().actionManager.informacije.sviKuvari:
        if kuvar.korisnickoIme == staroKorisnicko:
            kuvar = azuriranKuvar
    QApplication.instance().actionManager.informacije.upisiKorisnika()
