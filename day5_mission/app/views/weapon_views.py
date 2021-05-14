from flask import Blueprint, render_template, request
from app import db


bp = Blueprint("weapon", __name__, url_prefix="/weapon")
weapon = db["weapon"]


# GET, 자료를 조회한다.
@bp.route("/")
def weapon_get():
    return render_template("weapon_list.html", weapon_list=weapon.all())


# POST, 자료를 추가한다.
@bp.route("/", methods=["POST"])
def weapon_create():
    try:
        data = request.get_json()
        new_name = data["name"]
        new_stock = data["stock"]
    except Exception as e:
        return f"잘못된 요청입니다: {e}", 400

    # 예외처리
    if not isinstance(new_name, str):
        return f"잘못된 요청입니다: name이 문자열이 아님", 400
    elif not isinstance(new_stock, int):
        return f"잘못된 요청입니다: stock이 int형 숫자가 아님", 400
    elif new_stock < 0:
        return f"잘못된 요청입니다: stock이 음수임", 400

    # 이름이 같은 무기가 있으면 추가하지 않음
    new_data = dict(name=new_name, stock=new_stock)
    result = weapon.insert_ignore(new_data, ["name"])
    if not result:
        return "같은 이름의 무기가 있습니다.", 400
    return render_template("weapon_list.html", weapon_list=weapon.all())


# PUT, 자료를 업데이트한다.
@bp.route("/<string:string>", methods=["PUT"])
def weapon_update(string):
    try:
        data = request.get_json()
        new_stock = data["stock"]
    except Exception as e:
        return f"잘못된 요청입니다: {e}", 400

    # 예외처리
    if not isinstance(new_stock, int):
        return f"잘못된 요청입니다: stock이 int형 숫자가 아님", 400
    elif new_stock < 0:
        return f"잘못된 요청입니다: stock이 음수임", 400

    new_data = dict(name=string, stock=new_stock)
    result = weapon.update(new_data, ["name"])
    if not result:
        return f"이름이 {string}인 데이터가 없습니다."
    return render_template("weapon_list.html", weapon_list=weapon.all())


# DELETE, 자료를 삭제한다.
@bp.route("/<string:string>", methods=["DELETE"])
def weapon_delete(string):
    result = weapon.delete(name=string)
    if result:
        return f"{string} 데이터가 삭제되었습니다."
    return f"이름이 {string}인 데이터가 없습니다."
