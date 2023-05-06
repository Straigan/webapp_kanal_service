import requests
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account

from webapp.config import SERVICE_ACCOUNT_FILE, SCOPES, SAMPLE_RANGE_NAME, SAMPLE_SPREADSHEET_ID
from webapp.db import db
from webapp.kanal_service.models import Order


def get_google_sheets_data():
    """Загрузка данных из гугл табилици"""

    credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                    range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    for row in values:
        yield row


def get_kurs_dollara():
    """Функция получает данные по дорллару из ЦБ РФ по API"""
    return requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


def delete_order_in_db():
    'Если номера заказа из БД нет в списке номеров заказов из гугл таблице, то заказ удаляется из БД'
    query_orders = Order.query.all()
    numbers_orders_data_db = tuple((order.number_order for order in query_orders))
    numbers_orders_data_google_sheets = tuple((int(order[1]) for order in get_google_sheets_data()))

    for number_order_db in numbers_orders_data_db:
        if number_order_db not in numbers_orders_data_google_sheets:
            delete_order_in_db = Order.query.filter_by(number_order=number_order_db).one()
            db.session.delete(delete_order_in_db)
    db.session.commit()


def add_order_in_db():
    'Если номера заказа из гугл таблицы нет в БД, то строка номера заказа добавляется в БД'

    query_orders = Order.query.all()
    numbers_orders_data_db = tuple((order.number_order for order in query_orders))
    data_google_sheets = tuple((data_sheet for data_sheet in get_google_sheets_data()))

    for order_google_sheets in data_google_sheets:
        order_google_sheets_str_to_int = int(order_google_sheets[1])
        if order_google_sheets_str_to_int not in numbers_orders_data_db:
            kurs_dollar_cb_rf = get_kurs_dollara()
            price_in_ruble = order_google_sheets_str_to_int * kurs_dollar_cb_rf['Valute']['USD']['Value']
            add_order = Order(
                number_str = order_google_sheets[0],
                number_order = order_google_sheets_str_to_int,
                price_in_dollar = order_google_sheets[2],
                price_in_ruble = round(price_in_ruble, 2),
                date_of_delivery = order_google_sheets[3],
                hash_line = hash((order_google_sheets[2], order_google_sheets[3]))
            )
            db.session.add(add_order)
    db.session.commit()


def change_order_data_in_db():
    """
    Происходит сравнение содержимого строки из гугл таблици со стракой из БД, через сравнение хешей.
    Если хеш заказа из гугул таблици не совпадает с хешом заказа из ДБ, то проиходит обновление данных
    в таблице с созданием нового хеша.
    """
    query_orders = Order.query.all()
    numbers_orders_data_db = tuple((order.hash_line for order in query_orders))
    data_google_sheets = tuple((data_sheet for data_sheet in get_google_sheets_data()))
    
    for order_google_sheets in data_google_sheets:
        order_google_sheets_str_to_int = int(order_google_sheets[1])
        hash_order_in_google_table = hash((order_google_sheets[2], order_google_sheets[3]))
        if hash_order_in_google_table not in numbers_orders_data_db:
            kurs_dollar_cb_rf = get_kurs_dollara()
            price_in_ruble = order_google_sheets_str_to_int * kurs_dollar_cb_rf['Valute']['USD']['Value']
            number_order = order_google_sheets_str_to_int
            change_order = Order.query.filter(number_order==number_order).first()
            change_order.number_str = order_google_sheets[0],
            change_order.price_in_dollar = order_google_sheets[2],
            change_order.price_in_ruble = round(price_in_ruble, 2),
            change_order.date_of_delivery = order_google_sheets[3],
            change_order.hash_line = hash((order_google_sheets[2], order_google_sheets[3]))
        
    db.session.commit()
