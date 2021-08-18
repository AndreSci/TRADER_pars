import sys
import take_pars_data
from create_new_buttons import table_new_button

from PyQt6.QtWidgets import QDialog, QWidget, QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from graphic_main import Ui_Dialog

class ImageDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.appWin = QApplication(sys.argv)
        self.uiMwin = Ui_Dialog()
        self.uiMwin.setupUi(self)

        self.uiMwin.Button_Exit.clicked.connect(self.bt_exit)
        self.uiMwin.Button_All.clicked.connect(self.bt_all)
        self.uiMwin.Button_Search.clicked.connect(self.bt_search)
        self.uiMwin.Button_Reset.clicked.connect(self.bt_reset)
        self.uiMwin.Button_New.clicked.connect(self.bt_new)

        # Зона новых кнопок в таблице table_for_cards--------------------------------
        self.listNewButtonTable = list()    # База новых кнопок из таблицы
        self.feedbackLogButton = dict()  # запись адресов новых кнопок
        # ---------------------------------------------------------------------------
        # Зона данных парсинга ------------------------------------------------------
        self.Pars_item = dict()
        # ---------------------------------------------------------------------------

    def bt_exit(self):
        print("system save all data (NEED #TODO)")
        raise SystemExit(1)

    def bt_all(self):
        print("(NEED #TODO)")

    def bt_search(self):
        print("(NEED #TODO)")

    def bt_new(self):
        print("(NEED #TODO)")

    def bt_reset(self):
        self.do_table_cards()

    def take_pars_file(self):
        self.Pars_item = take_pars_data.take_trade24()

    def table_button_click(self, number_row_item):
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.page_1_All)

    def do_table_cards(self):
        self.listNewButtonTable.clear()
        self.feedbackLogButton.clear()

        if not self.Pars_item:
            self.take_pars_file()

        print(self.Pars_item)
        "' Очищаем заглавия '"

        self.uiMwin.table_for_cards.clear()
        self.uiMwin.table_for_cards.setRowCount(0)

        labels = ['Address', '№', 'Name', 'Comments']

        self.uiMwin.table_for_cards.setColumnCount(len(labels))  # устанавливаем длину таблицы
        self.uiMwin.table_for_cards.setHorizontalHeaderLabels(labels)  # заполняем название столбцов
        # ------------------------------------------------------------------------------------------
        # return list() "result_item_cards"
        # { car_num_dig / name / target / {result_lot(dict)}...}
        # {     0          1        2       3   ...     }

        index_row = 0
        number_row_item = 1
        its_group_name = False

        for key in self.Pars_item:

            for cards in self.Pars_item[key]:

                for card in cards:
                    row = self.uiMwin.table_for_cards.rowCount()  # получаем кол-во строк
                    self.uiMwin.table_for_cards.setRowCount(row + 1)  # создаем новою строку

                    self.uiMwin.table_for_cards.setItem(index_row, 0, QTableWidgetItem(key))
                    self.uiMwin.table_for_cards.setItem(index_row, 1, QTableWidgetItem(card[0]))
                    self.uiMwin.table_for_cards.setItem(index_row, 2, QTableWidgetItem(card[1]))
                    self.uiMwin.table_for_cards.setItem(index_row, 3, QTableWidgetItem(card[2]))

                    index_row += 1




