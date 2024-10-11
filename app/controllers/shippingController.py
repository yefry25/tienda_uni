from flask import Blueprint, request, jsonify

bp = Blueprint('shipping_controller', __name__)

@bp.route('/createShipping', methods=['POST'])
def add_user():
    from services.shippingService import create_shipping
    data = request.json
    result = create_shipping(data)
    return jsonify(result)

@bp.route('/shippings', methods=["GET"])
def get_users():
    from services.shippingService import get_shippings
    result = get_shippings()
    return jsonify(result)