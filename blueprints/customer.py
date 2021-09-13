from flask import Blueprint

from service.customer import CustomerService

customer_bp = Blueprint('customer_bp', __name__)


@customer_bp.route('/<customer_id>')
def get_customer_info(customer_id):
    return CustomerService.get_customer_info(customer_id)