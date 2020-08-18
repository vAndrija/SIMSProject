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
    aplikacija = ProzorZaPrijavu()
    app.actionManager = ActionManager(aplikacija)
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()


