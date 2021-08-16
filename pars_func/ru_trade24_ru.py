import logging

import requests
from bs4 import BeautifulSoup
import time

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ParsLots')

''' УСТАНОВЛИНА МАКСИМАЛЬНОЕ КОЛИЧЕСТВО СТРАНИЦ 50!!!'''

NAME = "ru-trade24.ru"
URL_01 = 'https://www.ru-trade24.ru/Home/Trades?page='
URL_02 = '&sort=Id&ascending=False&status=1'
HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
MAX_PAGE = 50
CARDS_NAME = "row row--v-offset trade-card"


def get_html(url, params=None):     # Получаем html данные с сайта
    req = requests.get(url, params=params, headers=HEADER)
    return req


def pars(url):  # Соединяемся и проверяем ответ
    html = get_html(url)
    if html.status_code >= 200 and html.status_code < 400:
        return html
    else:
        print('error!')
        return False


def load_page(html: str):   # Получаем нужные участки html
    soup = BeautifulSoup(html, 'html.parser')
    trade_cards = soup.find_all(class_=CARDS_NAME)

    return trade_cards


def get_info(cards):    # Получаем данные всех предложений и лотов с страницы

    result_item_cards = list()

    for item_card in cards:

        result_item = list()

        card_find = item_card.find('div', class_='col col--xs-9')

        card_name = item_card.find('div', class_='trade-card__name').get_text()
        card_target = item_card.find('div', class_='trade-card__type').get_text()

        lots = card_find.find_all('div', class_='row row--v-offset')

        # Предполагается что строка будет содержать только одно digit значение
        card_number_dig = ''.join(filter(lambda x: x.isdigit(), card_target))

        # Заполняем лист(result_item) по схеме "Номер /	Имя продавца / тип продажи / Лот №"
        result_item.append(card_number_dig)
        result_item.append(card_name)
        result_item.append(card_target)

        index_lot = 1
        result_lot = dict()

        for lot in lots:
            try:    # Вынужденная мера из-за наличия одинаковых имён
                lots_text = lot.find('div', class_='collapse').get_text()
                lots_price = lot.find('div', class_='trade-card__price').get_text()
                # \xa0 is actually non-breaking space in Latin1 (ISO 8859-1),
                # also chr(160). You should replace it with a space.
                # Read up on http://docs.python.org/howto/unicode.html
                lots_price = lots_price.replace(u'\xa0', u' ')
            except:     # Пропускаем этот цикл
                continue

            result_lot[index_lot] = list()
            result_lot[index_lot].append(index_lot)
            result_lot[index_lot].append(lots_text)
            result_lot[index_lot].append(lots_price)

            index_lot += 1

        result_item.append(result_lot)
        #print(result_item)
        #print('################################################################')

        result_item_cards.append(result_item)
    #print(result_item_cards[3][2])
    return result_item_cards


def start_pars():

    full_info = dict()
    full_info[NAME] = list()

    next_page = []
    trade_card_pages = []
    page_full = True
    index = 1

    while(page_full):
        url_f = f'{URL_01}{index}{URL_02}'
        html_item = pars(url_f)

        if html_item == False and MAX_PAGE > index:
            index += 1
            continue
        elif MAX_PAGE <= index:
            print('End work, out of range!')
            page_full = False
            break

        next_page.append(html_item)

        card_page = load_page(html_item.text)

        if len(card_page) == 0:
            break

        trade_card_pages.append(card_page)

        #print(f'done {index} - len = {len(trade_card_pages[index - 1])}')
        index += 1
        time.sleep(1)

        break   # Убрать в релизе

    for it in trade_card_pages:
        full_info[NAME].append(get_info(it))

    return full_info


print(start_pars())