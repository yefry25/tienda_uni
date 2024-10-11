from flask import Blueprint, request, jsonify

bp = Blueprint('bill_controller', __name__)

@bp.route('/createBill', methods=['POST'])
def add_user():
    from services.billService import create_bill
    data = request.json
    result = create_bill(data)
    return jsonify(result)

@bp.route('/bills', methods=["GET"])
def get_users():
    from services.billService import get_bills
    result = get_bills()
    return jsonify(result)