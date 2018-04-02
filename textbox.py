import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 textbox"
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        self.btn = QPushButton("Show text", self)
        self.btn.move(20, 80)
        self.btn.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        text_box_value = self.textbox.text()
        QMessageBox.question(self, "Message - pythonspot.com", "You typed: " + text_box_value, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())