import sys
from PyQt6.QtWidgets import QApplication
from gui_function import ImageDialog
from pars_func import ru_trade24_ru


def create_main_window():

    """ pyuic6 -x graphic_main.ui -o graphic_main.py """
    """ shift + F6 сменить имена нужной переменной в коде"""

    """ creating the graphic window class """

    app = QApplication(sys.argv)

    window = ImageDialog()
    window.show()

    window.create_web_list()

    sys.exit(app.exec())


if __name__ == "__main__":
    create_main_window()

