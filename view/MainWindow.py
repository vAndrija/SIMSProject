from PyQt5.QtWidgets import  *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.showMaximized()
        self.show()



