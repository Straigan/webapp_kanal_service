import requests

from webapp.config import TOKEN_TELEGRAM, CHAT_ID_TELEGRAM


def messege_old_date_order_in_db(number_order, date_order):
    'Шаблон сообщение'
    message = f'Заказ нормер {number_order}, срок доставки {date_order} - прошел.'
    post_massage_telegram_bot(message)


def post_massage_telegram_bot(message: str) -> None:
    'Отпарвка сообщения в телеграмм чат'
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage?chat_id={CHAT_ID_TELEGRAM}&text={message}"
    print(requests.get(url).json())