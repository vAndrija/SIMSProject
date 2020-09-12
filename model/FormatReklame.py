from enum import Enum

class FormatReklame:
    PUNAREKLAMA =0
    POLUREKLAMA =1
    OBICNAREKLAMA =2

    def __str__(self):
        return self.name