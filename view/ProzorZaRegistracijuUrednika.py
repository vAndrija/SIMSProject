from view.ProzorZaRegistraciju import *


class ProzorZaRegistracijuUrednika(ProzorZaRegistraciju):
    def __init__(self):
        super().__init__()
        self.dodajDugmeRegistracije()

    def dodajOpremuISastojke(self):
        pass

    def dodajDugmeRegistracije(self):
        dugme = QPushButton("Registrujte se")
        dugme.setFixedSize(250, 30)
        dugme.clicked.connect(self.registracija)
        self.grid.addWidget(dugme, 11, 3)

    def registracija(self):
        ime = self.tekstovi[0].text()
        prezime = self.tekstovi[1].text()
        kIme = self.tekstovi[2].text()
        lozinka = self.tekstovi[3].text()
        ponovnaLozinka = self.tekstovi[4].text()
        mejl = self.tekstovi[5].text()
        adresa = self.tekstovi[6].text()
        mesto = self.tekstovi[7].text()
        ppt = self.tekstovi[8].text()
        pol = self.pol.currentIndex()
        datum = self.datum.date().toPyDate()
        if ime == "" or prezime == "" or kIme == "" or lozinka == "" or mejl == "" or adresa == "" or mesto == "" or ppt == "":
            ObavestavajucaPoruka("Niste popunili sva polja.")
        else:
            if lozinka != ponovnaLozinka:
                ObavestavajucaPoruka("Vasa lozinka nije ispravna.")
            self.registrovaniKorisnik = QApplication.instance().actionManager.informacije.kreirajUrednika(ime, prezime,
                                                                                                          kIme, lozinka,
                                                                                                          mejl,
                                                                                                          str(datum),
                                                                                                          adresa, mesto,
                                                                                                          ppt, pol, [])
            self.hide()
