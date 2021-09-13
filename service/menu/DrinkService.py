from flask import jsonify

from models.model import Drink
from schemas.schema import DrinkSchema

drinkSchema = DrinkSchema()
drinkSchemas = DrinkSchema(many=True)


def get_drinks():
    result = Drink.query.all()

    if not result:
        return jsonify({'message': 'no drinks found'}), 400

    return jsonify(drinkSchemas.dump(result)), 200


def get_drink(drink_id):
    result = Drink.query.filter_by(drink_id=drink_id).first()

    if not result:
        return jsonify({'message': 'did not find drink with id ' + str(drink_id)}), 400

    return jsonify(drinkSchema.dump(result)), 200
