from celery import shared_task

from webapp.db import db
from webapp.kanal_service.models import Order
from webapp.services.google_sheet import delete_order_in_db, add_order_in_db, change_order_data_in_db, check_orders_date_delivery


@shared_task(name='comparison_data_google_sheets_and_add_or_delete_data_in_db')
def comparison_data_google_sheets_and_add_or_delete_data_in_db():
    """
        Сравние данных из гугл таблици и базы данных,
        с послидующим удалением, добавлением или изменением данных в базе данных
    """

    # delete_order_in_db()
    # add_order_in_db()
    # change_order_data_in_db()
    check_orders_date_delivery()
