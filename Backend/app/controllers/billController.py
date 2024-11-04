from flask import Blueprint, request, jsonify

bp = Blueprint('BillController', __name__)

@bp.route('/createBill', methods=['POST'])
def CreateBill():
    from app.Services.BillService import CreateBill
    data = request.json

    result, statusCode = CreateBill(data)
    return jsonify(result), statusCode

@bp.route('/bills', methods=["GET"])
def get_users():
    from app.Services.BillService import get_bills
    result, statusCode = get_bills()
    return jsonify(result), statusCode