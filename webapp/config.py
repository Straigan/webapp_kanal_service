import os

from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
SCOPES = [os.environ['SCOPES']]
SERVICE_ACCOUNT_FILE = os.path.join(basedir, 'credentials.json')
SAMPLE_SPREADSHEET_ID = os.environ['SAMPLE_SPREADSHEET_ID']
SAMPLE_RANGE_NAME = os.environ['SAMPLE_RANGE_NAME']
