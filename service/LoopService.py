import datetime

from extensions import db

from apscheduler.schedulers.background import BackgroundScheduler

from service.customer import CustomerService
from service.order import OrderService, DelivererService


class LoopService:
    def __init__(self, app):
        self.app = app
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.loop, trigger="interval", seconds=5)
        scheduler.start()

    def loop(self):
        with self.app.app_context():
            print('looping')
            self.assign_deliverers()
            self.return_deliverers()
            self.deliver_orders()


    # sets order status to delivered 10 minutes after departure of deliverer
    def deliver_orders(self):
        orders = OrderService.get_orders_on_delivery()

        for order in orders:
            deliverer = order.deliverer
            if datetime.datetime.now() >= deliverer.time_of_departure + datetime.timedelta(seconds=10):
                order.status = 'delivered'
                db.session.commit()


    # after 30 minutes sets deliverers which were delivering back to available
    def return_deliverers(self):
        deliverers_ = DelivererService.get_deliverers()

        for deliverer in deliverers_:
            if deliverer.in_progress:
                if datetime.datetime.now() >= deliverer.time_of_departure + datetime.timedelta(seconds=30):
                    deliverer.in_progress = False
                    deliverer.time_of_departure = datetime.datetime.min
                    db.session.commit()


    # assigns an available deliverer to an order after it's been in process for at least 5 minutes
    def assign_deliverers(self):
        orders = OrderService.get_orders_that_need_deliverers()
        for order in orders:
            customer = CustomerService.get_customer(order.customer_id)
            deliverer = DelivererService.get_available_deliverer(customer.address)

            if deliverer:
                order.deliverer_id = deliverer.deliverer_id
                order.estimated_delivery_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
                order.status = 'out for delivery'
                deliverer.in_progress = True
                deliverer.time_of_departure = datetime.datetime.now()
                db.session.commit()
