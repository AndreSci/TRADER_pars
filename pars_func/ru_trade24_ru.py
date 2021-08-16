import logging

import requests
from bs4 import BeautifulSoup
import time

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ParsLots')

''' УСТАНОВЛИНА МАКСИМАЛЬНОЕ КОЛИЧЕСТВО СТРАНИЦ 50!!!'''

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

    for item_card in cards:
        card_find = item_card.find('div', class_='col col--xs-9')

        card_name = item_card.find('div', class_='trade-card__name').get_text()
        card_target = item_card.find('div', class_='trade-card__type').get_text()

        lots = card_find.find_all('div', class_='row row--v-offset')

        # Предполагается что строка будет содержать только одно digit значение
        card_number_dig = ''.join(filter(lambda x: x.isdigit(), card_target))

        print(card_name)
        print(card_number_dig)
        print(card_target)

        index_lot = 1

        for lot in lots:
            try:    # Вынужденная мера из-за наличия одинаковых имён
                lots_text = lot.find('div', class_='collapse').get_text()
                lots_price = lot.find('div', class_='trade-card__price').get_text()
            except:     # Пропускаем этот цикл
                continue

            print('-----------------------')
            print(f'Лот № {index_lot}')
            index_lot += 1
            print(lots_text)
            print(f'Цена за лот: {lots_price}')

        print('################################################################')


full_info = dict()
nextPage = []
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

    nextPage.append(html_item)

    cardPage = load_page(html_item.text)

    if len(cardPage) == 0:
        break

    trade_card_pages.append(cardPage)

    print(f'done {index} - len = {len(trade_card_pages[index - 1])}')
    index += 1
    time.sleep(1)

    break   # Убрать в релизе

get_info(trade_card_pages[0])

