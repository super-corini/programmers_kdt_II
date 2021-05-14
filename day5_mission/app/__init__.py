from flask import Flask
import dataset


db = dataset.connect("sqlite:///bicsubi.db")


def create_app():
    app = Flask(__name__)

    from .views import main_views, weapon_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(weapon_views.bp)

    return app
