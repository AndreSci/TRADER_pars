import sys
import take_pars_data
from create_new_buttons import table_new_button
import json

from PyQt6.QtWidgets import QDialog, QWidget, QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from graphic_main import Ui_Dialog

NAME_JSON = "saved_info.json"
NAME_JSON_EXIT = "saved_info_exit.json"
NAME_CVS = "saved_info.cvs"
NAME_CVS_LAST_EXIT = "saved_info_exit.cvs"


class ImageDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.appWin = QApplication(sys.argv)
        self.uiMwin = Ui_Dialog()
        self.uiMwin.setupUi(self)

        self.uiMwin.Button_Exit.clicked.connect(self.bt_exit)
        self.uiMwin.Button_Save_Check.clicked.connect(self.bt_save_check)
        self.uiMwin.Button_Search.clicked.connect(self.bt_search)
        self.uiMwin.Button_Reset.clicked.connect(self.bt_reset)
        self.uiMwin.Button_Load_Save.clicked.connect(self.bt_load_save)

        # Зона новых кнопок в таблице table_for_cards--------------------------------
        self.listNewButtonTable = list()  # База новых кнопок из таблицы
        self.feedbackLogButton = dict()  # запись адресов новых кнопок
        # ---------------------------------------------------------------------------
        # Зона данных парсинга ------------------------------------------------------
        self.Pars_item = dict()
        self.pars_it_filter = dict()
        self.Filter_words = ""
        # ---------------------------------------------------------------------------

    def filter_pars(self, word="Москва"):

        if not self.Pars_item:
            self.take_pars_file()

        for key in self.Pars_item:
            self.pars_it_filter[key] = list()
            for cards in self.Pars_item[key]:
                pars_cards = list()

                for card in cards:
                    its_ok = False
                    for key_lots in card["lots"]:
                        if card["lots"][key_lots]["text"].find(word) != -1:
                            its_ok = True

                    if its_ok:
                        pars_cards.append(card)

                self.pars_it_filter[key].append(pars_cards)

        self.do_table_cards(True)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////////
    def bt_exit(self):
        j = json.dumps(self.Pars_item)
        with open(NAME_JSON_EXIT, 'w') as f:
            f.write(j)
            f.close()
        print("Exit save data: done!")
        raise SystemExit(1)

    def bt_save_check(self):
        j = json.dumps(self.Pars_item)
        with open(NAME_JSON, 'w') as f:
            f.write(j)
            f.close()
        print("Save done!")

    def bt_search(self):
        word = self.uiMwin.lineEdit_Search.text()
        if word == "Enter words" or word == "Please enter your question":
            self.uiMwin.lineEdit_Search.setText("Please enter your question")
        else:
            self.filter_pars(word)

    def bt_load_save(self):
        file_data = json.load(open("saved_info.json"))
        self.Pars_item = file_data
        print("load information Success!")
        self.do_table_cards()

    def bt_reset(self):
        self.do_table_cards(use_reset=True)

    # TABLE CREATING
    # Post here your functions for control at the table information
    # ///////////////////////////////////////////////////////////////////
    def take_pars_file(self):
        ptp = take_pars_data.take_ptp_center()
        t24 = take_pars_data.take_trade24()
        self.Pars_item["ru-trade24.ru"] = t24["ru-trade24.ru"]
        self.Pars_item["ptp-center.ru"] = ptp["ptp-center.ru"]

    def table_button_click(self, number_row_item):
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.page_1_All)

    def do_table_cards(self, use_filter=False, use_reset=False):
        self.listNewButtonTable.clear()
        self.feedbackLogButton.clear()

        pars_it_func = dict()

        if not self.Pars_item or use_reset == True:
            self.take_pars_file()
            pars_it_func = self.Pars_item
        else:
            pars_it_func = self.Pars_item

        if use_filter:
            pars_it_func = self.pars_it_filter

        "' Очищаем заглавия '"

        self.uiMwin.table_for_cards.clear()
        self.uiMwin.table_for_cards.setRowCount(0)

        labels = ['Address', '№', 'Name', 'Lots', 'Comments']

        self.uiMwin.table_for_cards.setColumnCount(len(labels))  # устанавливаем длину таблицы
        self.uiMwin.table_for_cards.setHorizontalHeaderLabels(labels)  # заполняем название столбцов
        # ------------------------------------------------------------------------------------------
        # return list() "result_item_cards"
        # { "number" / "name" / "target" / "lots" = list() -> (dict)...}
        # {     0          1        2       3   ...     }

        index_row = 0
        number_row_item = 1
        its_group_name = False

        for key in pars_it_func:

            for cards in pars_it_func[key]:

                for card in cards:
                    row = self.uiMwin.table_for_cards.rowCount()  # получаем кол-во строк
                    self.uiMwin.table_for_cards.setRowCount(row + 1)  # создаем новую строку
                    self.uiMwin.table_for_cards.setItem(index_row, 0, QTableWidgetItem(key))
                    self.uiMwin.table_for_cards.setItem(index_row, 1, QTableWidgetItem(card["number"]))
                    self.uiMwin.table_for_cards.setItem(index_row, 2, QTableWidgetItem(card["name"]))
                    self.uiMwin.table_for_cards.setItem(index_row, 3, QTableWidgetItem(str(len(card["lots"]))))
                    self.uiMwin.table_for_cards.setItem(index_row, 4, QTableWidgetItem(card["target"]))

                    index_row += 1

        row = self.uiMwin.table_for_cards.rowCount()  # получаем кол-во строк
        self.uiMwin.table_for_cards.setRowCount(row + 1)  # создаем последнюю строку в таблице
