# import werkzeug
#
# werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask import Flask
from bicsubi import api


app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
