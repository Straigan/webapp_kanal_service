from webapp.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_order = db.Column(db.Integer, unique=True)
    price_in_dollar = db.Column(db.Integer)
    price_in_ruble = db.Column(db.Float)
    date_of_delivery = db.Column(db.String(10))

    def __repr__(self):
        return f'<Order {self.number_order}, id {self.id}, date_of_delivery {self.date_of_delivery}>'