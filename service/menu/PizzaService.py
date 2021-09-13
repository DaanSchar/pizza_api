
from flask import jsonify

from extensions import db
from models.model import Pizza
from schemas.schema import PizzaSchema

pizzaSchema = PizzaSchema()
pizzaSchemas = PizzaSchema(many=True)


def get_pizzas():
    pizzas = pizzaSchemas.dump(Pizza.query.all())

    if not pizzas:
        return jsonify({'message': 'no pizzas found'}), 400

    for pizza in pizzas:
        add_total_price_to_pizza(pizza)

    return jsonify(pizzas), 200



def get_pizza(pizza_id):
    pizza = pizzaSchema.dump(Pizza.query.filter_by(pizza_id=pizza_id).first())

    if not pizza:
        return jsonify({"message": "Could not find pizza with id " + str(pizza_id)}), 400

    add_total_price_to_pizza(pizza)
    return jsonify(pizza), 200


def add_total_price_to_pizza(pizza):
    vat = 1.09
    profit = 1.4
    total = 0

    for topping in pizza.get('toppings'):
        total += topping.get('price')

    pizza['total_price'] = (total + pizza.get('price')) * profit * vat
