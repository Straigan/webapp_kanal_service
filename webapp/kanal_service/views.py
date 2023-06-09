from flask import Blueprint, render_template

from webapp.kanal_service.models import Order


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/')
def index():
    page_title = "Каналcервис"
    orders = Order.query.all()
    labels = [order.date_of_delivery for order in orders]
    data = [order.price_in_dollar for order in orders]
    total_sum_dollar = sum(data)
    return render_template('kanal_service/index.html', 
                    page_title=page_title, 
                    orders=orders, 
                    labels=labels, 
                    data=data, 
                    total_sum_dollar=total_sum_dollar
                )

