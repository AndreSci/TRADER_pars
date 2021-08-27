from PyQt6 import QtWidgets


# Функция не будет ничего возвращать так-как принимает список по ссылке и меняется на прямую через функцию
def table_new_button(setup_main_window, number_row_item, list_new_button_tab, name_it):
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
                                                             setup_main_window.table_button_click(number_row_item)
                                                            )


def table_new_checkbox(setup_main_window, number_row_item, list_new_button_tab, name_it):
    # только пример и ничего более!
    checkBox_1 = QtWidgets.QCheckBox('check')

    v_layout = QtWidgets.QVBoxLayout()  # поле для размещения
    v_layout.addWidget(checkBox_1)