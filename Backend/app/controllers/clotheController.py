from flask import Blueprint, request, jsonify

bp = Blueprint('clothe_controller', __name__)

@bp.route('/createClothe', methods=['POST'])
def add_user():
    from app.services.clothesService import create_clothe
    data = request.json
    result, statusCode = create_clothe(data)
    return jsonify(result), statusCode

@bp.route('/clothes', methods=["GET"])
def get_users():
    from app.services.clothesService import get_clothes
    result, statusCode = get_clothes()
    return jsonify(result), statusCode