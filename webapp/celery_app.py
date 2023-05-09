from celery import Celery, Task
from celery.schedules import crontab
from flask import Flask

from webapp import config
from webapp.kanal_service.tasks import comparison_data_google_sheets_and_add_or_delete_data_in_db, task_check_orders_date_delivery


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(config)
    celery_app.conf.beat_schedule = {
    'comparison_data_google_sheets_and_add_or_delete_data_in_db': {
        'task': 'comparison_data_google_sheets_and_add_or_delete_data_in_db',
        'schedule': 300.0,
        },
    'task_check_orders_date_delivery': {
         'task': 'task_check_orders_date_delivery',
        'schedule': crontab(minute=10, hour=0), 
        },
    }

    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app