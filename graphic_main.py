# Form implementation generated from reading ui file 'graphic_main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1201, 880)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_up = QtWidgets.QFrame(Dialog)
        self.menu_up.setMinimumSize(QtCore.QSize(720, 60))
        self.menu_up.setMaximumSize(QtCore.QSize(16777215, 60))
        self.menu_up.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.menu_up.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_up.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_up.setObjectName("menu_up")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.menu_up)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.menu_up)
        self.frame_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Button_Exit = QtWidgets.QPushButton(self.frame_4)
        self.Button_Exit.setMinimumSize(QtCore.QSize(70, 23))
        self.Button_Exit.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    background-color: rgb(109, 109, 109);\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 136, 136);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Exit.setObjectName("Button_Exit")
        self.horizontalLayout_2.addWidget(self.Button_Exit)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_Search = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_Search.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_Search.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(30,30,30);\n"
"    border-radius: 0px;\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.horizontalLayout_6.addWidget(self.lineEdit_Search)
        self.Button_Search = QtWidgets.QPushButton(self.frame_5)
        self.Button_Search.setMinimumSize(QtCore.QSize(70, 25))
        self.Button_Search.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Button_Search.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    background-color: rgb(109, 109, 109);\n"
"    border-color:rgb(130, 130, 130);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 136, 136);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Search.setObjectName("Button_Search")
        self.horizontalLayout_6.addWidget(self.Button_Search)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4.addWidget(self.frame_8)
        self.progressBar = QtWidgets.QProgressBar(self.frame_6)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 17))
        self.progressBar.setStyleSheet("QProgressBar{    \n"
"    border: 1px solid;\n"
"    background-color: rgb(230, 210, 185);\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"    border-radius: 5px;    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.295455 rgba(0, 21, 93, 250), stop:0.971751 rgba(205, 25, 89, 248));\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.Load_info = QtWidgets.QLabel(self.frame_6)
        self.Load_info.setMaximumSize(QtCore.QSize(16777215, 17))
        self.Load_info.setObjectName("Load_info")
        self.verticalLayout_4.addWidget(self.Load_info)
        self.horizontalLayout_7.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Button_Reset = QtWidgets.QPushButton(self.frame)
        self.Button_Reset.setMinimumSize(QtCore.QSize(0, 25))
        self.Button_Reset.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Button_Reset.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    background-color: rgb(109, 109, 109);\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 136, 136);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/cil-reload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Reset.setIcon(icon)
        self.Button_Reset.setCheckable(False)
        self.Button_Reset.setObjectName("Button_Reset")
        self.horizontalLayout_8.addWidget(self.Button_Reset)
        self.Button_Load_Save = QtWidgets.QPushButton(self.frame)
        self.Button_Load_Save.setMinimumSize(QtCore.QSize(0, 25))
        self.Button_Load_Save.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    background-color: rgb(109, 109, 109);\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 136, 136);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Button_Load_Save.setObjectName("Button_Load_Save")
        self.horizontalLayout_8.addWidget(self.Button_Load_Save)
        self.Button_Save_Check = QtWidgets.QPushButton(self.frame)
        self.Button_Save_Check.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button_Save_Check.setFont(font)
        self.Button_Save_Check.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Button_Save_Check.setAutoFillBackground(False)
        self.Button_Save_Check.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    background-color: rgb(109, 109, 109);\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(136, 136, 136);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/cil-save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Save_Check.setIcon(icon1)
        self.Button_Save_Check.setAutoExclusive(False)
        self.Button_Save_Check.setDefault(False)
        self.Button_Save_Check.setFlat(False)
        self.Button_Save_Check.setObjectName("Button_Save_Check")
        self.horizontalLayout_8.addWidget(self.Button_Save_Check)
        self.horizontalLayout_7.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.menu_up)
        self.menu_down = QtWidgets.QFrame(Dialog)
        self.menu_down.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu_down.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.menu_down.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_down.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_down.setObjectName("menu_down")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_down)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.menu_down)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1_All = QtWidgets.QWidget()
        self.page_1_All.setObjectName("page_1_All")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_1_All)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.table_for_cards = QtWidgets.QTableWidget(self.page_1_All)
        self.table_for_cards.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.table_for_cards.setStyleSheet("QTableWidget{\n"
"    border: 1px solid;\n"
"    border-color: rgb(1,1,1);\n"
"    background-color: rgb(211, 211, 211);\n"
"    border-radius: 3px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.table_for_cards.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.table_for_cards.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_for_cards.setAutoScroll(False)
        self.table_for_cards.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.table_for_cards.setShowGrid(True)
        self.table_for_cards.setGridStyle(QtCore.Qt.PenStyle.DashLine)
        self.table_for_cards.setRowCount(5)
        self.table_for_cards.setColumnCount(7)
        self.table_for_cards.setObjectName("table_for_cards")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_for_cards.setItem(0, 0, item)
        self.table_for_cards.horizontalHeader().setVisible(False)
        self.table_for_cards.horizontalHeader().setCascadingSectionResizes(False)
        self.table_for_cards.horizontalHeader().setDefaultSectionSize(130)
        self.table_for_cards.horizontalHeader().setHighlightSections(False)
        self.table_for_cards.horizontalHeader().setStretchLastSection(True)
        self.table_for_cards.verticalHeader().setVisible(False)
        self.table_for_cards.verticalHeader().setCascadingSectionResizes(False)
        self.table_for_cards.verticalHeader().setHighlightSections(False)
        self.table_for_cards.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.table_for_cards)
        self.menu_right = QtWidgets.QFrame(self.page_1_All)
        self.menu_right.setMinimumSize(QtCore.QSize(175, 0))
        self.menu_right.setMaximumSize(QtCore.QSize(175, 16777215))
        self.menu_right.setStyleSheet("background-color: rgb(12, 12, 12);")
        self.menu_right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_right.setObjectName("menu_right")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.menu_right)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.menu_right)
        self.frame_7.setMinimumSize(QtCore.QSize(160, 40))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Regions_Box = QtWidgets.QComboBox(self.frame_7)
        self.Regions_Box.setMinimumSize(QtCore.QSize(150, 25))
        self.Regions_Box.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.Regions_Box.setFont(font)
        self.Regions_Box.setStyleSheet("color: rgb(150,150, 150);\n"
"background-color: rgb(52, 52, 52);\n"
"selection-background-color: rgb(55, 56, 56);")
        self.Regions_Box.setObjectName("Regions_Box")
        self.Regions_Box.addItem("")
        self.Regions_Box.addItem("")
        self.Regions_Box.addItem("")
        self.verticalLayout_2.addWidget(self.Regions_Box)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.Web_sites = QtWidgets.QFrame(self.menu_right)
        self.Web_sites.setMinimumSize(QtCore.QSize(0, 0))
        self.Web_sites.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Web_sites.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Web_sites.setObjectName("Web_sites")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Web_sites)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5.addWidget(self.Web_sites)
        self.horizontalLayout_5.addWidget(self.menu_right)
        self.stackedWidget.addWidget(self.page_1_All)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Button_Like = QtWidgets.QPushButton(self.page_2)
        self.Button_Like.setGeometry(QtCore.QRect(80, 220, 71, 71))
        self.Button_Like.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image_file/like_off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("image_file/like_on.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.Button_Like.setIcon(icon2)
        self.Button_Like.setIconSize(QtCore.QSize(30, 30))
        self.Button_Like.setCheckable(True)
        self.Button_Like.setChecked(False)
        self.Button_Like.setAutoDefault(True)
        self.Button_Like.setFlat(True)
        self.Button_Like.setObjectName("Button_Like")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.menu_down)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_Exit.setText(_translate("Dialog", "Exit"))
        self.lineEdit_Search.setText(_translate("Dialog", "Enter words"))
        self.Button_Search.setText(_translate("Dialog", "Search"))
        self.Load_info.setText(_translate("Dialog", "Load info:"))
        self.Button_Reset.setText(_translate("Dialog", "Update"))
        self.Button_Load_Save.setText(_translate("Dialog", "Load Save"))
        self.Button_Save_Check.setText(_translate("Dialog", "Save"))
        self.table_for_cards.setSortingEnabled(True)
        __sortingEnabled = self.table_for_cards.isSortingEnabled()
        self.table_for_cards.setSortingEnabled(False)
        self.table_for_cards.setSortingEnabled(__sortingEnabled)
        self.Regions_Box.setItemText(0, _translate("Dialog", "All regions"))
        self.Regions_Box.setItemText(1, _translate("Dialog", "Moscow"))
        self.Regions_Box.setItemText(2, _translate("Dialog", "Moscow region"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
