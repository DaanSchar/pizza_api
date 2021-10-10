import os

from flask import Flask

from blueprints.customer import customer_bp
from blueprints.menu import menu_bp
from blueprints.order import order_bp
from extensions import db, ma


def create_app():
    app = Flask(__name__)

    db_path = os.path.join(os.path.dirname(__file__), '../database.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)
    ma.init_app(app)

    BASE = '/api/v1'

    app.register_blueprint(menu_bp, url_prefix=BASE + '/menu')
    app.register_blueprint(order_bp, url_prefix=BASE + '/order')
    app.register_blueprint(customer_bp, url_prefix=BASE + '/customer')

    return app
