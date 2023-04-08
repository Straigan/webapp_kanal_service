from flask import Blueprint, render_template

from webapp.kanal_service.models import Order


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/')
def index():
    page_title = "Каналcервис"
    orders = Order.query.all()
    return render_template('kanal_service/index.html', page_title=page_title, orders=orders)