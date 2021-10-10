import init_db
from init import create_app
from service import LoopService

app = create_app()
init_db.init(app)

loop = LoopService.LoopService(app)
