from flask import Blueprint, request, jsonify

bp = Blueprint('ProductController', __name__)

@bp.route('/createClothe', methods=['POST'])
def add_user():
    from app.Services.ProductService import create_clothe
    data = request.json
    result, statusCode = create_clothe(data)
    return jsonify(result), statusCode

@bp.route('/products', methods=["GET"])
def GetProducts():
    from app.Services.ProductService import GetProducts
    result, statusCode = GetProducts()
    return jsonify(result), statusCode