from flask import Blueprint
from service.menu import PizzaService, DrinkService, DessertService

menu_bp = Blueprint('menu_bp', __name__)


@menu_bp.route('/pizzas')
def get_pizzas():
    return PizzaService.get_pizzas()


@menu_bp.route('/pizzas/<pizza_id>')
def get_pizza(pizza_id):
    return PizzaService.get_pizza(pizza_id)


@menu_bp.route('/desserts')
def get_desserts():
    return DessertService.get_desserts()


@menu_bp.route('/desserts/<dessert_id>')
def get_dessert(dessert_id):
    return DessertService.get_dessert(dessert_id)


@menu_bp.route('/drinks')
def get_drinks():
    return DrinkService.get_drinks()


@menu_bp.route('/drinks/<drink_id>')
def get_drink(drink_id):
    return DrinkService.get_drink(drink_id)


