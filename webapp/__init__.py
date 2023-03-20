from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.kanal_service.views import blueprint as kanal_service


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(kanal_service)
    db.init_app(app)
    Migrate(app, db)
    return app