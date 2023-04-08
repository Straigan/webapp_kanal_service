from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.kanal_service.views import blueprint as kanal_service
from webapp.celery_app import celery_init_app


def create_webapp():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(kanal_service)
    db.init_app(app)
    Migrate(app, db)
    celery_init_app(app)
    return app



flask_app = create_webapp()
celery_app = flask_app.extensions["celery"]