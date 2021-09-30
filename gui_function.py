import sys
import take_pars_data
import time
from create_new_buttons import table_new_button
import json

from PyQt6.QtWidgets import QDialog, QWidget, QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt6 import QtCore
from graphic_main import Ui_Dialog

NAME_JSON = "saved_info.json"
NAME_JSON_EXIT = "saved_info_exit.json"


# Максимальный прогресс 99%, больше\равно уже создание таблицы и разблокировка кнопок
class ProgressHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)
    Pars_item = dict()

    def run(self):
        self.mysignal.emit(["progress_increment", 1])
        ptp = take_pars_data.take_ptp_center()
        self.mysignal.emit(["progress_increment", 50])
        t24 = take_pars_data.take_trade24()
        self.mysignal.emit(["progress_increment", 99])
        self.Pars_item["ru-trade24.ru"] = t24["ru-trade24.ru"]
        self.Pars_item["ptp-center.ru"] = ptp["ptp-center.ru"]
        self.mysignal.emit(["done", 99])
        time.sleep(1)
        self.mysignal.emit(["done", 100])




class ImageDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.appWin = QApplication(sys.argv)
        self.uiMwin = Ui_Dialog()
        self.uiMwin.setupUi(self)

        # Блокировка кнопок для выполнения функций (так же является триггером для аварийного выхода кнопкой Exit)
        self.BLOCK_BUTTON = False

        # Создаем экземпляр класса с потоком и парсинг сайтов
        self.uiMwin.progressBar.setValue(0)
        self.uiMwin.progressBar.hide()

        self.handlerAndParsData = ProgressHandler()
        self.handlerAndParsData.mysignal.connect(self.progress_bar_and_Pars)

        # Подвязываем кнопки к функциям
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

    def progress_bar_and_Pars(self, value):
        self.BLOCK_BUTTON = True
        self.uiMwin.progressBar.show()
        self.uiMwin.progressBar.setValue(value[1])
        if value[1] == 99:
            self.Pars_item = self.handlerAndParsData.Pars_item
            self.do_table_cards()
        if value[0] == "done" and value[1] == 100:
            self.BLOCK_BUTTON = False


    def filter_pars(self, word="Москва"):
        if self.BLOCK_BUTTON:
            return

        if not self.Pars_item:
            self.handlerAndParsData.start()

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
        if self.BLOCK_BUTTON:
            print("Emergency Exit without saving!")
            raise SystemExit(1)
        j = json.dumps(self.Pars_item)
        with open(NAME_JSON_EXIT, 'w') as f:
            f.write(j)
        print("Exit save data: done!")
        raise SystemExit(1)

    def bt_save_check(self):
        if self.BLOCK_BUTTON:
            return
        j = json.dumps(self.Pars_item)
        with open(NAME_JSON, 'w') as f:
            f.write(j)
        print("Save done!")

    def bt_search(self):
        if self.BLOCK_BUTTON:
            return
        word = self.uiMwin.lineEdit_Search.text()
        if word == "Enter words" or word == "Please enter your question":
            self.uiMwin.lineEdit_Search.setText("Please enter your question")
        else:
            self.filter_pars(word)

    def bt_load_save(self):
        if self.BLOCK_BUTTON:
            return
        file_data = json.load(open(NAME_JSON))
        self.Pars_item = file_data
        print("load information Success!")
        self.do_table_cards()

    def bt_reset(self):
        if self.BLOCK_BUTTON:
            return
        self.handlerAndParsData.start()

    # TABLE CREATING
    # Post here your functions for control at the table information
    # ///////////////////////////////////////////////////////////////////
    def take_pars_file(self):
        if self.BLOCK_BUTTON:
            return
        ptp = take_pars_data.take_ptp_center()
        t24 = take_pars_data.take_trade24()
        self.Pars_item["ru-trade24.ru"] = t24["ru-trade24.ru"]
        self.Pars_item["ptp-center.ru"] = ptp["ptp-center.ru"]

    def table_button_click(self, number_row_item):
        if self.BLOCK_BUTTON:
            return
        self.uiMwin.stackedWidget.setCurrentWidget(self.uiMwin.page_1_All)
        #TODO

    def do_table_cards(self, use_filter=False):

        self.listNewButtonTable.clear()
        self.feedbackLogButton.clear()

        pars_it_func = dict()

        if use_filter:
            pars_it_func = self.pars_it_filter
        else:
            pars_it_func = self.Pars_item

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
