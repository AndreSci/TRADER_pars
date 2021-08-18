from PyQt6 import QtCore, QtGui, QtWidgets


def table_new_button(SetupMainWindow, NumberRowItem, listNewButtonTab, Name):
    listNewButtonTab.append(QtWidgets.QPushButton(str(Name)))
    listNewButtonTab[NumberRowItem - 1].setStyleSheet("QPushButton {\n"
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
    listNewButtonTab[NumberRowItem - 1].clicked.connect(lambda: SetupMainWindow.table_button_click(NumberRowItem))