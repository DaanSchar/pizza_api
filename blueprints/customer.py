from flask import Blueprint, jsonify

from service.customer import CustomerService

customer_bp = Blueprint('customer_bp', __name__)


@customer_bp.route('/<customer_id>')
def get_customer_info(customer_id):
    return jsonify(CustomerService.get_customer_info(customer_id))


@customer_bp.route('/discount')
def use_discount():
    return jsonify(CustomerService.use_discount())
