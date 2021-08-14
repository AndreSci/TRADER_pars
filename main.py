import sys
from PyQt6.QtWidgets import QApplication
from GUI import ImageDialog

def create_main_window():

    """ pyuic6 -x graphic_main.ui -o graphic_main.py """
    """ shift + F6 сменить имена нужной переменной в коде"""

    """ creating the graphic window class """

    app = QApplication(sys.argv)

    window = ImageDialog()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    create_main_window()
