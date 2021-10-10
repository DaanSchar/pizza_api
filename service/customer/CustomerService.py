from flask import jsonify, request
from extensions import db

from models.model import Customer, Order, Discount
from schemas.schema import OrderSchema, CustomerSchema

order_schema = OrderSchema()
order_schemas = OrderSchema(many=True)
customer_schema = CustomerSchema()
customer_schemas = CustomerSchema(many=True)


def get_customer_info(customer_id):
    customer = customer_schema.dump(get_customer(customer_id))
    if not customer:
        return jsonify({'message': 'could not find customer with id ' + str(customer_id)})

    customer['total_orders'] = {
        'orders': len(get_delivered_orders(customer_id)),
        'pizza': get_total_pizza_orders(customer_id),
        'drink': get_total_drink_orders(customer_id),
        'dessert': get_total_dessert_orders(customer_id)
    }

    return customer


def get_customer(customer_id):
    return Customer.query.filter_by(customer_id=customer_id).first()


def use_discount():
    json = request.json
    discount = Discount.query.filter_by(code=json['code']).first()
    if not discount:
        return {'allowed': False}

    if not discount.is_used:
        discount.is_used = True
        db.session.commit()
        return {'allowed': True}

    return {'allowed': False}


def get_delivered_orders(customer_id):
    result = Order.query.filter_by(customer_id=customer_id, status='delivered')
    return order_schemas.dump(result)


def get_total_pizza_orders(customer_id):
    query = "SELECT COUNT(pizza_id) FROM pizza_order WHERE order_id IN (SELECT order_id FROM 'order' WHERE customer_id=" +str(customer_id)+" AND status='delivered')"
    return db.session.execute(query).first()[0]


def get_total_drink_orders(customer_id):
    query = "SELECT COUNT(drink_id) FROM drink_order WHERE order_id IN (SELECT order_id FROM 'order' WHERE customer_id=" + str(customer_id) + " AND status='delivered')"
    return db.session.execute(query).first()[0]


def get_total_dessert_orders(customer_id):
    query = "SELECT COUNT(drink_id) FROM drink_order WHERE order_id IN (SELECT order_id FROM 'order' WHERE customer_id=" + str(customer_id) + " AND status='delivered')"
    return db.session.execute(query).first()[0]
