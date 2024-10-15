from flask import Blueprint, request, jsonify

bp = Blueprint('bill_controller', __name__)

@bp.route('/createBill', methods=['POST'])
def add_user():
    from app.services.billService import create_bill
    data = request.json
    result, statusCode = create_bill(data)
    return jsonify(result), statusCode

@bp.route('/bills', methods=["GET"])
def get_users():
    from app.services.billService import get_bills
    result, statusCode = get_bills()
    return jsonify(result), statusCode