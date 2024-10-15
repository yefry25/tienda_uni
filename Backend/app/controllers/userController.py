from flask import Blueprint, request, jsonify

bp = Blueprint('user_controller', __name__)

@bp.route('/createUser', methods=["POST"])
def add_user():
    from app.services.userService import create_user
    data = request.json
    result, statusCode = create_user(data)
    return jsonify(result), statusCode

@bp.route('/users', methods=["GET"])
def get_users():
    from app.services.userService import get_users
    result, statusCode = get_users()
    return jsonify(result), statusCode

@bp.route('/updateUser/<int:id>', methods=["PUT"])
def update_user(id):
    from app.services.userService import update_user
    data = request.json
    result, statusCode = update_user(id, data)
    return jsonify(result), statusCode

@bp.route('/login', methods=["POST"])
def login():
    from app.services.userService import login

    # Recibe los datos de la solicitud (JSON) desde el cuerpo de la petición
    data = request.json
    
    # Extrae username y password del JSON
    userName = data.get('userName')
    password = data.get('password')

    result, statusCode = login(userName, password)
    return jsonify(result), statusCode