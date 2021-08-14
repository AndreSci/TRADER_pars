import sys
from PyQt6.QtWidgets import QDialog, QWidget, QApplication, QMainWindow
from graphic_main import Ui_Dialog

class ImageDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.uiMwin = Ui_Dialog()
        self.uiMwin.setupUi(self)

       # self.uiMwin.pushButton.clicked.connect(self.some)

    def some(self):
        print("Hello")