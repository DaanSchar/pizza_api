from flask import jsonify

from models.model import Dessert
from schemas.schema import DessertSchema

dessertSchema = DessertSchema()
dessertSchemas = DessertSchema(many=True)

def get_desserts():
    result = Dessert.query.all()

    if not result:
        return jsonify({'message': 'no desserts found'}), 400

    return jsonify(dessertSchemas.dump(result)), 200


def get_dessert(dessert_id):
    result = Dessert.query.filter_by(dessert_id=dessert_id).first()

    if not result:
        return jsonify({'message': 'no dessert found with id' + str(dessert_id)}), 400

    return jsonify(dessertSchema.dump(result)), 200