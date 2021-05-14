from flask import Blueprint


bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def hello_world():
    return "Hello, World!"


@bp.route("/whoami")
def whoami():
    return {"name": "Bing-su"}


@bp.route("/<string:string>")
def string(string):
    return {"value": string}

