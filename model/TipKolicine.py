from enum import Enum

class TipKolicine(Enum):
    GRAM = 0
    DL = 1
    KOMAD = 2
    SUPENAKASIKA = 3
    PRSTOHVAT = 4

    def __str__(self):
        return self.name