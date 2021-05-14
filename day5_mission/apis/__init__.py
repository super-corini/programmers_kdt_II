from flask_restx import Api

from .whoami import api as ns1
from .echo   import api as ns2
from .weapon import api as ns3

api = Api(
    title='Bicsubi',
    version='0.1',
    description='First mission for weekly assignment.',
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)