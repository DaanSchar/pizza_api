
from models.model import Deliverer
from schemas.schema import DelivererSchema

deliverer_schema = DelivererSchema()


def get_available_deliverer(address):
    zip_code = address[0:4]
    deliverer = Deliverer.query.filter_by(zip_code=zip_code, in_progress=False).first()
    return deliverer


def get_deliverers():
    return Deliverer.query.all()



def get_deliverer(id):
    return Deliverer.query.filter_by(deliverer_id=id).first()
