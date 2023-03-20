from flask import Blueprint, render_template
from webapp.services.google_sheet import insert_data_in_db


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/')
def index():
    page_title = "Каналcервис"
    insert_data_in_db()
    return render_template('kanal_service/index.html', page_title=page_title)