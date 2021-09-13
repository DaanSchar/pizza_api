from extensions import db
#TODO: implement deliverer system, coupon system

pizza_topping = db.Table('pizza_topping',
                         db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.pizza_id')),
                         db.Column('topping_id', db.Integer, db.ForeignKey('topping.topping_id'))
                         )

pizza_order = db.Table('pizza_order',
                       db.Column('order_id', db.ForeignKey('order.order_id')),
                       db.Column('pizza_id', db.ForeignKey('pizza.pizza_id')),
                       )

drink_order = db.Table('drink_order',
                       db.Column('order_id', db.ForeignKey('order.order_id')),
                       db.Column('drink_id', db.ForeignKey('drink.drink_id')),
                       )

dessert_order = db.Table('dessert_order',
                         db.Column('order_id', db.ForeignKey('order.order_id')),
                         db.Column('dessert_id', db.ForeignKey('dessert.dessert_id')),
                         )


class Pizza(db.Model):
    pizza_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)

    toppings = db.relationship('Topping', secondary=pizza_topping, backref=db.backref('pizza_topping'))


class Topping(db.Model):
    topping_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Dessert(db.Model):
    dessert_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Drink(db.Model):
    drink_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)


class Deliverer(db.Model):
    deliverer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_code = db.Column(db.String(), nullable=False)
    in_progress = db.Column(db.Boolean, nullable=False, default=False)


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.customer_id), nullable=False)
    date_of_order = db.Column(db.DateTime, nullable=False)
    estimated_delivery_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    # assigned_deliverer = db.Column(db.Integer, db.ForeignKey('deliverer.deliverer_id'))

    pizzas = db.relationship('Pizza', secondary=pizza_order, backref=db.backref('pizza_order'))
    drinks = db.relationship('Drink', secondary=drink_order, backref=db.backref('drink_order'))
    desserts = db.relationship('Dessert', secondary=dessert_order, backref=db.backref('dessert_order'))








