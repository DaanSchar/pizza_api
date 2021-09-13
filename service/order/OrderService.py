import datetime
from functools import wraps

from flask import jsonify, request
from sqlalchemy import desc

from extensions import db
from models.model import Pizza, Drink, Dessert, Customer
from models.model import Order
from schemas.schema import OrderSchema, CustomerSchema

order_schema = OrderSchema()
order_schemas = OrderSchema(many=True)
customer_schema = CustomerSchema()


def post_order():
    json = request.json

    if not json.get('pizza'):
        return jsonify({'message': 'You must order at least 1 Pizza'})

    try:
        if not customer_exist(json.get('customer')):
            create_customer(json.get('customer'))
        customer = get_customer(json.get('customer'))
    except:
        return jsonify({'message': 'something went wrong while determining customer'})

    try:
        order = Order(
            customer_id=customer.customer_id,
            date_of_order=datetime.datetime.now(),
            estimated_delivery_time=datetime.datetime.now() + datetime.timedelta(minutes=15),
            status='in process',
        )
        add_order_to_db(order, json)
        db.session.commit()
    except:
        return jsonify({'message': 'something went wrong while processing order'})

    return jsonify(order_schema.dump(order)), 200


def get_orders(customer_id):
    if not Customer.query.filter_by(customer_id=customer_id).first():
        return jsonify({'message': 'could not find customer'}), 404

    try:
        orders = order_schemas.dump(get_all_orders(customer_id))
    except:
        jsonify({'message': 'could not find orders'}), 404

    return jsonify(orders), 200


def get_current_order(customer_id):
    if not Customer.query.filter_by(customer_id=customer_id).first():
        return jsonify({'message': 'could not find customer'}), 404

    try:
        newest_order = order_schemas.dump(get_all_orders(customer_id))[0]
    except:
        return jsonify({'message': 'no open orders found'}), 404

    if not newest_order.get('status') == 'delivered':
        return jsonify(order_schema.dump(newest_order)), 200
    return jsonify({'message': 'no open orders found'}), 404


def cancel_current_order(customer_id):
    if not Customer.query.filter_by(customer_id=customer_id).first():
        return jsonify({'message': 'could not find customer'}), 404

    try:
        newest_order = get_all_orders(customer_id)[0]
        newest_order.status = 'canceled'
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'message': 'no open orders found'}), 404

    if newest_order.date_of_order + datetime.timedelta(minutes=5) < datetime.datetime.now():
        return jsonify({'message': 'you can only cancel orders within the first 5 minutes'}), 400

    return jsonify({'message': 'successfully canceled order'}), 200


def get_all_orders(customer_id):
    return Order.query.filter_by(customer_id=customer_id).order_by(desc(Order.date_of_order)).all()


def add_order_to_db(order, json):
    pizzas = Pizza.query.filter(Pizza.pizza_id.in_(json.get('pizza'))).all()
    drinks = Drink.query.filter(Drink.drink_id.in_(json.get('drink'))).all()
    desserts = Dessert.query.filter(Dessert.dessert_id.in_(json.get('dessert'))).all()

    for pizza in pizzas:
        order.pizzas.append(pizza)
    for drink in drinks:
        order.drinks.append(drink)
    for dessert in desserts:
        order.desserts.append(dessert)

    db.session.add(order)


def get_customer(customer):
    return Customer.query.filter_by(
        first_name=customer.get('first_name'),
        last_name=customer.get('last_name'),
        address=customer.get('address'),
        phone=customer.get('phone')
    ).first()


def customer_exist(customer):
    if get_customer(customer):
        return True
    return False


def create_customer(customer):
    new_customer = Customer(
        first_name=customer.get('first_name'),
        last_name=customer.get('last_name'),
        address=customer.get('address'),
        phone=customer.get('phone')
    )
    db.session.add(new_customer)

