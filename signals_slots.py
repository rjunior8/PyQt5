import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QMenu, QMenuBar, QPushButton, QSpinBox,
                             QTextEdit, QVBoxLayout)

class Dialog(QDialog):
    def slot_method(self):
        print("slot method called.")

    def __init__(self):
        super(Dialog, self).__init__()
        btn = QPushButton("Click")
        btn.clicked.connect(self.slot_method)
        main_layout = QVBoxLayout()
        main_layout.addWidget(btn)
        self.setLayout(main_layout)
        self.setWindowTitle("Button Example")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())