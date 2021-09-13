from flask import Blueprint

from service.order import OrderService

order_bp = Blueprint('order_bp', __name__)


@order_bp.route('', methods=['POST'])
def post_order():
    return OrderService.post_order()


@order_bp.route('/<customer_id>')
def get_orders(customer_id):
    return OrderService.get_orders(customer_id)


@order_bp.route('/current/<customer_id>')
def get_current_order(customer_id):
    return OrderService.get_current_order(customer_id)


@order_bp.route('/current/<customer_id>', methods=['PUT'])
def cancel_current_order(customer_id):
    return OrderService.cancel_current_order(customer_id)