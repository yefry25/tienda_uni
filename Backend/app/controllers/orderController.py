from flask import Blueprint, request, jsonify

bp = Blueprint('order_controller', __name__)

@bp.route('/createOrder', methods=['POST'])
def add_user():
    from app.services.orderService import create_order
    data = request.json
    result, statusCode = create_order(data)
    return jsonify(result), statusCode

@bp.route('/orders', methods=["GET"])
def get_users():
    from app.services.orderService import get_orders
    result, statusCode = get_orders()
    return jsonify(result), statusCode

@bp.route('/orderDetail/<int:idUsuario>', methods=["GET"])
def update_user(idUsuario):
    from app.services.orderService import getOrderDetailByUserId
    result, statusCode = getOrderDetailByUserId(idUsuario)
    return jsonify(result), statusCode