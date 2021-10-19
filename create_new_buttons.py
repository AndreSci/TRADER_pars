from PyQt6 import QtWidgets, QtCore, QtGui


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

# ------------------------------------------------------------------------------


def table_new_checkbox(self, number_row_item, list_new_button_tab, name_it):
    # только пример и ничего более!
    checkBox_1 = QtWidgets.QCheckBox('check')

    v_layout = QtWidgets.QVBoxLayout()  # поле для размещения
    v_layout.addWidget(checkBox_1)

# ------------------------------------------------------------------------------


def web_site_but(self, list_new_button_web, name_it=str):  # Принимает self.uiMwin, list(), имя сайта
    number_row_item = len(list_new_button_web)
    list_new_button_web.append(QtWidgets.QPushButton(str(name_it)))

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

# ------------------------------------------------------------------------------


def like_but_conf(self, name_it_web, number):
    print(f"push = {name_it_web}: {number}")

    try:
        if self.dict_button_liked[name_it_web][number] == 0:
            self.dict_button_liked[name_it_web][number] = 1
        elif self.dict_button_liked[name_it_web][number] == 1:
            self.dict_button_liked[name_it_web][number] = 0
    except:
        self.dict_button_liked[name_it_web][number] = 1


# ------------------------------------------------------------------------------


def like_table_button(self, name_it_web=str, number=str):
    # Принимает self.uiMwin, dict(), сайт и номер объявления

    self.dict_new_button_like[name_it_web] = dict()
    self.dict_new_button_like[name_it_web][number] = QtWidgets.QPushButton(str(number))
    self.dict_new_button_like[name_it_web][number].setStyleSheet("QPushButton {\n"
                                                      "    border: 0px solid;\n"
                                                    " background-color: rgb(211, 211, 211);\n"
                                                      "}")

    self.dict_new_button_like[name_it_web][number].setText("")
    self.dict_new_button_like[name_it_web][number].setCheckable(True)

    try:
        if self.dict_button_liked[name_it_web][number] == 1:
            self.dict_new_button_like[name_it_web][number].setChecked(True)
        else:
            self.dict_new_button_like[name_it_web][number].setChecked(False)
    except:
        if name_it_web not in self.dict_button_liked:
            self.dict_button_liked[name_it_web] = dict()
        if number not in self.dict_button_liked[name_it_web]:
            self.dict_button_liked[name_it_web][number] = int()

        self.dict_button_liked[name_it_web][number] = 0
        self.dict_new_button_like[name_it_web][number].setChecked(False)

    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("image_file/like_off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    icon2.addPixmap(QtGui.QPixmap("image_file/like_on.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
    self.dict_new_button_like[name_it_web][number].setIcon(icon2)
    self.dict_new_button_like[name_it_web][number].setIconSize(QtCore.QSize(18, 18))
    self.dict_new_button_like[name_it_web][number].setObjectName(f"Button_Like_{str(number)}")

    self.dict_new_button_like[name_it_web][number].clicked.connect(lambda: like_but_conf(self, name_it_web,
                                                                                         number))

