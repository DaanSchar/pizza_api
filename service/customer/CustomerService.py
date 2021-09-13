from flask import jsonify
from extensions import db

from models.model import Customer, Order
from schemas.schema import OrderSchema, CustomerSchema

order_schema = OrderSchema()
order_schemas = OrderSchema(many=True)
customer_schema = CustomerSchema()
customer_schemas = CustomerSchema(many=True)


def get_customer_info(customer_id):
    customer = customer_schema.dump(Customer.query.filter_by(customer_id=customer_id).first())
    if not customer:
        return jsonify({'message': 'could not find customer with id ' + str(customer_id)})

    customer['total_orders'] = {
        'orders': len(get_delivered_orders(customer_id)),
        'pizza': get_total_pizza_orders(customer_id),
        'drink': get_total_drink_orders(customer_id),
        'dessert': get_total_dessert_orders(customer_id)
    }

    return jsonify(customer), 200


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
