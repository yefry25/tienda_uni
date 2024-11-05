from flask import Blueprint, request, jsonify

bp = Blueprint('UserController', __name__)

@bp.route('/createUser', methods=["POST"])
def AddUser():
    from app.Services.UserService import CreateUser
    userData = request.json

    result, statusCode = CreateUser(userData)
    return jsonify(result), statusCode

@bp.route('/users', methods=["GET"])
def get_users():
    from app.Services.UserService import get_users
    result, statusCode = get_users()
    return jsonify(result), statusCode

@bp.route('/updateUser/<int:id>', methods=["PUT"])
def update_user(id):
    from app.Services.UserService import update_user
    data = request.json
    result, statusCode = update_user(id, data)
    return jsonify(result), statusCode

@bp.route('/login', methods=["POST"])
def Login():
    from app.Services.UserService import Login

    # Recibe los datos de la solicitud (JSON) desde el cuerpo de la petición
    data = request.json
    
    # Extrae username y password del JSON
    userName = data.get('nickName')
    password = data.get('password')

    result, statusCode = Login(userName, password)
    return jsonify(result), statusCode