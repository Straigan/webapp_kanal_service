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


def insert_data_in_db():
    """Запись данных в таблицу"""
    kurs_dollar_cb_rf = get_kurs_dollara()
    for data_sheets_yield in get_google_sheets_data():
        price_in_ruble = int(data_sheets_yield[1]) * kurs_dollar_cb_rf['Valute']['USD']['Value']
        insert_order = Order(
            number_str = data_sheets_yield[0],
            number_order = data_sheets_yield[1],
            price_in_dollar = data_sheets_yield[2],
            price_in_ruble = round(price_in_ruble, 2),
            date_of_delivery = data_sheets_yield[3],
        )
        db.session.add(insert_order)
    db.session.commit()
