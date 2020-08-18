#Dodat komenar

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from controller.actions.ActionManager import *
from view.MainWindow import *
from view.ProzorZaPrijavu import *
import sys
def main():
    app = QApplication(sys.argv)
    # app.setStyle("fusion")
    # p = QPalette()
    # p.setColor(QPalette.Window, QColor(53, 53, 53))
    # p.setColor(QPalette.Button, QColor(53, 53, 53))
    # p.setColor(QPalette.Highlight, QColor(142, 45, 197))
    # p.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    # p.setColor(QPalette.WindowText, QColor(255, 255, 255))
    #
    # app.setPalette(p)
    source = ""
    # with open("C:\\Users\korisnik\Desktop\stajl.qss","r") as fp:
    #     source = fp.read()
    # app.setStyleSheet(source)



    aplikacija = ProzorZaPrijavu()
    app.actionManager = ActionManager(aplikacija)
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()