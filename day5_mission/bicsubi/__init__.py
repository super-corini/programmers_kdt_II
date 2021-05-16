from flask_restx import Api
import bicsubi.core as core
import bicsubi.extended as extended
from .db_core import BicsubiDb

api = Api(version='0.1.0', title='bicsubi', ordered=True,
          description='Assistant of Bronze-man')
api.add_namespace(core.api)
api.add_namespace(extended.api)
core.db = BicsubiDb('bicsubi.sqlite')
extended.db = core.db
