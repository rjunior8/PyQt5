import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt absolute positioning"
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        lbl = QLabel("Python", self)
        lbl.move(50, 50)
        lbl2 = QLabel("PyQt5", self)
        lbl2.move(100, 100)
        lbl3 = QLabel("Examples", self)
        lbl3.move(150, 150)
        lbl4 = QLabel("pythonspot.com", self)
        lbl4.move(200, 200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())