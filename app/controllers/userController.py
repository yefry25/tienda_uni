from flask import Blueprint, request, jsonify

bp = Blueprint('user_controller', __name__)

@bp.route('/createUser', methods=['POST'])
def add_user():
    from app.services.userService import create_user
    data = request.json
    result = create_user(data)
    return jsonify(result)

@bp.route('/users', methods=["GET"])
def get_users():
    from app.services.userService import get_users
    result = get_users()
    return jsonify(result)