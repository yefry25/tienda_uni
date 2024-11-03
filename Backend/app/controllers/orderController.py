from flask import Blueprint, request, jsonify

bp = Blueprint('OrderController', __name__)

@bp.route('/createOrder', methods=['POST'])
def CreateOrder():
    from app.Services.OrderService import CreateOrder
    data = request.json

    result, statusCode = CreateOrder(data)
    return jsonify(result), statusCode

@bp.route('/orders', methods=["GET"])
def get_users():
    from app.Services.OrderService import get_orders
    result, statusCode = get_orders()
    return jsonify(result), statusCode

@bp.route('/orderDetail/<int:idUsuario>', methods=["GET"])
def update_user(idUsuario):
    from app.Services.OrderService import getOrderDetailByUserId
    result, statusCode = getOrderDetailByUserId(idUsuario)
    return jsonify(result), statusCode