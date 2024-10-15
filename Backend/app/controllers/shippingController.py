from flask import Blueprint, request, jsonify

bp = Blueprint('shipping_controller', __name__)

@bp.route('/createShipping', methods=['POST'])
def add_user():
    from app.services.shippingService import create_shipping
    data = request.json
    result, statusCode = create_shipping(data)
    return jsonify(result), statusCode

@bp.route('/shippings', methods=["GET"])
def get_users():
    from app.services.shippingService import get_shippings
    result, statusCode = get_shippings()
    return jsonify(result), statusCode