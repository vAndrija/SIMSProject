from view.ObavestavajucaPoruka import *


class ProzorZaPromenuLozinke(QDialog):
    def __init__(self, korisnik):
        super().__init__()
        self.korisnik = korisnik
        self.initUI()
        self.inicijalizujGrid()

        self.exec_()

    def initUI(self):
        self.setWindowTitle("Promena lozinke")
        self.setFixedSize(400, 500)
        image = QImage("..\slike\lozinka.png")
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

        matrica = ['', '', '',
                   '', '', '',
                   '', '', '',
                   '', '', '',
                   'Unesite staru lozinku:', '', '',
                   '*', '', '',
                   'Unesite novu lozinku:', '', '',
                   '^', '', '',
                   'Ponovo unesite novu lozinku:', '', '',
                   '/', '', '',
                   '', '', '',
                   '+', '', '',
                   '', '', '',
                   ]

        pozicije = [(i, j) for i in range(13) for j in range(3)]

        for pozicija, sadrzaj in zip(pozicije, matrica):

            if sadrzaj == "*":
                self.staraLozinka = QLineEdit()
                self.staraLozinka.setFixedSize(200, 25)
                self.staraLozinka.setEchoMode(QLineEdit.Password)
                grid.addWidget(self.staraLozinka, *pozicija)
            elif sadrzaj == "^":
                self.novaLozinka = QLineEdit()
                self.novaLozinka.setFixedSize(200, 25)
                self.novaLozinka.setEchoMode(QLineEdit.Password)
                grid.addWidget(self.novaLozinka, *pozicija)
            elif sadrzaj == "/":
                self.novaLozinkaPonovo = QLineEdit()
                self.novaLozinkaPonovo.setFixedSize(200, 25)
                self.novaLozinkaPonovo.setEchoMode(QLineEdit.Password)
                grid.addWidget(self.novaLozinkaPonovo, *pozicija)
            elif sadrzaj == "+":
                dugme = QPushButton("Promeni lozinku")
                dugme.clicked.connect(self.promeniLozinku)
                grid.addWidget(dugme, *pozicija)
            else:
                labela = QLabel(sadrzaj)
                labela.setFixedSize(240, 20)
                grid.addWidget(labela, *pozicija)

    def promeniLozinku(self):
        if QApplication.instance().actionManager.prijavljeniKorisnik.lozinka != self.staraLozinka.text():
            ObavestavajucaPoruka("Uneta stara lozinka nije ispravna. Pokusajte ponovo.")
            self.staraLozinka.setText("")
        else:
            if self.novaLozinka.text() != self.novaLozinkaPonovo.text():
                ObavestavajucaPoruka("Nova lozinka i ponovljena nova lozinka se ne poklapaju. Pokusajte ponovo.")
                self.novaLozinka.setText("")
                self.novaLozinkaPonovo.setText("")
            else:
                QApplication.instance().actionManager.informacije.promeniLozinkuPrijavljenom(self.novaLozinka.text())
                ObavestavajucaPoruka("Uspesno ste promenili lozinku.")
                self.close()
