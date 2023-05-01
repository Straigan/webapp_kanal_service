from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.kanal_service.views import blueprint as kanal_service
from webapp.celery_app import celery_init_app


def create_webapp():
    webapp = Flask(__name__)
    webapp.config.from_pyfile('config.py')
    webapp.register_blueprint(kanal_service)
    db.init_app(webapp)
    from webapp.kanal_service import models
    with webapp.app_context():
        db.create_all()
    Migrate(webapp, db)
    celery_init_app(webapp)
    return webapp



flask_app = create_webapp()
celery_app = flask_app.extensions["celery"]