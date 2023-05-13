import os

from dotenv import load_dotenv
from celery.schedules import crontab

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

# WebApp Config
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Google Sheets Config
SCOPES = [os.environ['SCOPES']]
SERVICE_ACCOUNT_FILE = os.path.join(basedir, 'credentials.json')
SAMPLE_SPREADSHEET_ID = os.environ['SAMPLE_SPREADSHEET_ID']
SAMPLE_RANGE_NAME = os.environ['SAMPLE_RANGE_NAME']

# Celery Config
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']

# Telegram Congig
TOKEN_TELEGRAM = os.environ['TOKEN_TELEGRAM']
CHAT_ID_TELEGRAM = os.environ['CHAT_ID_TELEGRAM']
