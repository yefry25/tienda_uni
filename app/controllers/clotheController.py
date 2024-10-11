from flask import Blueprint, request, jsonify

bp = Blueprint('clothe_controller', __name__)

@bp.route('/createClothe', methods=['POST'])
def add_user():
    from services.clothesService import create_clothe
    data = request.json
    result = create_clothe(data)
    return jsonify(result)

@bp.route('/clothes', methods=["GET"])
def get_users():
    from services.clothesService import get_clothes
    result = get_clothes()
    return jsonify(result)