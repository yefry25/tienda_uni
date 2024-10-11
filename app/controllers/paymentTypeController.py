from flask import Blueprint, request, jsonify

bp = Blueprint('paymentType_controller', __name__)

@bp.route('/createPaymentType', methods=['POST'])
def add_user():
    from services.paymentTypeService import create_paymentType
    data = request.json
    result = create_paymentType(data)
    return jsonify(result)