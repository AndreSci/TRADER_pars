from PyQt6 import QtWidgets, QtCore


# Функция не будет ничего возвращать так-как принимает список по ссылке и меняется на прямую через функцию
def table_new_button(self, number_row_item, list_new_button_tab, name_it):
    list_new_button_tab.append(QtWidgets.QPushButton(str(name_it)))
    list_new_button_tab[number_row_item - 1].setStyleSheet("QPushButton {\n"
                                                      "    border: 0px solid;\n"
                                                      "    background-color: rgb(109, 109, 109);\n"
                                                      "}\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: rgb(136, 136, 136);\n"
                                                      "\n"
                                                      "}\n"
                                                      "QPushButton:pressed {    \n"
                                                      "    background-color: rgb(85, 170, 255);\n"
                                                      "}")
    list_new_button_tab[number_row_item - 1].clicked.connect(lambda:
                                                             self.table_button_click(number_row_item)
                                                            )


def table_new_checkbox(self, number_row_item, list_new_button_tab, name_it):
    # только пример и ничего более!
    checkBox_1 = QtWidgets.QCheckBox('check')

    v_layout = QtWidgets.QVBoxLayout()  # поле для размещения
    v_layout.addWidget(checkBox_1)


def web_site_but(self, list_new_button_web, name_it=str):  # Принимает self.uiMwin, list(), имя сайта
    number_row_item = len(list_new_button_web)
    list_new_button_web.append(QtWidgets.QPushButton(name_it))

    list_new_button_web[number_row_item].setMinimumSize(QtCore.QSize(0, 20))
    list_new_button_web[number_row_item].setStyleSheet("QPushButton {\n"
                                    "    border: 0px solid;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    color: rgb(136, 136, 136);\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton:pressed {    \n"
                                    "    color: rgb(85, 170, 255);\n"
                                    "}")
    list_new_button_web[number_row_item].setObjectName(f"web_button_{number_row_item + 1}")
    self.uiMwin.verticalLayout_6.addWidget(list_new_button_web[number_row_item])

    list_new_button_web[number_row_item].clicked.connect(lambda: self.web_site_buttons_click(number_row_item))
