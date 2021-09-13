from extensions import ma
from models.model import Pizza, Topping, Dessert, Drink, Customer, Order


class ToppingSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Topping
        load_instance = True

    topping_id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()


class PizzaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pizza
        load_instance = True

    pizza_id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    vegan = ma.auto_field()
    toppings = ma.Nested(ToppingSchema, many=True)


class DessertSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Dessert
        load_instance = True

    dessert_id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()


class DrinkSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Drink
        load_instance = True

    drink_id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()


class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order
        load_instance = True

    order_id = ma.auto_field()
    customer_id = ma.auto_field()
    date_of_order = ma.auto_field()
    estimated_delivery_time = ma.auto_field()
    pizzas = ma.Nested(PizzaSchema, many=True)
    drinks = ma.Nested(DrinkSchema, many=True)
    desserts = ma.Nested(DessertSchema, many=True)
    status = ma.auto_field()


class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
        load_instance = True

    customer_id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    phone = ma.auto_field()
    address = ma.auto_field()