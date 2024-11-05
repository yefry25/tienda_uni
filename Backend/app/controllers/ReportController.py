from flask import Blueprint, request, jsonify

bp = Blueprint('ReportController', __name__)

@bp.route('/salesByProduct', methods=["GET"])
def SaleByProduct():
    from app.Services.ReportService import SaleByProduct
    result, statusCode = SaleByProduct()
    return jsonify(result), statusCode
