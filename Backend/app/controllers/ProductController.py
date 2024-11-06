from flask import Blueprint, request, jsonify

bp = Blueprint('ProductController', __name__)

@bp.route('/addProduct', methods=['POST'])
def addProduct():
    from app.Services.ProductService import CreateProduct
    data = request.json
    result, statusCode = CreateProduct(data)
    return jsonify(result), statusCode

@bp.route('/products', methods=["GET"])
def GetProducts():
    from app.Services.ProductService import GetProducts
    result, statusCode = GetProducts()
    return jsonify(result), statusCode