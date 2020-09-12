import sys

from controller.actions.ActionManager import *
from view.ProzorZaPrijavu import *


def main():
    app = QApplication(sys.argv)
    aplikacija = ProzorZaPrijavu()
    app.actionManager = ActionManager(aplikacija)
    app.actionManager.glavniProzor = None
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
