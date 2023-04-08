import os

from dotenv import load_dotenv
from celery.schedules import crontab

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

TIMEZONE='Europe/Yekaterinburg'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
SCOPES = [os.environ['SCOPES']]
SERVICE_ACCOUNT_FILE = os.path.join(basedir, 'credentials.json')
SAMPLE_SPREADSHEET_ID = os.environ['SAMPLE_SPREADSHEET_ID']
SAMPLE_RANGE_NAME = os.environ['SAMPLE_RANGE_NAME']
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']

