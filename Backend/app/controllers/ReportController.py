from flask import Blueprint, jsonify

bp = Blueprint('ReportController', __name__)

@bp.route('/salesByProduct', methods=["GET"])
def SaleByProduct():
    from app.Services.ReportService import SaleByProduct
    result, statusCode = SaleByProduct()
    return jsonify(result), statusCode

@bp.route('/salesByCategory', methods=["GET"])
def SaleByCategory():
    from app.Services.ReportService import SaleByCategory
    result, statusCode = SaleByCategory()
    return jsonify(result), statusCode

@bp.route('/statusOfUser', methods=["GET"])
def StatusOfUser():
    from app.Services.ReportService import StatusOfUsers
    result, statusCode = StatusOfUsers()
    return jsonify(result), statusCode

@bp.route('/salesForUser', methods=["GET"])
def SalesForUser():
    from app.Services.ReportService import SalesForUsers
    result, statusCode = SalesForUsers()
    return jsonify(result), statusCode

@bp.route('/productInventory', methods=["GET"])
def ProductInventory():
    from app.Services.ReportService import ProductInventory
    result, statusCode = ProductInventory()
    return jsonify(result), statusCode

@bp.route('/orderStatus', methods=["GET"])
def OrderStatus():
    from app.Services.ReportService import OrderStatus
    result, statusCode = OrderStatus()
    return jsonify(result), statusCode

@bp.route('/issuedBills', methods=["GET"])
def IssuedBills():
    from app.Services.ReportService import IssuedBills
    result, statusCode = IssuedBills()
    return jsonify(result), statusCode

@bp.route('/montlyIncome', methods=["GET"])
def MonthlyIncome():
    from app.Services.ReportService import MonthlyIncome
    result, statusCode = MonthlyIncome()
    return jsonify(result), statusCode
