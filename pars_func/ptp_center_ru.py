import logging

import requests
import fake_useragent
from bs4 import BeautifulSoup
import time

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ParsLots')

''' УСТАНОВЛИНА МАКСИМАЛЬНОЕ КОЛИЧЕСТВО СТРАНИЦ 50!!!'''


class NameSpace:
    def __init__(self):
        self.NAME = "ptp-center.ru"
        self.URL_01 = 'https://ptp-center.ru/etp/trade/list.html'
        self.URL_02 = '?page='
        self.HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.MAX_PAGE = 10
        self.CARDS_NAME = "data"


""" Пояснение к получаемым данным из данной функции """
# Заполняем лист(result_item) по схеме "Номер /	Имя продавца / тип продажи / Лот №"
# return list() "result_item_cards"
# { car_num_dig / name / target / {result_lot(dict)}...}
# {     0          1        2       3   ...     }

# {result_lot(dict)...}   have structure
# { index / text / price }
# {   0      1      2    }


def get_html(class_name, url, params=None):     # Получаем html данные с сайта
    req = requests.get(url, params=params, headers=class_name.HEADER)
    return req


def pars(url, class_name):  # Соединяемся и проверяем ответ
    html = get_html(class_name, url)
    if html.status_code >= 200 and html.status_code < 400:
        return html.text
    else:
        print('error!')
        return False


def load_page(html: str, class_name):   # Получаем нужные участки html
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all(class_=class_name.CARDS_NAME)

    return cards


def get_info(cards):    # Получаем данные всех предложений и лотов с страницы

    result_item_cards = list()
    # отсеиваем все карточки из полученных данных
    cards_find = cards[0].find_all('tr', style="cursor: pointer")

    for card_find in cards_find:

        result_item = dict()
        card_number_dig = 0  # ''.join(filter(lambda x: x.isdigit(), card_target))

        # Заполняем лист(result_item) по схеме "Номер /	Имя продавца / тип продажи/состояние / Лот №"

        res = card_find.find_all('td', colspan="1")  # получаем разделы карты

        result_item["number"] = res[0].get_text()
        result_item["name"] = res[1].get_text()
        result_item["target"] = res[3].get_text()

        # { "number" / "name" / "target" / "lots" = list() -> (dict)...}
        # {     0          1        3       2   ...     }

        index_lot = 1
        result_lot = dict()

        result_lot[index_lot] = dict()
        result_lot[index_lot]["text"] = res[2].get_text()
        result_lot[index_lot]["price"] = 'none'

        result_item["lots"] = result_lot

        result_item_cards.append(result_item)
    return result_item_cards


def start_pars():

    class_name = NameSpace()

    full_info = dict()
    full_info[class_name.NAME] = list()

    next_page = []
    trade_card_pages = []
    page_full = True
    index = 1

    while(page_full):
        url_f = f'{class_name.URL_01}{class_name.URL_02}{index}'

        try:
            html_item = pars(url_f, class_name)
        except:
            print(f"Requests ending on index: {index}")
            break

        if html_item == False and class_name.MAX_PAGE > index:
            index += 1
            continue
        elif class_name.MAX_PAGE <= index:
            print('End work, out of range!')
            page_full = False
            break

        next_page.append(html_item)

        card_page = load_page(html_item, class_name)

        if len(card_page) == 0:
            break

        trade_card_pages.append(card_page)

        index += 1
        time.sleep(0.1)

        break   # Убрать в релизе

    for it in trade_card_pages:
        full_info[class_name.NAME].append(get_info(it))

    print("create data ptp_center_ru: Success!!!")

    return full_info


#print(start_pars())