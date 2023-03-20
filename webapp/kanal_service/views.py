from flask import Blueprint, render_template


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/')
def index():
    page_title = "Каналcервис"
    return render_template('kanal_service/index.html', page_title=page_title)