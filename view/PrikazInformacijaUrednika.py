from view.ObavestavajucaPoruka import *


class PrikazInformacijaUrednika(QDialog):
    def __init__(self, urednik, parent):
        super().__init__()
        self.parent = parent
        self.urednik = urednik
        self.initUI()
        self.inicijalizujGrid()

        self.exec_()

    def initUI(self):
        self.setWindowTitle("Prikaz profila")
        self.setFixedSize(800, 800)
        image = QImage("..\slike\\urednik.jpg")
        sImage = image.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        icon = QIcon("..\slike\ikonica.png")
        self.setWindowIcon(icon)
        sadrzaj = ""
        with open("..\slike\stajl.css", "r") as stream:
            sadrzaj = stream.read()
        self.setStyleSheet(sadrzaj)

    def inicijalizujGrid(self):
        grid = QGridLayout()
        self.setLayout(grid)

        matrica = ['Ime:', '1', '',
                   'Prezime:', '2', '',
                   'Korisnicko ime:', '3', '',
                   'Azurirajte korisnicko ime:', '/', '',
                   'Mejl:', '4', '',
                   'Datum rodjenja:', '5', '',
                   'Adresa:', '6', '',
                   'Naziv mesta:', '7', '',
                   'Azurirajte naziv mesta:', '*', '',
                   'Postanski broj:', '8', '',
                   'Azurirajte postanski broj:', '-', '',
                   'Pol:', '9', '',
                   'Broj recepata koje nije uredio:', '10', '',
                   '', '11', '',
                   '', '12', '',
                   ]

        pozicije = [(i, j) for i in range(18) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):
            if sadrzaj == "1":
                labela = QLabel(self.urednik.ime)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "2":
                labela = QLabel(self.urednik.prezime)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "3":
                self.kIme = QLabel(self.urednik.korisnickoIme)
                self.kIme.setFixedSize(170, 20)
                grid.addWidget(self.kIme, *pozicija)
            elif sadrzaj == "4":
                labela = QLabel(self.urednik.mejl)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "5":
                labela = QLabel(self.urednik.datumRodjenja)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "6":
                labela = QLabel(self.urednik.adresa)
                labela.setFixedSize(170, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "7":
                self.mesto = QLabel(self.urednik.mesto.nazivMesta)
                self.mesto.setFixedSize(170, 20)
                grid.addWidget(self.mesto, *pozicija)
            elif sadrzaj == "8":
                self.postanskiBr = QLabel(self.urednik.mesto.postanskiBroj)
                self.postanskiBr.setFixedSize(170, 20)
                grid.addWidget(self.postanskiBr, *pozicija)
            elif sadrzaj == "9":
                if self.urednik.pol == 0:
                    pol = "Zenski"
                else:
                    pol = "Muski"
                labela = QLabel(pol)
                labela.setFixedSize(250, 20)
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "10":
                labela = QLabel(str(len(self.urednik.noviRecepti)))
                grid.addWidget(labela, *pozicija)
            elif sadrzaj == "11":
                dugme = QPushButton("Azuriraj nalog")
                dugme.clicked.connect(self.azurirajNalog)
                dugme.setFixedWidth(300)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "12":
                dugme = QPushButton("Obrisi nalog")
                dugme.setFixedWidth(300)
                dugme.clicked.connect(self.obrisiNalog)
                grid.addWidget(dugme, *pozicija)
            elif sadrzaj == "/":
                self.novoKIme = QLineEdit()
                self.novoKIme.setFixedWidth(140)
                self.novoKIme.setText(self.urednik.korisnickoIme)
                grid.addWidget(self.novoKIme, *pozicija)
            elif sadrzaj == "*":
                self.novoMesto = QLineEdit()
                self.novoMesto.setFixedWidth(140)
                self.novoMesto.setText(self.urednik.mesto.nazivMesta)
                grid.addWidget(self.novoMesto, *pozicija)
            elif sadrzaj == "-":
                self.noviPostanskiBr = QLineEdit()
                self.noviPostanskiBr.setFixedWidth(140)
                self.noviPostanskiBr.setText(self.urednik.mesto.postanskiBroj)
                grid.addWidget(self.noviPostanskiBr, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(210, 20)
                grid.addWidget(labela, *pozicija)

    def obrisiNalog(self):
        potvrda = QMessageBox
        odgovor = potvrda.question(self, '', "Da li ste sigurni da zelite da obrisete nalog?", potvrda.Yes | potvrda.No)
        if odgovor == potvrda.Yes:
            QApplication.instance().actionManager.informacije.obrisiUrednika(self.urednik)
            QApplication.instance().actionManager.informacije.upisiUrednike()
            self.parent.refresujStranu()
            self.parent.refresujTab2()
            self.hide()

    def azurirajNalog(self):
        if self.novoKIme.text() == "" and self.novoMesto.text() == "" and self.noviPostanskiBr.text() == "":
            ObavestavajucaPoruka("Niste uneli nove podatke.")
        else:
            if self.novoKIme.text() != "":
                staroKorisnicko = self.urednik.korisnickoIme
                self.urednik.korisnickoIme = self.novoKIme.text()
                self.kIme.setText(self.novoKIme.text())
                self.urednik.azurirajHtmlDokument(staroKorisnicko)
                # QApplication.instance().actionManager.informacije.azurirajHtmlDokument(self.urednik, staroKorisnicko)

            if self.novoMesto.text() != "":
                self.urednik.mesto.nazivMesta = self.novoMesto.text()
                self.mesto.setText(self.novoMesto.text())

            if self.noviPostanskiBr.text() != "":
                self.urednik.mesto.postanskiBroj = self.noviPostanskiBr.text()
                self.postanskiBr.setText(self.noviPostanskiBr.text())
            QApplication.instance().actionManager.informacije.upisiUrednike()
            # QApplication.instance().actionManager.informacije.citanjeKorisnika()
            self.parent.refresujStranu()
            self.parent.refresujTab2()
            # mozda obrisati liniju ispod
            self.hide()
